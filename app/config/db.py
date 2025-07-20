import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from util.env import env

db_config = {
    "postgres": {
        "database": env("POSTGRES_DATABASE", "ea_app_db"),
        "user":     env("POSTGRES_USER",     "postgres" ),
        "password": env("POSTGRES_PASSWORD", "root"     ),
        "host":     env("POSTGRES_HOST",     "localhost"),
        "port":     env("POSTGRES_PORT",      5432      ),
    },
    'mysql': {
        "host": None,
        "user": None,
        "password": None,
        "database": None,
    }
}