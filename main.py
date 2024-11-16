from fastapi import FastAPI
from aiogram import types
from databaseorm import create_tables
from bot import bot, dp
from config import *

TELEBOT_ENDPOINT = f'/bot/{TELEGRAM_BOT_TOKEN}'
WEBHOOK = f'{NGROK_TUNNEL}{TELEBOT_ENDPOINT}'

app = FastAPI()

@app.on_event('startup')
async def startup():
    create_tables()
    web_inf = await bot.get_webhook_info()
    if web_inf.url != WEBHOOK:
        await bot.set_webhook(WEBHOOK)

@app.post(TELEBOT_ENDPOINT)
async def get_updates(upd: dict):
    telegram_update = types.Update(**upd)
    await dp.feed_update(bot=bot, update=telegram_update)

@app.on_event('shutdown')
async def shutdown():
    await bot.session.close()