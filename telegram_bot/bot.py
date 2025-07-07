import re
import logging
import sys
import os
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, ROOT_DIR)

from agent.pipeline import main as run_pipeline
from data.sample_data import schema

API_TOKEN = os.environ['TG_API_TOKEN']

logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
dp = Dispatcher()

def escape_md(text: str) -> str:
    escape_chars = r'_*[]()~`>#+-=|{}.!'
    return re.sub(f'([{re.escape(escape_chars)}])', r'\\\1', text)

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.reply("Привет! Введи запрос на естественном языке, и я сгенерирую SQL.")

@dp.message()
async def handle_query(message: types.Message):
    await message.answer("Обрабатываю запрос...")
    result = run_pipeline(message.text, schema)

    if "error" in result:
        await message.answer(f"Ошибка: {escape_md(result['error'])}", parse_mode="MarkdownV2")
    else:
        response_text = (
            f"Тип запроса: {escape_md(result['query_type'])}\n\n"
            f"SQL:\n```\n{escape_md(result['sql'])}\n```\n\n"
            f"Объяснение:\n{escape_md(result['explanation'])}"
        )
        await message.answer(response_text, parse_mode="MarkdownV2")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
