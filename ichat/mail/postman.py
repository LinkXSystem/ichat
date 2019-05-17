from functools import wraps
import smtplib
from email.mime.text import MIMEText
import logging


def singleton(cls):
    instances = {}

    @wraps(cls)
    def getinstance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return getinstance


@singleton
class Postman(object):

    def __init__(self, host, port, username, password):
        self._instance = None
        self._status = False
        self._host = host
        self._port = port
        self._username = username
        self._password = password
        self._initial()

    def debug(self, status):
        self._status = status

    def _initial(self):
        try:
            self._instance = smtplib.SMTP()
            self._instance.connect(self._host, self._port)
            self._instance.login(self._username, self._password)
        except smtplib.SMTPException as error:
            self._instance = None
            logging.log(logging.WARNING, error)

    def email(self, sender, subject, content, receivers):
        try:
            if self._instance is None:
                self._initial()
            mail = MIMEText(content, 'plain', 'utf-8')
            mail['Subject'] = subject
            mail['From'] = sender
            # mail['To'] = receivers[0]
            self._instance.set_debuglevel(1 if self._status else 0)
            self._instance.sendmail(sender, receivers, mail.as_string())
            return None
        except smtplib.SMTPException as error:
            return error

    def __del__(self):
        if not (self._instance is None):
            self._instance.quit()
