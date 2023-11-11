import asyncio
from aiogram import Bot, Dispatcher, types, executor
from dotenv import load_dotenv
import os

load_dotenv()
bot = Bot(os.getenv('TOKEN'), parse_mode="HTML")
dp = Dispatcher(bot=bot)


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    text_hyper_start1 = '<a href="https://t.me/mama_curls">#мамакудрей</a>'
    text_hyper_start2 = '<a href="https://t.me/mama_curls">МАМА КУДРЕЙ</a>'
    text_hyper_start3 = '<a href="https://t.me/kosmo_kudri">КОСМОКУДРИ</a>'
    textStart = f'👋Привет, коллега!\nДобро пожаловать в Кудрявый Бот!\n\nМеня зовут Мэри, и я {text_hyper_start1}\n Здесь для тебя я приготовила много полезного о\n завивке волос и работе с кудрями\n\n▫️ Мой канал:\n{text_hyper_start2}\n\n▫️ Онлайн-школа завивки:\n{text_hyper_start3}\n\n▫️ Сайт: marykosmos.ru\n\n👇 Ниже тебя ждет гайд "5 шагов к стабильной базе   \nна кудрях" 🚀'
    start_photo = open(f'C:/Users/ilya_/PycharmProjects/pythonProject2/TgBotKydri_test/pictures/Start_photo.jpg', 'rb')
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('🎁получить гайд', callback_data='guide'))
    await message.answer_photo(start_photo, caption=textStart, reply_markup=markup)


@dp.callback_query_handler(lambda call: call.data == "guide")
async def callback_guide_start(call):
    with open(
            'C:/Users/ilya_/PycharmProjects/pythonProject2/TgBotKydri_test/pictures/5_ШАГОВ_К_СТАБИЛЬНОЙ_КЛИЕНТСКОЙ_БАЗЕ_НА_КУДРЯХ.pdf',
            'rb') as file:
        await call.message.answer_document(file)
        await asyncio.sleep(15)
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton('🔍Узнать подробнее', callback_data='under_guide'))
        await call.message.answer(
            '👍Отлично! В Гайде описаны основные шаги, которые помогут любому мастеру по волосам работать с клиентской базой и увеличивать ее.\n\n🎁Для своих коллег помимо гайда я приготовила кое-что еще, а именно - открытый вебинар!\n\n🔥На нем я расскажу на примере моей команды и учеников как именно знания о завивке волос и о том, как работать с кудрявыми волосами привели всех нас к стабильному доходу и постоянно пополняющейся базе за счет рекомендаций.',
            reply_markup=markup)


#
@dp.callback_query_handler(lambda call: call.data == 'under_guide')
async def callback_vebinar(call):
    photo_vebinar = open('C:/Users/ilya_/PycharmProjects/pythonProject2/TgBotKydri_test/pictures/веб27.09.png', 'rb')
    text_vebinar = 'КАК ПАРИКМАХЕРУ СОБРАТЬ БОЛЬШУЮ БАЗУ КЛИЕНТОВ И ПОВЫСИТЬ СВОЙ ДОХОД В НЕСКОЛЬКО РАЗ?\n\n какой то текст\n\n и еще текст какой-нибудь)'
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('🔥Я иду!', callback_data='go_vebinar'))
    await call.message.answer_photo(photo_vebinar, caption=text_vebinar, reply_markup=markup)


if __name__ == '__main__':
    executor.start_polling(dp)
