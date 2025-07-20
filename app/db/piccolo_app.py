import os
from piccolo.conf.apps import AppConfig
from models.AppUser import AppUser  

MIGRATIONS_PATH = os.path.join(
    os.path.dirname(__file__),
    "migrations",
)

APP_CONFIG = AppConfig(
    app_name="db",
    migrations_folder_path=MIGRATIONS_PATH,
    table_classes=[AppUser],
)
