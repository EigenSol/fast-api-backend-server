import os, sys

sys.path.append(os.path.abspath(os.path.join(__file__, "../../../")))

from models.AppUser import AppUser

async def run():
    await AppUser.insert().add(
        AppUser(name="Ali"),
        AppUser(name="Sara"),
    )