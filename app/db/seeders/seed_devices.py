# seeders/device_seeder.py
import os, sys
sys.path.append(os.path.abspath(os.path.join(__file__, "../../../")))

from models.Device import Device
from models.AppUser import AppUser

async def run():
    ali = await AppUser.objects().get(AppUser.name == "Ali")
    sara = await AppUser.objects().get(AppUser.name == "Sara")

    await Device.insert().add(
        Device(device_name="Ali's Phone", app_user_id=ali.id),
        Device(device_name="Sara's Laptop", app_user_id=sara.id),
    )
