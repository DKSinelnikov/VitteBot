from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher import filters
from aiogram.types import (ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton)

token = "5954507210:AAFRIlnvY76SXAr72nxeyO4JTNBTrVKl5YY"
bot = Bot(token=token)
dp = Dispatcher(bot)
button1 = KeyboardButton('заказ')
keyboard = ReplyKeyboardMarkup()
keyboard.add(button1)
button2 = KeyboardButton('жалоба')
keyboard.add(button2)


bad_words = ["дурак", "идиот", 'дьявол', 'чёрт', 'хрень', 'фигня']


@dp.callback_query_handler(text='delete')
async def delete_meeting(query):
    await query.answer('Хорошо. Мы сообщим об этом другому участнику. ')
    await bot.send_message(query.from_user.id,  'Хорошо. Мы сообщим об этом другому участнику. ')


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("I glad to see you!")

for word in bad_words:
    @dp.message_handler(filters.Text(contains=word, ignore_case=True))
    async def bad_message(msg: types.Message):
        await bot.send_message(msg.from_user.id, "Не ругайтесь. ")

@dp.message_handler(commands=['hello'])
async def menu(message: types.Message):
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("yandex.ru", url='https://ya.ru'))
    markup.add(InlineKeyboardButton('отмена', callback_data='delete'))

    await message.reply('Информация о встрече. ', reply_markup=markup)






@dp.message_handler(filters.Text(contains='жалоба', ignore_case=True))
async def confort_user(msg: types.Message):
    await bot.send_message(msg.from_user.id, "На что у вас есть жалоба? Ваш ответ должен содержать, я жалуюсь на... ")





@dp.message_handler(filters.Text(contains='я жалуюсь на', ignore_case=True))
async def confort_user(msg: types.Message):
    await bot.send_message(msg.from_user.id, "Хорошо, мы поняли вас. Мы попытаемся исправить эту ошибку. Спасибо, что вы помогаете нам быть лучше! ")


@dp.message_handler(filters.Text(contains='заказ', ignore_case=True))
async def viches(msg: types.Message):
    await bot.send_message(msg.from_user.id, "Извините, сейчас мы не можем принять заказ. Попытайтесь заказать завтра. ")


@dp.message_handler()
async def kyeword(msg: types.Message):
    await bot.send_message(msg.from_user.id, 'Выберете действие', reply_markup=keyboard)


@dp.message_handler()
async def echo_message(msg: types.Message):
    await bot.send_message(msg.from_user.id, msg.text)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

# @dp.message_handler(text_contains="Дурак", ignore_case=True)
