import telebot
from telebot import types

bot = telebot.TeleBot('5556517526:AAFwJT7z7Mog4ygR2-6VOqdycy3mlH3PlRU')


def my_transport(message):
    markup = types.InlineKeyboardMarkup(row_width=4)
    button1 = types.InlineKeyboardButton(text="1", callback_data='5')
    button2 = types.InlineKeyboardButton(text="2", callback_data='6')
    button3 = types.InlineKeyboardButton(text="3", callback_data='7')

    markup.add(button1, button2, button3)
    photo = open("./images/images999.jpg", 'rb')
    bot.send_photo(message.chat.id, photo=photo, caption='марка и модель')
    bot.send_message(message.chat.id, """Краткое описание""".format(message.from_user), reply_markup=markup)
