import logging
from aiogram import Bot, Dispatcher, executor
import config
import handlers
import asyncio
import requests

# Main variable
logging.basicConfig(level=logging.INFO)
bot = Bot(token=config.token)
dp = Dispatcher(bot)


if __name__ == '__main__':
    from handlers import dp
    dp.loop.create_task(handlers.get_new_music()) 
    dp.loop.create_task(handlers.new_film_get())
    dp.loop.create_task(handlers.rambler_news_get())
    dp.loop.create_task(handlers.igromania_get())
    dp.loop.create_task(handlers.habr_get())
        
    executor.start_polling(dp, skip_updates=True)
