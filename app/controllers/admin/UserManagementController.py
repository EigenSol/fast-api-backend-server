from models.Device import Device

class UserManagementController:

    @staticmethod
    async def get_user_devices(request):
        user_id = int(request.path_params.get("id"))
        devices = await Device.select().where(Device.app_user_id == user_id)
        return devices
