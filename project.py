import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram import Router, F
from config import BOT_TOKEN
from aiogram.types import FSInputFile, ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton

form_router = Router()
dp = Dispatcher()
logger = logging.getLogger(__name__)

# глобальные переменные
address_user = None
number_user = None
zakaz_user_dict = dict()
zakaz_user_listkey = []
for_add_bluda = "None"
path_info_menu = "txt_file\menu.txt"
sum_zakaz = 0

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

YesorNo_keyboard = [[KeyboardButton(text='Добавить'), KeyboardButton(text='Меню')],
                    [KeyboardButton(text='Назад'), KeyboardButton(text='Удалить')], ]

seting_zakaz_keyboard = [[KeyboardButton(text='Заказать')], [KeyboardButton(text='Назад')]]

kb = ReplyKeyboardMarkup(keyboard=start_keyboard, resize_keyboard=True, one_time_keyboard=False)

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG
)

# создаем маршрутизатор
dp = Dispatcher()


# бот
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
    await message.reply("Мы - The great Delivery. Новая и самая лучшая доставка в вашем городе! \n", reply_markup=kb)


@dp.message(lambda message: message.text == "Меню")
async def menu(message: types.Message):
    global for_add_bluda
    kb = ReplyKeyboardMarkup(keyboard=catalog_keyboard, resize_keyboard=True, one_time_keyboard=False)
    await message.reply("Выберите категорию", reply_markup=kb)
    for_add_bluda = "None"


@dp.message(lambda message: message.text == "Обо мне")
async def phone(message: types.Message):
    kb = ReplyKeyboardMarkup(keyboard=about_me_keyboard, resize_keyboard=True, one_time_keyboard=False)
    await message.reply(f"Ваш номер: {number_user} \n Адрес доставки: {address_user}", reply_markup=kb)


@dp.message(lambda message: message.text == "Мой заказ")
async def info_zakaz(message: types.Message):
    global zakaz_user_dict
    global zakaz_user_listkey
    global sum_zakaz
    kb = ReplyKeyboardMarkup(keyboard=back_keyboard, resize_keyboard=True, one_time_keyboard=False)
    zakaz_uot = ''
    for key in zakaz_user_listkey:
        zakaz_uot += f"{key} - {zakaz_user_dict[key][0]}шт\n"
    await message.reply(f"Ваш заказ: \n{zakaz_uot} \n Итоговая сумма: {sum_zakaz}руб", reply_markup=kb)


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
    global for_add_bluda
    global path_info_menu
    with open(path_info_menu, mode="r", encoding="utf-8") as f:
        all_stroki = f.readlines()
        for_add_bluda = "Пеперони"
        for i in range(len(all_stroki)):
            if all_stroki[i].rstrip('\n') == for_add_bluda:
                price = int(all_stroki[i + 1].rstrip('\n'))
                description = all_stroki[i + 2].rstrip('\n')
                compound = all_stroki[i + 3].rstrip('\n')

    kb = ReplyKeyboardMarkup(keyboard=YesorNo_keyboard, resize_keyboard=True, one_time_keyboard=False)
    photo = FSInputFile("foto_food/pizza/peperoni.jpg")
    await message.answer_photo(photo=photo,
                               caption=f"Пеперони \nСтоимость: {price}руб\nОписание:  {description}\nСостав: {compound}",
                               reply_markup=kb)


@dp.message(lambda message: message.text == "4 сыра")
async def address(message: types.Message):
    global for_add_bluda
    global path_info_menu
    with open(path_info_menu, mode="r", encoding="utf-8") as f:
        all_stroki = f.readlines()
        for_add_bluda = "4 сыра"  # выбор блюда
        for i in range(len(all_stroki)):
            if all_stroki[i].rstrip('\n') == for_add_bluda:
                price = int(all_stroki[i + 1].rstrip('\n'))
                description = all_stroki[i + 2].rstrip('\n')
                compound = all_stroki[i + 3].rstrip('\n')

    kb = ReplyKeyboardMarkup(keyboard=YesorNo_keyboard, resize_keyboard=True, one_time_keyboard=False)
    photo = FSInputFile("foto_food/pizza/4_chees.jpg")
    await message.answer_photo(
        photo=photo,
        caption=f"4 сыра \nСтоимость: {price}руб\nОписание:  {description}\nСостав: {compound}",
        reply_markup=kb
    )


