import telebot
from telebot import types
from asorc import fake_rad_situation, RAD_LEVELS, show_rad

bot = telebot.TeleBot('5556517526:AAFwJT7z7Mog4ygR2-6VOqdycy3mlH3PlRU')


@bot.message_handler(commands=['contacts'])
def contacts(message):
    bot.send_message(message.chat.id, text='Звони по номеру +380931378795')


def main_menu1(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton(text="Типы туров")
    btn2 = types.KeyboardButton(text="Наша команда")
    btn3 = types.KeyboardButton(text="Транспорт")
    btn4 = types.KeyboardButton(text="Радиацыонная обстановка")
    btn5 = types.KeyboardButton(text="Контакты")
    btn6 = types.KeyboardButton(text="Что брать с собой?")
    btn7 = types.KeyboardButton(text="Форма одежды")
    markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7)
    bot.send_message(message.chat.id, text="Главное меню:".format(message.from_user), reply_markup=markup)
    bot.register_next_step_handler(message, submain_menu1)


def submain_menu1(message):
    from crew_file import my_crew
    if message.text == "Наша команда":
        my_crew(message)

    elif message.text == "Типы туров":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Стандартные на 1 день")
        btn2 = types.KeyboardButton("Двухдневные туры")
        btn3 = types.KeyboardButton("Приватные туры")

        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn1, btn2, btn3, back)
        bot.send_message(message.chat.id, text="Задай мне вопрос", reply_markup=markup)

    elif message.text == "Стандартные на 1 день":
        bot.send_message(message.chat.id, text="Тут план стандартного тура")

    elif message.text == "Двухдневные туры":
        bot.send_message(message.chat.id, text="Тут план 2хдневного тура")

    elif message.text == "Приватные туры":
        bot.send_message(message.chat.id, text="Тут план и описание ПРИВАТА")

    elif message.text == "Транспорт":
        bot.send_message(message.chat.id, "заебись")

    elif message.text == "Радиацыонная обстановка":
        fake_rad_situation(message)

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

    elif message.text in RAD_LEVELS:
        show_rad(message)

    else:
        bot.send_message(message.chat.id, text="На такую комманду я не запрограммировал..")
