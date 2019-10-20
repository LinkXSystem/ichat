import re


class CommonUtils:
    @staticmethod
    def equal(source, target):
        status = False
        if source == target:
            status = True

        return status


class IsUtils:
    @staticmethod
    def url(target):
        match = re.match(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\), ]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', target)
        return bool(match)
