import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from dotenv import load_dotenv
import os

load_dotenv()
mail_host = os.environ.get('MAIL_HOST')
mail_password = os.environ.get('MAIL_PASSWORD')
mail_send_header = os.environ.get('MAIL_SEND_HEADER')


async def send_notification(name, surname, text):
    msg = MIMEMultipart()
    msg['From'] = mail_host
    msg['To'] = mail_host
    msg['Subject'] = f'{mail_send_header} {surname} {name}'
    message = text
    msg.attach(MIMEText(message))
    try:
        mailserver = smtplib.SMTP('smtp.yandex.ru', 587)
        mailserver.set_debuglevel(True)
        # Определяем, поддерживает ли сервер TLS
        mailserver.ehlo()
        # Защищаем соединение с помощью шифрования tls
        mailserver.starttls()
        # Повторно идентифицируем себя как зашифрованное соединение перед аутентификацией.
        mailserver.ehlo()
        mailserver.login(mail_host, mail_password)
        mailserver.sendmail(mail_host, mail_host, msg.as_string())
        mailserver.quit()
        print("Письмо успешно отправлено")
    except smtplib.SMTPException:
        print("Ошибка: Невозможно отправить сообщение")