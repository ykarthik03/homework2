import pytest
from commands.base_command import BaseCommand

class DummyCommand(BaseCommand):
    def name(self):
        return "dummy"
    def execute(self, *args):
        print("Dummy executed with args:", args)

def test_dummy_command(capsys):
    cmd = DummyCommand()
    assert cmd.name() == "dummy"
    cmd.execute("test")
    output = capsys.readouterr().out.strip()
    assert "Dummy executed with args:" in output
