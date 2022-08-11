import telebot
import random
from telebot import types
from translations.helper import get_subbutton_text_by_language

from csvlanguagetest import read_from_csv


bot = telebot.TeleBot('5556517526:AAFwJT7z7Mog4ygR2-6VOqdycy3mlH3PlRU')

RAD_LEVELS = {
    'КПП Дитятки':  [8, 12, 17, 24, 15, 21, 19, 10, 23, 14],
    "г.Чернобыль": [9, 12, 17, 11, 15, 9, 10, 19, 23, 14],
    "ЗГРЛС Дуга": [21, 15, 17, 24, 37, 52, 19, 14, 23, 45],
    "с.Копачи": [65, 12, 17, 24, 15, 21, 19, 10, 23, 14],
    "3-я очередь строительства ЧАЭС": [8, 12, 17, 24, 15, 21, 19, 10, 23, 14],
    "Чернобыльская АЭС": [224, 220, 189, 240, 197, 234, 256, 210, 238, 192],
    "Рыжий лес": [125, 127, 155, 141, 156, 112, 120, 121, 114, 118],
    "г.Припять": [101, 87, 123, 141, 96, 112, 93, 69, 114, 91]
}


def fake_rad_situation(message):

    language = (read_from_csv(message.chat.id))
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton(text=get_subbutton_text_by_language(language, "rad_lvl", "button_1"))
    btn2 = types.KeyboardButton(text=get_subbutton_text_by_language(language, "rad_lvl", "button_2"))
    btn3 = types.KeyboardButton(text=get_subbutton_text_by_language(language, "rad_lvl", "button_3"))
    btn4 = types.KeyboardButton(text=get_subbutton_text_by_language(language, "rad_lvl", "button_4"))
    btn5 = types.KeyboardButton(text=get_subbutton_text_by_language(language, "rad_lvl", "button_5"))
    btn6 = types.KeyboardButton(text=get_subbutton_text_by_language(language, "rad_lvl", "button_6"))
    btn7 = types.KeyboardButton(text=get_subbutton_text_by_language(language, "rad_lvl", "button_7"))
    btn8 = types.KeyboardButton(text=get_subbutton_text_by_language(language, "rad_lvl", "button_8"))
    btn9 = types.KeyboardButton(text=get_subbutton_text_by_language(language, "rad_lvl", "button_9"))
    markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9)
    bot.send_message(
        message.chat.id,
        text="️Данные по какой станции автоматического контроля за "
             "радиационной обстановкой вы хотите получить?☢️".format(message.from_user), reply_markup=markup,
    )


# noinspection PyArgumentList
def show_rad(message):
    from main_menu_func import main_menu1
    rad_levels_list = RAD_LEVELS[message.text]
    rad_level = random.choice(rad_levels_list)

    bot.send_message(
        message.chat.id,
        text=f"Cейчас уровень излучения на {message.text} равен {rad_level} мкЗв/ч.",
    )

    if message.text == get_subbutton_text_by_language("rad_lvl", "button_9"):
        return main_menu1(message)
