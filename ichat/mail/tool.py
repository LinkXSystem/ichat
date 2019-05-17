from email.mime.text import MIMEText, MIMENonMultipart


class EmailTool(object):

    @staticmethod
    def text(content):
        mail = MIMEText(content, 'plain', 'utf-8')
        return mail

    @staticmethod
    def html(content):
        mail = MIMEText(content, 'html', 'utf-8')
        return mail

    @staticmethod
    def file(content, files):
        instance = MIMENonMultipart()
        instance.attach(content)
