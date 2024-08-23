import sys
import logging

if sys.platform == "win32":
    import asyncio
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

from bot.handlers.start_menu_handler import router
from bot.create_bot import dp, bot
from bot.handlers.authorisation import router_auth
from bot.handlers.registrartion import router_reg
from bot.handlers.auth.create_FO_po_TO import router_create

async def main():
    dp.include_routers(router, router_auth, router_reg, router_create)
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')

