from .middlewares import middleware_config
from .db import db_config
from util.env import env


app_config = {
    "middlewares": middleware_config,
    "db": db_config,
    "debug": env("DEBUG", 1)
}