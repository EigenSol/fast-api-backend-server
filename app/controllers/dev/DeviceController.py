from fastapi import HTTPException
from models.Device import Device
from models.AppUser import AppUser

class DeviceController:

    @staticmethod
    async def list(request):
        return await Device.select()

    @staticmethod
    async def get(request):
        device_id = int(request.path_params.get("id"))
        device = await Device.objects().where(Device.id == device_id).first()
        if not device:
            raise HTTPException(404, "Device not found")
        return device

    @staticmethod
    async def create(request):
        data = await request.json()
        device = await Device(**data).save().returning()
        return device

    @staticmethod
    async def update(request):
        device_id = int(request.path_params.get("id"))
        device = await Device.objects().where(Device.id == device_id).first()
        if not device:
            raise HTTPException(404, "Device not found")
        data = await request.json()
        for k, v in data.items():
            setattr(device, k, v)
        await device.save()
        return device

    @staticmethod
    async def delete(request):
        device_id = int(request.path_params.get("id"))
        device = await Device.objects().where(Device.id == device_id).first()
        if not device:
            raise HTTPException(404, "Device not found")
        await device.remove()
        return {"message": "Device deleted"}
    
    # @staticmethod
    # async def get_user(request):
    #     device_id = int(request.path_params.get("id"))

    #     device = await Device.objects().where(Device.id == device_id).first()
    #     if not device:
    #         raise HTTPException(404, "Device not found")

    #     user = await device.app_user_id.resolve()
    #     if not user:
    #         raise HTTPException(404, "User not found for this device")

    #     return user


    @staticmethod
    async def get_user(request):
        device_id = int(request.path_params.get("id"))

        device = await Device.objects().where(Device.id == device_id).prefetch(Device.app_user_id).first()
        if not device:
            raise HTTPException(404, "Device not found")

        return device.app_user_id  # already resolved via prefetch
