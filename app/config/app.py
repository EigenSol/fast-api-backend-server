from .middlewares import middleware_config
from .db import db_config

app_config = {
    "middlewares": middleware_config,
    "db": db_config,
}