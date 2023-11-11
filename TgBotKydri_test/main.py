from aiogram import Bot, Dispatcher, types, executor
from dotenv import load_dotenv
import os


load_dotenv()
bot = Bot(os.getenv('TOKEN'),parse_mode="HTML")
dp = Dispatcher(bot=bot)




@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    text = '<u>#мамакудрей</u>'
    text123 = f'👋Привет, коллега!\nДобро пожаловать в Кудрявый Бот!\n\nМеня зовут Мэри, и я {text}\n Здесь для тебя я приготовила много полезного о\n завивке волос и работе с кудрями\n\n▫️ Мой канал:\nМАМА КУДРЕЙ\n\n▫️ Онлайн-школа завивки:\nКОСМОКУДРИ\n\n▫️ Сайт: marykosmos.ru\n\n👇 Ниже тебя ждет гайд "5 шагов к стабильной базе   \nна кудрях" 🚀'
    start_photo = open(f'C:/Users/ilya_/PycharmProjects/pythonProject2/TgBotKydri_test/pictures/Start_photo.jpg', 'rb')
    await message.answer_photo(start_photo,caption=text123)

    #text2 = "[мамакудрей](https://t.me/mama_curls)"
    #('#мамакудрей', 'https://t.me/mama_curls')











if __name__ == '__main__':
    executor.start_polling(dp)