@dp.message(lambda message: message.text == "Ассорти")
async def phone(message: types.Message):
    global for_add_bluda
    global path_info_menu
    with open(path_info_menu, mode="r", encoding="utf-8") as f:
        all_stroki = f.readlines()
        for_add_bluda = "Ассорти"  # выбор блюда
        for i in range(len(all_stroki)):
            if all_stroki[i].rstrip('\n') == for_add_bluda:
                price = int(all_stroki[i + 1].rstrip('\n'))
                description = all_stroki[i + 2].rstrip('\n')
                compound = all_stroki[i + 3].rstrip('\n')

    kb = ReplyKeyboardMarkup(keyboard=YesorNo_keyboard, resize_keyboard=True, one_time_keyboard=False)
    photo = FSInputFile("foto_food/pizza/assorti.jpeg")
    await message.answer_photo(
        photo=photo,
        caption=f"Ассорти \nСтоимость: {price}руб\nОписание:  {description}\nСостав: {compound}",
        reply_markup=kb
    )


# catalog_drink_keyboard
@dp.message(lambda message: message.text == "Кола")
async def stop(message: types.Message):
    global for_add_bluda
    global path_info_menu
    with open(path_info_menu, mode="r", encoding="utf-8") as f:
        all_stroki = f.readlines()
        for_add_bluda = "Кола"  # выбор блюда
        for i in range(len(all_stroki)):
            if all_stroki[i].rstrip('\n') == for_add_bluda:
                price = int(all_stroki[i + 1].rstrip('\n'))
                description = all_stroki[i + 2].rstrip('\n')

    kb = ReplyKeyboardMarkup(keyboard=YesorNo_keyboard, resize_keyboard=True, one_time_keyboard=False)
    photo = FSInputFile("foto_food/drink/coca-cola.jpeg")
    await message.answer_photo(
        photo=photo,
        caption=f"Кока-кола \nСтоимость: {price}руб\nОписание:  {description}\n",
        reply_markup=kb
    )


@dp.message(lambda message: message.text == "Фанта")
async def address(message: types.Message):
    global for_add_bluda
    global path_info_menu
    with open(path_info_menu, mode="r", encoding="utf-8") as f:
        all_stroki = f.readlines()
        for_add_bluda = "Фанта"  # выбор блюда
        for i in range(len(all_stroki)):
            if all_stroki[i].rstrip('\n') == for_add_bluda:
                price = int(all_stroki[i + 1].rstrip('\n'))
                description = all_stroki[i + 2].rstrip('\n')

    kb = ReplyKeyboardMarkup(keyboard=YesorNo_keyboard, resize_keyboard=True, one_time_keyboard=False)
    photo = FSInputFile("foto_food/drink/fanta.jpg")
    await message.answer_photo(
        photo=photo,
        caption=f"Фанта \nСтоимость: {price}руб\nОписание:  {description}",
        reply_markup=kb
    )


@dp.message(lambda message: message.text == "Липтон")
async def phone(message: types.Message):
    global for_add_bluda
    global path_info_menu
    with open(path_info_menu, mode="r", encoding="utf-8") as f:
        all_stroki = f.readlines()
        for_add_bluda = "Липтон"  # выбор блюда
        for i in range(len(all_stroki)):
            if all_stroki[i].rstrip('\n') == for_add_bluda:
                price = int(all_stroki[i + 1].rstrip('\n'))
                description = all_stroki[i + 2].rstrip('\n')

    kb = ReplyKeyboardMarkup(keyboard=YesorNo_keyboard, resize_keyboard=True, one_time_keyboard=False)
    photo = FSInputFile("foto_food/drink/lipton.png")
    await message.answer_photo(
        photo=photo,
        caption=f"Липтон \nСтоимость: {price}руб\nОписание:  {description}",
        reply_markup=kb
    )


# catalog_pizza_keyboard
@dp.message(lambda message: message.text == "Цезарь")
async def stop(message: types.Message):
    global for_add_bluda
    global path_info_menu
    with open(path_info_menu, mode="r", encoding="utf-8") as f:
        all_stroki = f.readlines()
        for_add_bluda = "Цезарь"  # выбор блюда
        for i in range(len(all_stroki)):
            if all_stroki[i].rstrip('\n') == for_add_bluda:
                price = int(all_stroki[i + 1].rstrip('\n'))
                description = all_stroki[i + 2].rstrip('\n')
                compound = all_stroki[i + 3].rstrip('\n')

    kb = ReplyKeyboardMarkup(keyboard=YesorNo_keyboard, resize_keyboard=True, one_time_keyboard=False)
    photo = FSInputFile("foto_food/salad/Caesar.jpg")
    await message.answer_photo(
        photo=photo,
        caption=f"Цезарь \nСтоимость: {price}руб\nОписание:  {description}\nСостав: {compound}",
        reply_markup=kb
    )


