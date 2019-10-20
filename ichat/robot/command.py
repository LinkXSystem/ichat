import re

from ..utils import CommonUtils


def register():
    pass


def info():
    pass


def clean():
    pass


def notfound():
    return 'This is not found in built-in commands ~~~'


class Command:
    @staticmethod
    def valid(prefix, command):
        regex = re.compile(r'^' + prefix + '')
        return regex.match(command)

    @staticmethod
    def split(perfix, command):
        return command.replace(perfix, '')

    def __init__(self):
        self.original = {
            'register': register,
            'info': info,
            'clean': clean,
            'notfound': notfound
        }
        self.commands = self.original.copy()

    def has(self, command):
        return command in self.commands

    def update(self, commands):
        self.commands = self.commands.update(commands)

    def reset(self, command):
        if command not in self.commands:
            return

        if command in self.original:
            self.commands.update({command: self.original.get(command)})
            return

        self.commands.update({
            command: lambda: ''
        })
