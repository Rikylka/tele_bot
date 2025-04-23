import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram import Router, F

from config import BOT_TOKEN
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton

form_router = Router()
dp = Dispatcher()
logger = logging.getLogger(__name__)

start_keyboard = [[KeyboardButton(text='О магазине'), KeyboardButton(text='Товары')],
                  [KeyboardButton(text='Обо мне')]]

back_keyboard = [[KeyboardButton(text='Назад')]]

catalog_keyboard = [[KeyboardButton(text='Тип1'), KeyboardButton(text='Тип2')],
                  [KeyboardButton(text='Тип3')]]

catalog_type1_keyboard = [[KeyboardButton(text='1Товар1'), KeyboardButton(text='1Товар2')],
                  [KeyboardButton(text='1Товар3')]]

catalog_type2_keyboard = [[KeyboardButton(text='2Товар1'), KeyboardButton(text='2Товар2')],
                  [KeyboardButton(text='2Товар3')]]

catalog_type3_keyboard = [[KeyboardButton(text='3Товар1'), KeyboardButton(text='3Товар2')],
                  [KeyboardButton(text='3Товар3')]]


YesorNo_keyboard = [[KeyboardButton(text='Добавить'), KeyboardButton(text='Назад')]]

kb = ReplyKeyboardMarkup(keyboard=start_keyboard, resize_keyboard=True, one_time_keyboard=False)

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG
)

# создаем маршрутизатор
dp = Dispatcher()


async def main():
    bot = Bot(token=BOT_TOKEN)
    await dp.start_polling(bot)


@dp.message(Command('start'))
async def start(message: types.Message):
    await message.reply("Привет.", reply_markup=kb)


@dp.message(lambda message: message.text == "О магазине")
async def stop(message: types.Message):
    await message.reply("Пока.", reply_markup=kb)


@dp.message(Command('help'))
async def help(message: types.Message):
    await message.reply("Я бот-магазин")


@dp.message(lambda message: message.text == "Товары")
async def address(message: types.Message):
    kb = ReplyKeyboardMarkup(keyboard=catalog_keyboard, resize_keyboard=True, one_time_keyboard=False)
    await message.reply(".", reply_markup=kb)

@dp.message(lambda message: message.text == "Обо мне")
async def phone(message: types.Message):
    kb = ReplyKeyboardMarkup(keyboard=back_keyboard, resize_keyboard=True, one_time_keyboard=False)
    await message.reply("Вы человек", reply_markup=kb)


@dp.message(lambda message: message.text == "Назад")
async def site(message: types.Message):
    kb = ReplyKeyboardMarkup(keyboard=start_keyboard, resize_keyboard=True, one_time_keyboard=False)
    await message.reply("", reply_markup=kb)


@dp.message(lambda message: message.text == "О магазине")
async def work_time(message: types.Message):
    kb = ReplyKeyboardMarkup(keyboard=back_keyboard, resize_keyboard=True, one_time_keyboard=False)
    await message.reply("Мы продаём всё.", reply_markup=kb)


if __name__ == '__main__':
    asyncio.run(main())  # начинаем принимать сообщения
