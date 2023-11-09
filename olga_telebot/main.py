from aiogram import Bot, Dispatcher, types
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton
from dotenv import load_dotenv

import logging
import os


load_dotenv()
API_TOKEN = os.getenv('API_TOKEN')

bot = Bot(token=API_TOKEN)

logging.basicConfig(level=logging.INFO)

dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    button = KeyboardButton(text='Привет!')
    keyboard.add(button)
    await message.reply(text='Привет, я твой бот! Чем могу помочь?', reply_markup=keyboard)


if __name__ == '__main__':
    from aiogram import executor

    executor.start_polling(dp, skip_updates=True)
