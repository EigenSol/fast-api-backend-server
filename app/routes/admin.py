from controllers.admin.UserManagementController import UserManagementController

admin_routes = [
    {
        'path': '/users',
        'group': [
            {
                "name":"devices",
                'method': 'GET',
                'path': '/{id}/devices',
                'handler': UserManagementController.get_user_devices,
            },
        ]
    }
]