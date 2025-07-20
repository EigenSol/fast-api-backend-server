# piccolo_conf.py
from piccolo.engine.postgres import PostgresEngine
from piccolo.conf.apps import AppRegistry
from util.config import config

DB = PostgresEngine(
    config={
        "database": config("db.postgres.database",  "ea_app_db"),
        "user":     config("db.postgres.user",      "postgres"),
        "password": config("db.postgres.password",  "root"),
        "host":     config("db.postgres.host",      "localhost"),
        "port":     config("db.postgres.port",      5432),
    }
)



APP_REGISTRY = AppRegistry(
    apps=[
        "db.piccolo_app",
    ]
)
