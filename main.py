import asyncio
import requests
from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from dotenv import load_dotenv
import os

load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


def get_dog_image():
    url = "https://dog.ceo/api/breeds/image/random"
    response = requests.get(url)
    data = response.json()
    return data['message']


def get_random_quote():
    url = "https://zenquotes.io/api/random"
    response = requests.get(url)
    data = response.json()
    return f"\"{data[0]['q']}\" — {data[0]['a']}"


@dp.message(CommandStart())
async def start_command(message: Message):
    await message.answer("Привет! Я бот-мотиватор. Используй /dog для фото собаки или /quote для цитаты.")


@dp.message(Command("dog"))
async def send_dog(message: Message):
    dog_url = get_dog_image()
    await message.answer_photo(photo=dog_url, caption="Вот твой верный друг!")


@dp.message(Command("quote"))
async def send_quote(message: Message):
    quote_text = get_random_quote()
    await message.answer(quote_text)


async def main():
    print("Бот запущен...")
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())