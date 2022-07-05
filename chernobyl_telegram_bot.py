import telebot
from telebot import types

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

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton(text="Типы туров")    #
    btn2 = types.KeyboardButton(text="Наша команда")  #
    btn3 = types.KeyboardButton(text="Транспорт")  #
    btn4 = types.KeyboardButton(text="Радиацыонная обстановка")  #
    btn5 = types.KeyboardButton(text="Контакты")  #
    btn6 = types.KeyboardButton(text="Что брать с собой?")   #
    btn7 = types.KeyboardButton(text="Форма одежды")  #
    markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7)
    bot.send_message(message.chat.id, text="Главное меню:".format(message.from_user), reply_markup=markup)
    bot.register_next_step_handler(message, submain_menu)


@bot.message_handler(content_types=['text'])
def submain_menu(message):
    if message.text == "Наша команда":
        bot.send_message(message.chat.id, text="команда заебись")
    elif message.text == "Типы туров":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Na 1 day")
        btn2 = types.KeyboardButton("Na 2 days")
        btn3 = types.KeyboardButton("Privat")

        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn1, btn2, btn3, back)
        bot.send_message(message.chat.id, text="Задай мне вопрос", reply_markup=markup)

    elif message.text == "Транспорт":
        bot.send_message(message.chat.id, "заебись")

    elif message.text == "Радиацыонная обстановка":
        bot.send_message(message.chat.id, "Norma")

    elif message.text == "Контакты":
        contacts(message)

    elif message.text == "Что брать с собой?":
        bot.send_message(message.chat.id, text="Ebu")

    elif message.text == "Форма одежды":
        bot.send_message(message.chat.id, text="Ebu 2/0")

    elif message.text == "Вернуться в главное меню":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Типы туров")
        btn2 = types.KeyboardButton("Наша команда")  #
        btn3 = types.KeyboardButton("Транспорт")  #
        btn4 = types.KeyboardButton("Радиацыонная обстановка")  #
        btn5 = types.KeyboardButton("Контакты")  #
        btn6 = types.KeyboardButton("Что брать с собой?")  #
        btn7 = types.KeyboardButton("Форма одежды")  #
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7)
        bot.send_message(message.chat.id, text="Вы вернулись в главное меню", reply_markup=markup)
    else:
        bot.send_message(message.chat.id, text="На такую комманду я не запрограммировал..")

bot.polling(none_stop=True)