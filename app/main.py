from datetime import timedelta
from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from . import models, schemas, crud, auth, dependencies
from .database import engine
from typing import Annotated
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.post("/token", response_model=schemas.Token)
async def login_for_access_token(form_data: schemas.UserSchema, db: Annotated[Session, Depends(dependencies.get_db)]):
    user = crud.authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=auth.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = auth.create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

@app.post("/users/", response_model=schemas.UserSchema)
async def create_user(user: schemas.UserSchema, db: Annotated[Session, Depends(dependencies.get_db)]):
    db_user = crud.get_user(db, username=user.username)
    if db_user:
        raise HTTPException(status_code=400, detail="Username already registered")
    hashed_password = auth.get_password_hash(user.password)
    return crud.create_user(db=db, user=user, hashed_password=hashed_password)

auth_scheme = HTTPBearer()
@app.get("/users/me/", response_model=schemas.TokenData)
async def read_users_me(token: Annotated[HTTPAuthorizationCredentials, Depends(auth_scheme)], 
                        current_user: Annotated[schemas.TokenData, Depends(auth.get_current_user)]):
    return current_user
