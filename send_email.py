import os
import smtplib
from admin_app import db, app

from db_home.models import User

EMAIL_ADDRESS = 'lgtahir93@gmail.com'
EMAIL_PASSWORD = 'rtjrwzoznvpibsal'

def code_generation():
    import random
    from string import ascii_letters, digits
    symb = ascii_letters + digits
    secure_random = random.SystemRandom()
    code = ''.join(secure_random.choice(symb) for i in range(8))
    return code


def send_pass(email, oft):
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()

        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

        subject = 'Подтверждение сотрудника'
        body = oft

        msg = f'Subject: {subject}\n\n{body}'
        bit_msg = msg.encode('utf-8')

        smtp.sendmail(EMAIL_ADDRESS, email, bit_msg)
        return 'Отправлено'



