import json
import configparser

class method_reader:
    def __init__(self, lists, list2):
        with open("methods.json", "r",encoding='utf-8') as file:
            self.jsonn = json.load(file)
        self.lists = lists
        self.list2 = list2
    def names(self):
        for text in self.jsonn['methods']:
            self.lists.append(f"{text['name']}")
            self.list2.append(f"{text['use']}")

class config_reader:
    def __init__(self, req):
        self.config = configparser.ConfigParser()
        self.req = req
    def read(self):
        self.config.read('config.conf')
        if self.req == 'lport':
            return self.config['DEFAULT_CONFIGS']['lport']
        elif self.req == 'proxyfile':
            return self.config['DEFAULT_CONFIGS']['proxyfile']
        elif self.req == 'uafile':
            return self.config['DEFAULT_CONFIGS']['uafile']
        elif self.req == 'type':
            return self.config['DEFAULT_CONFIGS']['type']

#cf = config_reader('lport')
#print(cf.read())
