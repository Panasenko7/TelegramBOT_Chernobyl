import telebot
import random
from telebot import types


bot = telebot.TeleBot('5556517526:AAFwJT7z7Mog4ygR2-6VOqdycy3mlH3PlRU')

RAD_LEVELS = {
    'КПП Дитятки':  [8, 12, 17, 24, 15, 21, 19, 10, 23, 14],
    "г.Чернобыль" : [9, 12, 17, 11, 15, 9, 10, 19, 23, 14],
    "ЗГРЛС Дуга" : [21, 15, 17, 24, 37, 52, 19, 14, 23, 45],
    "с.Копачи" : [65, 12, 17, 24, 15, 21, 19, 10, 23, 14],
    "3-я очередь строительства ЧАЭС" : [8, 12, 17, 24, 15, 21, 19, 10, 23, 14],
    "Чернобыльская АЭС" : [224, 220, 189, 240, 197, 234, 256, 210, 238, 192],
    "Рыжий лес" : [125, 127, 155, 141, 156, 112, 120, 121, 114, 118],
    "г.Припять" : [101, 87, 123, 141, 96, 112, 93, 69, 114, 91]
}


def fake_rad_situation(message):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton(text="КПП Дитятки")
    btn2 = types.KeyboardButton(text="г.Чернобыль")
    btn3 = types.KeyboardButton(text="ЗГРЛС Дуга")
    btn4 = types.KeyboardButton(text="с.Копачи")
    btn5 = types.KeyboardButton(text="3-я очередь строительства ЧАЭС")
    btn6 = types.KeyboardButton(text="Чернобыльская АЭС")
    btn7 = types.KeyboardButton(text="Рыжий лес")
    btn8 = types.KeyboardButton(text="г.Припять")
    btn9 = types.KeyboardButton(text="Вернуться в главное меню")
    markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9)
    bot.send_message(
        message.chat.id,
        text="️Данные по какой станции автоматического контроля за "
             "радиационной обстановкой вы хотите получить?☢️".format(message.from_user), reply_markup=markup,
    )


def show_rad(message):
    rad_levels_list = RAD_LEVELS[message.text]
    rad_level = random.choice(rad_levels_list)

    bot.send_message(
        message.chat.id,
        text=f"Cейчас уровень излучения на {message.text} равен {rad_level} мкЗв/ч.",
    )

    if message.text == "Вернуться в главное меню":
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
