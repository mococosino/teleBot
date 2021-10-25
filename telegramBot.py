import telebot
from telebot import types
from types import LambdaType

api = telebot.TeleBot("token")

@api.message_handler(commands=['start'])
def start(message):
    keyboard = types.InlineKeyboardMarkup()
    key_start = types.InlineKeyboardButton(text='Начать', callback_data='startbot')
    key_data = types.InlineKeyboardButton(text='data', callback_data='data')
    keyboard.add(key_start)
    keyboard.add(key_data)
    api.send_message(message.from_user.id, "🖐 Добро пожаловать " + message.from_user.first_name + "! Нажмите на нужную команду из списка!", reply_markup=keyboard)

@api.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == 'startbot':
        api.send_message(call.from_user.id, 'La LA')
    elif call.data == 'data':
        api.send_message(call.from_user.id, "datata")

api.polling()
