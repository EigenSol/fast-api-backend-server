from routes.users import user_routes
from routes.devices import device_routes
from routes.admin import admin_routes
from routes.guest import guest_routes

routes = [
    {"name":"user.", "path": "/users", "group": user_routes},
    {"name":"device.", "path": "/devices", "group": device_routes},
    {"name":"admin.", "path": "/admin", "group": admin_routes},
    {"name":"guest.", "group": guest_routes},
]