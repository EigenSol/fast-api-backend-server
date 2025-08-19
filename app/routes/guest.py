from controllers.dev.SubscriptionController import SubscriptionController
# from middlewares.SessionKeyMiddleware import SessionKeyMiddleware

guest_routes = [
    {
        "name": "subscriptions",
        "method": "GET",
        "path": "/subscriptions",
        "handler": SubscriptionController.list,
    }
]
