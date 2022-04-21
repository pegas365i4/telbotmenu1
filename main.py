import logging
from aiogram import Bot, Dispatcher, executor, types
import markups as nav
import  random

TOKEN = "5******3:A***************************4" # imput my token

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def command_start(message: types.Message):
    await bot.send_message(message.from_user.id, 'Привет {0.first_name}'.format(message.from_user), reply_markup=nav.mainMenu)

@dp.message_handler()
async def bot_message(message: types.Message):
    await bot.send_message(message.from_user.id, message.text)
    if message.text == '🎲 Рандомное число':
        await bot.send_message(message.from_user.id, 'Ваше число: ' + str(random.randint(1000, 9999)))

    elif message.text == '❤ Главное меню':
        await bot.send_message(message.from_user.id, 'Какой-то текст ❤ Главное меню', reply_markup=nav.mainMenu)

    elif message.text == '➡ Другое':
        await bot.send_message(message.from_user.id, 'Какой-то текст ➡ Другое', reply_markup=nav.otherMenu)

    elif message.text == '⚠ Информация':
        await bot.send_message(message.from_user.id, 'Какая-то информация')

    elif message.text == '💹 Курсы валют':
        await bot.send_message(message.from_user.id, 'Курсы валют на сегодня')

    else:
        await message.reply('Неизвестная команда')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)