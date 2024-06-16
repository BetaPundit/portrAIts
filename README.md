# portrAIts: Elevate your portraits with AI-driven artistic brilliance!

## Setup

### Step 1: Create virtual environment    
```shell
python3 -m venv env
source env/bin/activate
```

### Step 2: Install dependencies
```shell
pip install -r requirements.txt
```

### Step 3: Generate SECRET_KEY and store it in .env file
```python
import secrets

SECRET_KEY = secrets.token_hex(32)
print(SECRET_KEY)
```

Your .env file should look like:
```shell
DATABASE_URL=postgresql://portraits_user:yourpassword@localhost/portraits_db
SECRET_KEY=<YOUR_GENERATED_SECRET_KEY>
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

### Step 4: Set Up PostgreSQL

1. Install PostgreSQL:

    ```shell
    sudo apt install -y postgresql postgresql-contrib
    ```

2. Start PostgreSQL service:
    ```shell
    sudo service postgresql start
    ```

3. Create a PostgreSQL user and database:
    ```shell
    sudo -u postgres psql
    ```

4. In the PostgreSQL shell:
    ```sql
    CREATE DATABASE portraits_db;
    CREATE USER portraits_user WITH PASSWORD 'portraits123!';
    ALTER ROLE portraits_user SET client_encoding TO 'utf8';
    ALTER ROLE portraits_user SET default_transaction_isolation TO 'read committed';
    ALTER ROLE portraits_user SET timezone TO 'UTC';
    GRANT ALL PRIVILEGES ON DATABASE portraits_db TO portraits_user;
    \c EXAMPLE_DB postgres
    GRANT ALL ON SCHEMA public TO portraits_user;
    \q
    ```

### Step 5: Run the app
```shell
uvicorn app.main:app --reload
```
