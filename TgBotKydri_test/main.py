import asyncio
from aiogram import Bot, Dispatcher, types, executor
from dotenv import load_dotenv
import os

from TgBotKydri_test.text import textStart, textGuide, text_vebinar, textGoVebinar

load_dotenv()
bot = Bot(os.getenv('TOKEN'), parse_mode="HTML")
dp = Dispatcher(bot=bot)


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    markup = types.InlineKeyboardMarkup(resize_keyboard=True)
    markup.add(types.InlineKeyboardButton('🎁получить гайд', callback_data='guide'))
    await message.answer_photo(open(f'C:/Users/ilya_/PycharmProjects/pythonProject2/TgBotKydri_test/pictures'
                                    f'/Start_photo.jpg', 'rb'), caption=textStart, reply_markup=markup)


@dp.callback_query_handler(lambda call: call.data == "guide")
async def callback_guide_start(call):
    with open('C:/Users/ilya_/PycharmProjects/pythonProject2/TgBotKydri_test/pictures/5_ШАГОВ_К_СТАБИЛЬНОЙ_'
              'КЛИЕНТСКОЙ_БАЗЕ_НА_КУДРЯХ.pdf', 'rb') as file:
        await call.message.answer_document(file)
        await asyncio.sleep(15)
        markup = types.InlineKeyboardMarkup(resize_keyboard=True)
        markup.add(types.InlineKeyboardButton('🔍Узнать подробнее', callback_data='under_guide'))
        await call.message.answer(textGuide, reply_markup=markup)


@dp.callback_query_handler(lambda call: call.data == 'under_guide')
async def callback_vebinar(call):
    markup = types.InlineKeyboardMarkup(resize_keyboard=True)
    markup.add(types.InlineKeyboardButton('🔥Я иду!', callback_data='go_vebinar'))
    await call.message.answer_photo(open('C:/Users/ilya_/PycharmProjects/pythonProject2/TgBotKydri_test/pictures'
                                         '/веб27.09.png', 'rb'), caption=text_vebinar, reply_markup=markup)


@dp.callback_query_handler(lambda call: call.data == 'go_vebinar')
async def callback_vebinar(call):
    await call.message.answer(textGoVebinar)


if __name__ == '__main__':
    executor.start_polling(dp)
