class Interface:
    def markdown(self):
        raise Exception('subclasses need to overwrite the method !!!')


class Repository(Interface):
    def __init__(self, name, url, fork, time, description, json):
        self.template = '''
        Name: [{name}](url)
        fork: {fork}
        description: {description}
        updated: {time}
        '''
        self.name = name
        self.url = url
        self.fork = fork
        self.time = time
        self.description = description
        self.json = json

    def markdown(self):
        return self.template.format_map(vars(self))