@dp.message(lambda message: message.text == "Оливье")
async def address(message: types.Message):
    global for_add_bluda
    global path_info_menu
    with open(path_info_menu, mode="r", encoding="utf-8") as f:
        all_stroki = f.readlines()
        for_add_bluda = "Оливье"  # выбор
        for i in range(len(all_stroki)):
            if all_stroki[i].rstrip('\n') == for_add_bluda:
                price = int(all_stroki[i + 1].rstrip('\n'))
                description = all_stroki[i + 2].rstrip('\n')
                compound = all_stroki[i + 3].rstrip('\n')

    kb = ReplyKeyboardMarkup(keyboard=YesorNo_keyboard, resize_keyboard=True, one_time_keyboard=False)
    photo = FSInputFile("foto_food/salad/olivie.jpg")
    await message.answer_photo(
        photo=photo,
        caption=f"Оливье \nСтоимость: {price}руб\nОписание:  {description}\nСостав: {compound}",
        reply_markup=kb
    )


@dp.message(lambda message: message.text == "Греческий")
async def phone(message: types.Message):
    global for_add_bluda
    global path_info_menu
    with open(path_info_menu, mode="r", encoding="utf-8") as f:
        all_stroki = f.readlines()
        for_add_bluda = "Греческий"
        for i in range(len(all_stroki)):
            if all_stroki[i].rstrip('\n') == for_add_bluda:
                price = int(all_stroki[i + 1].rstrip('\n'))
                description = all_stroki[i + 2].rstrip('\n')
                compound = all_stroki[i + 3].rstrip('\n')

    kb = ReplyKeyboardMarkup(keyboard=YesorNo_keyboard, resize_keyboard=True, one_time_keyboard=False)
    photo = FSInputFile("foto_food/salad/grecheskie.png")
    await message.answer_photo(
        photo=photo,
        caption=f"Греческий салат \nСтоимость: {price}руб\nОписание:  {description}\nСостав: {compound}",
        reply_markup=kb
    )


# добавить в заказ
@dp.message(lambda message: message.text == 'Добавить')
async def phone(message: types.Message):
    global for_add_bluda
    global zakaz_user_dict
    global zakaz_user_listkey
    global path_info_menu
    global sum_zakaz
    kb = ReplyKeyboardMarkup(keyboard=YesorNo_keyboard, resize_keyboard=True, one_time_keyboard=False)
    if for_add_bluda == "None":
        await message.reply("Сначала выберите блюдо из меню", reply_markup=kb)
    else:
        await message.reply(f"Вы добавили {for_add_bluda}", reply_markup=kb)
        # добавление в словарь
        if for_add_bluda in zakaz_user_dict:
            n_bluda = zakaz_user_dict[for_add_bluda][0]
            zakaz_user_dict[for_add_bluda] = [n_bluda + 1]
        else:
            zakaz_user_dict[for_add_bluda] = [1]
            zakaz_user_listkey += [for_add_bluda]
        # сумма заказа
        with open(path_info_menu, mode="r", encoding="utf-8") as f:
            all_stroki = f.readlines()
            for i in range(len(all_stroki)):
                if all_stroki[i].rstrip('\n') == for_add_bluda:
                    price = int(all_stroki[i + 1].rstrip('\n'))
        sum_zakaz += price


# удалить
@dp.message(lambda message: message.text == "Удалить")
async def phone(message: types.Message):
    global for_add_bluda
    global zakaz_user_listkey
    global zakaz_user_dict
    global path_info_menu
    global sum_zakaz
    kb = ReplyKeyboardMarkup(keyboard=YesorNo_keyboard, resize_keyboard=True, one_time_keyboard=False)
    if for_add_bluda == "None":
        await message.reply("Снала выберите блюдо, которое хотите удалить из заказа", reply_markup=kb)
    elif not for_add_bluda in zakaz_user_dict:
        await message.reply("Вы даже не добавили эту позицию в заказ!", reply_markup=kb)
    else:
        if zakaz_user_dict[for_add_bluda][0] == 1:
            del zakaz_user_dict[for_add_bluda]
            zakaz_user_listkey.remove(for_add_bluda)
        else:
            n_bluda = zakaz_user_dict[for_add_bluda][0]
            zakaz_user_dict[for_add_bluda] = [n_bluda - 1]
        await message.reply("Вы удалили позицию из заказа", reply_markup=kb)
        # сумма заказа
        with open(path_info_menu, mode="r", encoding="utf-8") as f:
            all_stroki = f.readlines()
            for i in range(len(all_stroki)):
                if all_stroki[i].rstrip('\n') == for_add_bluda:
                    price = int(all_stroki[i + 1].rstrip('\n'))
        sum_zakaz -= price


# Назад
@dp.message(lambda message: message.text == "Назад")
async def back_start(message: types.Message):
    global for_add_bluda
    kb = ReplyKeyboardMarkup(keyboard=start_keyboard, resize_keyboard=True, one_time_keyboard=False)
    await message.reply("Вы вернулись", reply_markup=kb)
    for_add_bluda = "None"


if __name__ == '__main__':
    asyncio.run(main())  # начинаем принимать сообщения
