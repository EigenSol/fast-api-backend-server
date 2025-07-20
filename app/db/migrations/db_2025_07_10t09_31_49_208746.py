from piccolo.apps.migrations.auto.migration_manager import MigrationManager
from piccolo.columns.column_types import Varchar, ForeignKey
from piccolo.columns.indexes import IndexMethod
from models.AppUser import AppUser

ID = "2025-07-10T09:31:49:208746"
VERSION = "1.27.1"
DESCRIPTION = ""


async def forwards():
    manager = MigrationManager(
        migration_id=ID, app_name="db", description=DESCRIPTION
    )


    manager.add_table(class_name="Device", tablename="devices")

    manager.add_column(
        table_class_name="Device",
        tablename="devices",
        column_name="device_name",
        column_class=Varchar,
        params={"length": 255},
    )

    manager.add_column(
        table_class_name="Device",
        tablename="devices",
        column_name="app_user_id",
        column_class=ForeignKey,
        params={"references": AppUser},
    )

    return manager
