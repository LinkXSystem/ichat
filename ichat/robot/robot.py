from .command import Command


class Robot:
    def __init__(self):
        self.options = {}
        self.behaviors = Command()

    def register(self, options):
        self.options = self.options.update(options)

    def flow(self, message):
        text = message['Text']

        if Command.valid(':', text):
            return self.action(Command.split(':', text))

        return self.reply()

    def reply(self):
        return 'This is robot !!!'

    def action(self, command):
        if not self.behaviors.has(command):
            return self.behaviors.commands['notfound']()

        return self.behaviors.commands[command]()
