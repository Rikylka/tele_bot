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

# Инфа о пользователе
address_user = None
number_user = None
zakaz_user = []

start_keyboard = [[KeyboardButton(text='О магазине'), KeyboardButton(text='Меню')],
                  [KeyboardButton(text='Обо мне'), KeyboardButton(text='Мой заказ')]]

back_keyboard = [[KeyboardButton(text='Назад')]]

about_me_keyboard = [[KeyboardButton(text='Изменить адрес'), KeyboardButton(text='Изменить номер')],
                     [KeyboardButton(text='Назад')]]

catalog_keyboard = [[KeyboardButton(text='Пицца'), KeyboardButton(text='Напитки')],
                    [KeyboardButton(text='Салаты')]]

catalog_pizza_keyboard = [[KeyboardButton(text='Пеперони'), KeyboardButton(text='4 сыра')],
                          [KeyboardButton(text='Ассорти')]]

catalog_drink_keyboard = [[KeyboardButton(text='Кола'), KeyboardButton(text='Фанта')],
                          [KeyboardButton(text='Липтон')]]

catalog_salat_keyboard = [[KeyboardButton(text='Цезарь'), KeyboardButton(text='Оливье')],
                          [KeyboardButton(text='Греческий')]]

YesorNo_keyboard = [[KeyboardButton(text='Добавить')], [KeyboardButton(text='Меню')],
                    [KeyboardButton(text='Назад')]]

seting_zakaz_keyboard = [[KeyboardButton(text='Заказать')], [KeyboardButton(text='Назад')]]

kb = ReplyKeyboardMarkup(keyboard=start_keyboard, resize_keyboard=True, one_time_keyboard=False)

logging.basicConfig(
format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s', level = logging.DEBUG
)

# создаем маршрутизатор
dp = Dispatcher()


async def main():
    bot = Bot(token=BOT_TOKEN)
    await dp.start_polling(bot)


@dp.message(Command('start'))
async def start(message: types.Message):
    await message.reply("Привет.", reply_markup=kb)


@dp.message(Command('help'))
async def help(message: types.Message):
    await message.reply("Я бот-магазин, что-бы запустить меня напишите /start")


# start_keyboard
@dp.message(lambda message: message.text == "О магазине")
async def info_shop(message: types.Message):
    await message.reply("Мы доставка Быстрые ноги пизды не получают", reply_markup=kb)


@dp.message(lambda message: message.text == "Меню")
async def menu(message: types.Message):
    kb = ReplyKeyboardMarkup(keyboard=catalog_keyboard, resize_keyboard=True, one_time_keyboard=False)
    await message.reply(".", reply_markup=kb)


@dp.message(lambda message: message.text == "Обо мне")
async def phone(message: types.Message):
    kb = ReplyKeyboardMarkup(keyboard=about_me_keyboard, resize_keyboard=True, one_time_keyboard=False)
    await message.reply(f"Ваш номер: {number_user} \n Адрес доставки: {address_user}", reply_markup=kb)


@dp.message(lambda message: message.text == "Мой заказ")
async def info_zakaz(message: types.Message):
    kb = ReplyKeyboardMarkup(keyboard=back_keyboard, resize_keyboard=True, one_time_keyboard=False)
    zakaz_uot = "\n".join(zakaz_user)
    await message.reply(f"Ваш заказ: {zakaz_uot}", reply_markup=kb)


# catalog_keyboard
@dp.message(lambda message: message.text == "Пицца")
async def stop(message: types.Message):
    kb = ReplyKeyboardMarkup(keyboard=catalog_pizza_keyboard, resize_keyboard=True, one_time_keyboard=False)
    await message.reply("Выберите пиццу", reply_markup=kb)


@dp.message(lambda message: message.text == "Напитки")
async def address(message: types.Message):
    kb = ReplyKeyboardMarkup(keyboard=catalog_drink_keyboard, resize_keyboard=True, one_time_keyboard=False)
    await message.reply("Выберите напиток", reply_markup=kb)


