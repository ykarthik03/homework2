# tests/helpers.py
from commands.base_command import BaseCommand

class DummyCommand(BaseCommand):
    def name(self):
        return "dummy"

    def execute(self, *args):
        print("Dummy executed with args:", args)
