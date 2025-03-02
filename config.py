import os

DB_CONFIG = {
    "sqlite_path": "./divar.db",
    "postgres": {
        "dbname": os.getenv("POSTGRES_DB", "divar"),
        "user": os.getenv("POSTGRES_USER", "divar_user"),
        "password": os.getenv("POSTGRES_PASSWORD", "divar_password"),
        "host": "postgres",
        "port": "5432",
    },
}
