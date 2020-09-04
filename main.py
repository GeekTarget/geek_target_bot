import logging
from aiogram import Bot, Dispatcher, executor
import config
import handlers
import asyncio

# Main variable
logging.basicConfig(level=logging.INFO)
bot = Bot(token=config.token)
dp = Dispatcher(bot)

# Running bot
if __name__ == '__main__':
    from handlers import dp
    print(1)
    dp.loop.create_task(handlers.get_new_music())
    print(1)
    #dp.loop.create_task(handlers.new_film_get())
    #dp.loop.create_task(handlers.rambler_news_get())
    #dp.loop.create_task(handlers.igromania_get())
    #dp.loop.create_task(handlers.habr_get())
        
    executor.start_polling(dp, skip_updates=True)
