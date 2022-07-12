import telebot
from telebot import types
from main_menu_func import main_menu1, submain_menu1

bot = telebot.TeleBot('5556517526:AAFwJT7z7Mog4ygR2-6VOqdycy3mlH3PlRU')


@bot.message_handler(commands=['start'])
def language_choice(message):
    markup = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton(text="Українська 🇺🇦", callback_data='ukr')
    button2 = types.InlineKeyboardButton(text="English 🇬🇧", callback_data='eng')
    button3 = types.InlineKeyboardButton(text="Русский 🇷🇺", callback_data='rus')
    markup.add(button1, button2, button3)
    bot.send_message(message.chat.id, """Вітаю, {0.first_name}! Оберіть мову будь-ласка.
Hello, {0.first_name}! Please, choose the language.""".format(message.from_user), reply_markup=markup)


@bot.message_handler(commands=['back'])
def back_to_menu(message):
    return bot.register_next_step_handler(message, main_menu)


@bot.message_handler(commands=['contacts'])
def contacts(message):
    bot.send_message(message.chat.id, text='Звони по номеру 380931378795')


@bot.callback_query_handler(func=lambda c: c.data == 'ukr')
def callback_inline_ukr(call):
    # TODO: add language info to context
    main_menu(call.message)


@bot.callback_query_handler(func=lambda c: c.data == 'eng')
def callback_inline_eng(call):
    # TODO: add language info to context
    main_menu(call.message)


@bot.callback_query_handler(func=lambda c: c.data == 'rus')
def callback_inline_rus(call):
    # TODO: add language info to context
    main_menu(call.message)


def main_menu(message):
    main_menu1(message)


@bot.message_handler(content_types=['text'])
def submain_menu(message):
    submain_menu1(message)


bot.polling(none_stop=True)