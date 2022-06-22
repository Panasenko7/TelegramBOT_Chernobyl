import telebot
from telebot import types

from telebot_employees import add_employee
from telebot_employees import get_employees
from telebot_employees import remove_employee

bot = telebot.TeleBot('5560343365:AAFWsgh3glvdFLV5r4MUkI7sts885CHh1Cg')


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Start")
    btn2 = types.KeyboardButton("Help")
    btn3 = types.KeyboardButton("Info")
    btn4 = types.KeyboardButton("Add")
    btn5 = types.KeyboardButton("Remove")
    markup.add(btn1, btn2, btn3, btn4, btn5)

    bot.send_message(message.chat.id, text="Здравствуйте, {0.first_name}! Я помогу вам назначить сотрудников на смены."
                     .format(message.from_user), reply_markup=markup)


@bot.message_handler(commands=['info'])
def information(message):
    bot.send_message(message.chat.id, text="Общая статистика по сотрудникам :")
    bot.send_message(message.chat.id, str(get_employees()))


@bot.message_handler(commands=['add'])
def adding(message):
    bot.send_message(message.chat.id, text="Введите имя,фамилию человека которого хотите добавить")
    bot.register_next_step_handler(message, add_employee_)


@bot.message_handler(commands=['help'])
def help_(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Утренняя смена")
    btn2 = types.KeyboardButton("Дневная смена")
    btn3 = types.KeyboardButton("Вечерняя смена")

    back = types.KeyboardButton("Вернуться в главное меню")
    markup.add(btn1, btn2, btn3, back)
    bot.send_message(message.chat.id, text="Какую смену формируем?", reply_markup=markup)
    bot.register_next_step_handler(message, func)


@bot.message_handler(content_types=['text'])
def func(message):
    if message.text == "Start":
        bot.send_message(message.chat.id, text="Чего сидим? Го замутим сменки!)")

    elif message.text == "Info":
        bot.send_message(message.chat.id, text="Общая статистика по сотрудникам :")
        bot.send_message(message.chat.id, str(get_employees()))

    elif message.text == "Add":
        bot.send_message(message.chat.id, text="Введите имя,фамилию человека которого хотите добавить")
        bot.register_next_step_handler(message, add_employee_)

    elif message.text == "Remove":
        bot.send_message(message.chat.id, text="Введите имя,фамилию человека которого хотите удалить")
        bot.register_next_step_handler(message, remove_employee_)

    elif message.text == "Help":
        help_(message)

    elif message.text == "Утренняя смена":
        bot.send_message(message.chat.id, text="ХУЮтренняя смена")

    elif message.text == "Дневная смена":
        bot.send_message(message.chat.id, text="ХУЕдневная смена")

    elif message.text == "Вечерняя смена":
        bot.send_message(message.chat.id, text="ХУЕчерняя смена")

    elif message.text == "Вернуться в главное меню":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("Start")
        button2 = types.KeyboardButton("Help")
        button3 = types.KeyboardButton("Info")
        button4 = types.KeyboardButton("Add")
        button5 = types.KeyboardButton("Remove")

        markup.add(button1, button2, button3, button4, button5)
        bot.send_message(message.chat.id, text="Вы вернулись в главное меню.", reply_markup=markup)
    else:
        bot.send_message(message.chat.id, text="Позвольте предложить вам воспользоваться одной из команд в меню :"
                                               " start; info; help; add or remove")




def add_employee_(message):
    add_employee(message.text)
    bot.send_message(message.chat.id, 'Успешно добавлен')
    bot.register_next_step_handler(message, help)


def remove_employee_(message):
    if remove_employee(message.text):
        bot.send_message(message.chat.id, 'Успешно удален')
    else:
        bot.send_message(message.chat.id, 'Net takogo usera')

    bot.register_next_step_handler(message, func)


bot.enable_save_next_step_handlers(delay=1)   #  Включает сохранения пошагового обработчика
bot.load_next_step_handlers()                 #  Загрузка пошагового обработчика
bot.polling(none_stop=True)