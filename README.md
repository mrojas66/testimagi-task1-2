# TEST 1 y 2

This is the new API for test. 

## Project Structure

- 📂 **my_project/**
  - 📂 **alembic/**
    - 📂 **versions/**
  - 📂 **api/**
  - 📂 **services/**
  - 📂 **models/**
  - 📂 **entities/**
  - 📂 **core/**
  - 📂 **tests/**
  - 📂 **api/**
  - 📄 **main.py**
  - 📄 **alembic.ini**
  - 📄 **.env**
  - 📄 **requirements.txt**


## Main Libraries

- **FastAPI**: A modern, fast web framework for building APIs with Python.

- **SQLAlchemy**: ORM to handle database operations.

- **Alembic**: Database migration tool for SQLAlchemy.

## Initial Setup

1. Clone the repository.
2. Create a virtual environment and activate it.
3. Install dependencies using `pip install -r requirements.txt`.
4. Set up environment variables in `.env`.

For more instructions on how to use and deploy the project, (add pertinent instructions).

## Contributing

Instructions on how other developers can contribute to the project, coding rules, etc.

## License

Licensing information for the project, if any.

## Start up 

python -m venv venv
source venv/bin/activate

Remeber the migration 
`alembic upgrade head -> Actualizar.` 

Generar una nueva migracion 

`alembic revision --autogenerate -m "Modificar usuarios"`



