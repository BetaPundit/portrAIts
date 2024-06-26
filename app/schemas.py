from pydantic import BaseModel

class UserSchema(BaseModel):
    username: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: str | None = None

class PromptSchema(BaseModel):
    prompt: str | None
    style: str | None