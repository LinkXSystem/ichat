Command = ('register', 'info', 'clean', 'update',)


class WeChat:
    @staticmethod
    def get(message):
        return message['User']

    @staticmethod
    def valid(source, target, attr):
        temp = target[attr]
        return temp in source.keys()

    @staticmethod
    def command(target):
        return target in Command
