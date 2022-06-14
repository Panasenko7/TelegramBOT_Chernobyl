import telebot
from telebot import types

from telebot_employees import add_employee, get_employees


# types.InlineKeyboardMarkup(row_width=3)

bot = telebot.TeleBot("5560343365:AAFWsgh3glvdFLV5r4MUkI7sts885CHh1Cg")


@bot.message_handler(commands=['start'])
def start_message(message):
    wellcome_message = f'Здравствуйте, {message.from_user.first_name}! Я помогу вам назначить сотрудников на смены.'
    bot.send_message(message.chat.id, wellcome_message)


@bot.message_handler(commands=['add'])
def add_command(message):
    bot.send_message(message.chat.id, 'ведите имя, фамилию и рабочие часы сотрудника:')


@bot.message_handler(commands=['info'])
def info_message_with_total_amount_employees(message):
    pass


@bot.message_handler(commands=['remove'])
def remove_employee(message):
    pass


@bot.message_handler(commands=['help'])
def create_buttons_with_shifts(message):
    markup_inline = types.ReplyKeyboardMarkup(resize_keyboard=True)
    shift_1_button = types.InlineKeyboardButton(text='Morning', callback_data='shift_1')
    shift_2_button = types.InlineKeyboardButton(text='Day', callback_data='shift_2')
    shift_3_button = types.InlineKeyboardButton(text='Evening', callback_data='shift_3')

    show_employees_button = types.InlineKeyboardButton(text='Show employees', callback_data='shift_3')

    markup_inline.add(shift_1_button, shift_2_button, shift_3_button, show_employees_button)
    bot.send_message(message.chat.id, 'Желаете составить график?', reply_markup=markup_inline)
    bot.register_next_step_handler(message, choose_button_get_action)


def choose_button_get_action(message):
    if message.text == 'Morning':
        bot.send_message(message.chat.id, '1111111111111')
    elif message.text == 'Day':
        bot.send_message(message.chat.id, '2222222222')
    elif message.text == 'Evening':
        bot.send_message(message.chat.id, '33333333333333')
    elif message.text == 'Show employees':
        bot.send_message(message.chat.id, str(get_employees()))

    print('wfwef')
    bot.register_next_step_handler(message, choose_button_get_action)
    pass


@bot.message_handler(content_types=['text'])
def unknown_message_from_user(message):
    add_employee(message.text)
    bot.send_message(message.chat.id, 'added')
    # bot.send_message(message.chat.id, 'Позвольте предложить вам воспользоваться одной из команд в меню :'
    #                                   ' start; info; help; add or remove')


bot.polling()
