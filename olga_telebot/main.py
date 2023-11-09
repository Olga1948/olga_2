from aiogram import Bot, Dispatcher, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from dotenv import load_dotenv

import logging
import os
import psycopg2


load_dotenv()
API_TOKEN = os.getenv('API_TOKEN')
DATABASE_URL = 'postgresql://username:password@localhost:5432/olga_db'

bot = Bot(token=API_TOKEN)

logging.basicConfig(level=logging.INFO)

dp = Dispatcher(bot)

conn = psycopg2.connect(DATABASE_URL, sslmode='prefer')
cursor = conn.cursor()

@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    button = KeyboardButton(text='Привет!')
    keyboard.add(button)
    await message.reply(text='Привет, я твой бот! Чем могу помочь?', reply_markup=keyboard)


@dp.message_handler(commands=['викторина'])
async def get_viktorina_command(message: types.Message):
    cursor.execute('SELECT question, answer FROM qa')
    qa_data = cursor.fetchall()

    for row in qa_data:
        question, answer = row
        await message.reply(text=f'Вопрос: {question}\nОтвет: {answer}')

if __name__ == '__main__':
    from aiogram import executor

    executor.start_polling(dp, skip_updates=True)
