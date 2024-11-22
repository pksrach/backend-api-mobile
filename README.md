## Scripts Used

- **Create a virtual environment**:
  ```bash
  python -m venv venv
  ```

- **Activate the virtual environment**:
  ```bash
    source venv/Scripts/activate
    or
    source venv/bin/activate
    ```

- **Create a `.env` file**:
    ```bash
    touch .env
    ```

- **Add the following environment variables to the `.env` file**:
- **PG_HOST**=localhost
- **PG_PORT**=5432
- **PG_USER**=postgres
- **PG_PASSWORD**=postgres
- **PG_DB**=efurniture
- **SECRET_KEY**=your_secret_key


- **Install the required packages**:
  ```bash
  pip install -r requirements.txt
  ```
  
- **Initialize the database**:
  ```bash
  alembic init alembic
  ```

- **Generate database migration**:
  ```bash
  alembic revision --autogenerate -m "Initial migration"
  ```
  
- **Run the database migrations**:
  ```bash
  alembic upgrade heads
  ```

- **Run the FastAPI server**:
  ```bash
  uvicorn app.main:app --reload
  ```