@dp.message(lambda message: message.text == "Салаты")
async def phone(message: types.Message):
    kb = ReplyKeyboardMarkup(keyboard=catalog_salat_keyboard, resize_keyboard=True, one_time_keyboard=False)
    await message.reply("Выберите Салат", reply_markup=kb)


# catalog_pizza_keyboard
@dp.message(lambda message: message.text == "Пеперони")
async def stop(message: types.Message):
    kb = ReplyKeyboardMarkup(keyboard=YesorNo_keyboard, resize_keyboard=True, one_time_keyboard=False)
    await message.reply("Пеперони \nСтоимость: \nОписание:  \nСостав:", reply_markup=kb)


@dp.message(lambda message: message.text == "4 сыра")
async def address(message: types.Message):
    kb = ReplyKeyboardMarkup(keyboard=YesorNo_keyboard, resize_keyboard=True, one_time_keyboard=False)
    await message.reply("4 сыра \nСтоимость: \nОписание:  \nСостав:", reply_markup=kb)


@dp.message(lambda message: message.text == "Ассорти")
async def phone(message: types.Message):
    kb = ReplyKeyboardMarkup(keyboard=YesorNo_keyboard, resize_keyboard=True, one_time_keyboard=False)
    await message.reply("Ассорти \nСтоимость: \nОписание:  \nСостав:", reply_markup=kb)

# catalog_drink_keyboard
@dp.message(lambda message: message.text == "Кола")
async def stop(message: types.Message):
    kb = ReplyKeyboardMarkup(keyboard=YesorNo_keyboard, resize_keyboard=True, one_time_keyboard=False)
    await message.reply("Кола-кола \nСтоимость: \nОписание:  \nСостав:", reply_markup=kb)


@dp.message(lambda message: message.text == "Фанта")
async def address(message: types.Message):
    kb = ReplyKeyboardMarkup(keyboard=YesorNo_keyboard, resize_keyboard=True, one_time_keyboard=False)
    await message.reply("Фанта \nСтоимость: \nОписание:  \nСостав:", reply_markup=kb)


@dp.message(lambda message: message.text == "Липтон")
async def phone(message: types.Message):
    kb = ReplyKeyboardMarkup(keyboard=YesorNo_keyboard, resize_keyboard=True, one_time_keyboard=False)
    await message.reply("Липтон \nСтоимость: \nОписание:  \nСостав:", reply_markup=kb)

# catalog_pizza_keyboard
@dp.message(lambda message: message.text == "Цезарь")
async def stop(message: types.Message):
    kb = ReplyKeyboardMarkup(keyboard=YesorNo_keyboard, resize_keyboard=True, one_time_keyboard=False)
    await message.reply("Цезарь \nСтоимость: \nОписание:  \nСостав:", reply_markup=kb)


@dp.message(lambda message: message.text == "Оливье")
async def address(message: types.Message):
    kb = ReplyKeyboardMarkup(keyboard=YesorNo_keyboard, resize_keyboard=True, one_time_keyboard=False)
    await message.reply("Оливье \nСтоимость: \nОписание:  \nСостав:", reply_markup=kb)


@dp.message(lambda message: message.text == "Греческий")
async def phone(message: types.Message):
    kb = ReplyKeyboardMarkup(keyboard=YesorNo_keyboard, resize_keyboard=True, one_time_keyboard=False)
    await message.reply("Греческий \nСтоимость: \nОписание:  \nСостав:", reply_markup=kb)

# Назад
@dp.message(lambda message: message.text == "Назад")
async def back_start(message: types.Message):
    kb = ReplyKeyboardMarkup(keyboard=start_keyboard, resize_keyboard=True, one_time_keyboard=False)
    await message.reply("Вы вернулись", reply_markup=kb)


if __name__ == '__main__':
    asyncio.run(main())  # начинаем принимать сообщения
