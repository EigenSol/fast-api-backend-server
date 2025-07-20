from controllers.dev.SubscriptionController import SubscriptionController
# from middlewares.SessionKeyMiddleware import SessionKeyMiddleware

guest_routes = [
    {
        "method": "GET",
        "path": "/subscriptions",
        "handler": SubscriptionController.list,
    }
]
