from controllers.dev.DeviceController import DeviceController
# from middlewares.SessionKeyMiddleware import SessionKeyMiddleware

device_routes = [
    {
        "group": [
            {
                "method": "GET",
                "path": "/",
                "handler": DeviceController.list,
            },
            {
                "method": "POST",
                "path": "/",
                "handler": DeviceController.create
            },
            {
                "method": "GET",
                "path": "/{id}",
                "handler": DeviceController.get
            },
            {
                "method": "PUT",
                "path": "/{id}",
                "handler": DeviceController.update
            },
            {
                "method": "DELETE",
                "path": "/{id}",
                "handler": DeviceController.delete
            },
            {
                "method": "GET",
                "path": "/{id}/user",
                "handler": DeviceController.get_user
            }
        ]
    }
]
