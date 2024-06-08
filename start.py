import asyncio
import logging
import requests
from aiogram import F
from aiogram import Bot,Dispatcher, types
from aiogram.filters.command import Command
from aiogram.utils.keyboard import InlineKeyboardBuilder

# Введите токен бота
TOKEN = '0000000:jjjjfffFFF-fdfds-fds'

# Вставьте ссылку к Вашему vMix - Web Site Address
vMix_control = 'http://localhost:8088'

logging.basicConfig(level=logging.INFO)
bot = Bot(TOKEN)
dp = Dispatcher()

# Приветственное сообщение, реакция на команду /start
hey = '''
Добро пожаловать, хотим уточнить некоторые правила пользования ботом.
Нажав на кнопку камеры, подождите появления камеры в эфире
Не стоит кликать бездумно на все камеры сразу, это не приведет к хорошему результату

Для начала нажмите /go
'''


@dp.message(Command('start'))
async def startu(message: types.Message):
    await message.answer(f'Привет\n{hey}')


# Реакция на команду /go, ее можно заменить на любую другую
@dp.message(Command('go'))
async def startu(message: types.Message):
    # Кнопки для переключения
    kb = [
        [
            types.InlineKeyboardButton(text='Input 1', callback_data='Input 1'),
            types.InlineKeyboardButton(text='Input 2', callback_data='Input 2'),
            types.InlineKeyboardButton(text='Input 3', callback_data='Input 3'),
        ],
        [
            types.InlineKeyboardButton(text='Input 4', callback_data='Input 4'),
            types.InlineKeyboardButton(text='Input 5', callback_data='Input 5'),
        ],
        [
            types.InlineKeyboardButton(text='Input 6', callback_data='Input 6'),
        ],
        [
            types.InlineKeyboardButton(text='Input 7', callback_data='Input 7'),
            types.InlineKeyboardButton(text='Input 8', callback_data='Input 8'),
            types.InlineKeyboardButton(text='Input 9', callback_data='Input 9'),
            
        ],
        [
            types.InlineKeyboardButton(text='Input 10', callback_data='Input 10'),
            types.InlineKeyboardButton(text='Input 11', callback_data='Input 11'),
        ],
        [
            types.InlineKeyboardButton(text='Input 12', callback_data='Input 12'),
        ]
        ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=kb)
    # Текст который идет вместе с кнопками
    await message.answer('Еще раз напоминаем\nНе стоит кликать бездумно на все камеры сразу, это не приведет к хорошему результату\n\nДождитесь пока камера появиться в эфире', reply_markup=keyboard)
    

# Реакция на кнопки
@dp.callback_query(F.data == 'Input 1')
async def answer(callback: types.CallbackQuery):
    requests.get(f'{vMix_control}/api/?function=CutDirect&input=1') 
    # Текст всплывающего окна после нажатия кнопки
    await callback.answer('Первый источник в эфире', cache_time=5)

@dp.callback_query(F.data == 'Input 2')
async def answer(callback: types.CallbackQuery):
    requests.get(f'{vMix_control}/api/?function=CutDirect&input=2')
    await callback.answer('Второй источник в эфире', cache_time=5)

@dp.callback_query(F.data == 'Input 3')
async def answer(callback: types.CallbackQuery):
    requests.get(f'{vMix_control}/api/?function=CutDirect&input=3')
    await callback.answer('Третий источник в эфире', cache_time=5)

@dp.callback_query(F.data == 'Input 4')
async def answer(callback: types.CallbackQuery):
    requests.get(f'{vMix_control}/api/?function=CutDirect&input=4')
    await callback.answer('Четвертый источник в эфире', cache_time=5)

@dp.callback_query(F.data == 'Input 5')
async def answer(callback: types.CallbackQuery):
    requests.get(f'{vMix_control}/api/?function=CutDirect&input=5')
    await callback.answer('Пятый источник в эфире', cache_time=5)

@dp.callback_query(F.data == 'Input 6')
async def answer(callback: types.CallbackQuery):
    requests.get(f'{vMix_control}/api/?function=CutDirect&input=6')
    await callback.answer('Шестой источник в эфире', cache_time=5)

@dp.callback_query(F.data == 'Input 7')
async def answer(callback: types.CallbackQuery):
    requests.get(f'{vMix_control}/api/?function=CutDirect&input=7')
    await callback.answer('Седьмой источник в эфире', cache_time=5)

@dp.callback_query(F.data == 'Input 8')
async def answer(callback: types.CallbackQuery):
    requests.get(f'{vMix_control}/api/?function=CutDirect&input=8')
    await callback.answer('Восьмой источник в эфире', cache_time=5)

@dp.callback_query(F.data == 'Input 9')
async def answer(callback: types.CallbackQuery):
    requests.get(f'{vMix_control}/api/?function=CutDirect&input=9')
    await callback.answer('Девятый источник в эфире', cache_time=5)

@dp.callback_query(F.data == 'Input 10')
async def answer(callback: types.CallbackQuery):
    requests.get(f'{vMix_control}/api/?function=CutDirect&input=10')
    await callback.answer('Десятый источник в эфире', cache_time=5)

@dp.callback_query(F.data == 'Input 11')
async def answer(callback: types.CallbackQuery):
    requests.get(f'{vMix_control}/api/?function=CutDirect&input=11')
    await callback.answer('Одиннадцатый источник в эфире', cache_time=5)

@dp.callback_query(F.data == 'Input 12')
async def answer(callback: types.CallbackQuery):
    requests.get(f'{vMix_control}/api/?function=CutDirect&input=12')
    await callback.answer('Двенадцатый источник в эфире', cache_time=5)

# Можно дублировать кнопки и так же расширить функционал


# Старт бота
async def main():
    await dp.start_polling(bot, skip_updates=True)


if __name__ == '__main__':
    asyncio.run(main())