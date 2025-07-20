from middlewares.SessionKeyMiddleware import SessionKeyMiddleware

middleware_config = {
    "aliases": {
        "session": SessionKeyMiddleware,
    }
}