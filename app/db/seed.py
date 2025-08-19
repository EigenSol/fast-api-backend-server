
import os, sys
sys.path.append(os.path.abspath(os.path.join(__file__, "../..")))
from util.debug import debug, DEBUG_FILE

import asyncio
from piccolo.engine import engine_finder
from seeders import seed_users



async def main():
    await engine_finder().start_connection_pool()

    debug("⏳ Seeding users...")
    await seed_users.run()
    debug("✅ Users seeded.")

    await engine_finder().close_connection_pool()

if __name__ == "__main__":
    asyncio.run(main())
