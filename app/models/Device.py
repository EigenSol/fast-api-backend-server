# models/Device.py
from piccolo.table import Table
from piccolo.columns import Varchar, ForeignKey
from models.AppUser import AppUser

class Device(Table, tablename="devices"):
    device_name = Varchar()
    app_user_id = ForeignKey(references=AppUser)
