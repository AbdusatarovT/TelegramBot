# import logging
# import traceback
# import time

from email import message
import telebot
from telebot import types
from admin_app import app
from configuration import BOT_TOKEN
from db_home.models import User
from db_home.models import db
from send_email import send_pass
from informations import info_text

bot = telebot.TeleBot(BOT_TOKEN)

# Метод создания кода для подтврждения
def code_generation():
    import random
    from string import ascii_letters, digits
    symb = ascii_letters + digits
    secure_random = random.SystemRandom()
    code = ''.join(secure_random.choice(symb) for i in range(8))
    return code

# Метод для для БД
def db_table_val(email: str, otp: str, user_id: int):
    with app.app_context():
        user = User()
        user.email = email
        user.user_id = user_id
        user.otp = otp
        db.session.add(user)
        db.session.commit()

# метод для удоления пользователя из БД
def delete_user(id):
    with app.app_context():
        a = db.session.query(User).filter(User.user_id == id).first()
        if id == a.user_id:
            db.session.delete(a)
            db.session.commit()

def update(id):
    with app.app_context():
        a = db.session.query(User).filter(User.user_id == id).first()
        a.active = True
        if id == a.user_id:
            db.session.add(a)
            db.session.commit()
            print('Все окей')



@bot.message_handler(commands = ['switch'])
def switch(message):
    markup = types.InlineKeyboardMarkup()
    switch_button = types.InlineKeyboardButton(text='Перейти', url="https://t.me/BakaiBankStaffBot")
    markup.add(switch_button)
    bot.send_message(message.chat.id, info_text, reply_markup = markup)


# Команда для старта
@bot.message_handler(commands=["start"])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('✉️ Отправить email')
    item2 = types.KeyboardButton('📜 Информация')

    markup.add(item1, item2)
    
    bot.send_message(message.chat.id, f'Привет {message.from_user.first_name}', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def bot_message(message):
    if message.text == '✉️ Отправить email':
        msg = bot.reply_to(message, 'Введите email!')
        bot.register_next_step_handler(msg, send_email)
    elif message.text == '📜 Информация':
        bot.send_message(message.chat.id, info_text)

# Функция для отправке сообщения
def send_email(message):
    print(message.text)
    with app.app_context():
        try:
            if '@gmail.com' in message.text:
                otp = code_generation()
                print(otp)
                db_table_val(message.text, otp, message.from_user.id)
                # send_pass(message.text, otp)
                msg = bot.reply_to(message, 'Вам отправлен код на корпаративную почту Бакай Банка📧. Введите полученый код!')
                # bot.send_message(message.chat.id, 'Секундочку ☝🏻')
                bot.register_next_step_handler(msg, cod_confirm)
            else:
                msg = bot.reply_to(message, 'Введите корпаротивный emai')
                bot.register_next_step_handler(msg, send_email)
        except Exception:
            bot.send_message(message.chat.id, 'Вы уже прошли проверку!')
        


# Метод для проверки кода
def cod_confirm(message):
    with app.app_context():
        otp = db.session.query(User.otp).filter(User.user_id == message.from_user.id).first()
        print(otp['otp'])
        update(message.from_user.id)
        if message.text == otp['otp']:
            bot.reply_to(message, 'Код подтвержден!')
        else:
            group_id = -1001799419976
            msg = bot.reply_to(message, 'Код не верный! Вы удалены из групы!')
            delete_user(message.from_user.id)
            bot.register_next_step_handler(msg, bot.ban_chat_member(group_id, message.from_user.id))


def cod_confirm(message):
    with app.app_context():
        otp = db.session.query(User.otp).filter(User.user_id == message.from_user.id).first()
        print(otp['otp'])
        update(message.from_user.id)
        if message.text == otp['otp']:
            bot.reply_to(message, 'Код подтвержден!')
        else:
            group_id = -1001799419976
            msg = bot.reply_to(message, 'Код не верный! Вы удалены из групы!')
            delete_user(message.from_user.id)
            bot.register_next_step_handler(msg, bot.ban_chat_member(group_id, message.from_user.id))



            



bot.polling(non_stop=True)
