import telebot
import time
from telebot import types

bot = telebot.TeleBot('7169102144:AAHKV3EX8yoyrfnlcI_PIJHEhXoK8D_9_Xg')


@bot.message_handler(commands=['start'])
def start(message):
    send_message = bot.send_message(message.chat.id, 'Мое первоначальное сообщение')
    time.sleep(2)
    bot.edit_message_text(chat_id=message.chat.id, message_id=send_message.message_id, text='Мое измененное сообщение')

@bot.message_handler(commands=['photo'])
def photo(message):
    photo = open('test.gif', 'rb')
    sent_msg = bot.send_photo(message.chat.id, photo, caption='Это мое фото')

    time.sleep(2)
    bot.edit_message_caption(chat_id=message.chat.id, message_id=sent_msg.message_id, caption='Новое описание')

@bot.message_handler(commands=['animation'])
def animation(message):
    anim = open('test.gif', 'rb')
    sent_msg = bot.send_animation(message.chat.id, anim, caption='Это мое фото')

    time.sleep(2)
    bot.edit_message_caption(chat_id=message.chat.id, message_id=sent_msg.message_id, caption='Новое описание')

@bot.message_handler(commands=['button'])
def button(message):
    murkup = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton('Пepвая кнопка', callback_data='press')
    murkup.add(button1)

    sent_msg = bot.send_message(message.chat.id, 'Haжми на кнопку', reply_markup=murkup)

    new_murkup = types.InlineKeyboardMarkup()
    button2 = types.InlineKeyboardButton('Вторая кнопка', callback_data='new_press')
    new_murkup.add(button2)
    time.sleep(2)
    bot.edit_message_reply_markup(chat_id=message.chat.id, message_id=sent_msg.message_id, reply_markup=new_murkup)


bot.polling()

