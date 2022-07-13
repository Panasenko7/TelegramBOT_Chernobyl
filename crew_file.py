import telebot
from telebot import types

bot = telebot.TeleBot('5556517526:AAFwJT7z7Mog4ygR2-6VOqdycy3mlH3PlRU')


def my_crew(message):
    markup = types.InlineKeyboardMarkup(row_width=4)
    button1 = types.InlineKeyboardButton(text="1", callback_data='1')
    button2 = types.InlineKeyboardButton(text="2", callback_data='2')
    button3 = types.InlineKeyboardButton(text="3", callback_data='3')
    button4 = types.InlineKeyboardButton(text="4", callback_data='4')
    markup.add(button1, button2, button3, button4)
    photo = open("./images/111.jpg", 'rb')
    bot.send_photo(message.chat.id, photo=photo, caption='Name!')
    bot.send_message(message.chat.id, """инфа про человека""".format(message.from_user), reply_markup=markup)


