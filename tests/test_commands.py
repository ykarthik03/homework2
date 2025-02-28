# tests/test_commands.py
# pylint: disable=duplicate-code
import pytest

import plugin_loader
from commands.add_command import AddCommand
from commands.divide_command import DivideCommand
from commands.menu_command import MenuCommand
from commands.multiply_command import MultiplyCommand
from commands.subtract_command import SubtractCommand
from commands.base_command import BaseCommand

from tests.helpers import DummyCommand


# Extend the tests for AddCommand with error cases
@pytest.mark.parametrize("args, expected", [
    (["2", "3"], "Result of add 2 and 3 is equal to 5"),
    (["a", "3"], "Invalid input. Please provide valid numbers. Received: ['a', '3']"),
    (["2"], "Error: 'add' requires exactly two numbers. Example: add 2 3"),
])
def test_add_command_cases(capsys, args, expected):
    cmd = AddCommand()
    cmd.execute(*args)
    captured = capsys.readouterr().out.strip()
    assert captured == expected


# Extend tests for SubtractCommand
@pytest.mark.parametrize("args, expected", [
    (["10", "3"], "Result of subtract 10 and 3 is equal to 7"),
    (["10", "b"], "Invalid input. Please provide valid numbers. Received: ['10', 'b']"),
    (["10"], "Error: 'subtract' requires exactly two numbers. Example: subtract 5 3"),
])
def test_subtract_command_cases(capsys, args, expected):
    cmd = SubtractCommand()
    cmd.execute(*args)
    captured = capsys.readouterr().out.strip()
    assert captured == expected


# Extend tests for MultiplyCommand
@pytest.mark.parametrize("args, expected", [
    (["4", "5"], "Result of multiply 4 and 5 is equal to 20"),
    (["x", "5"], "Invalid input. Please provide valid numbers. Received: ['x', '5']"),
    (["4"], "Error: 'multiply' requires exactly two numbers. Example: multiply 2 3"),
])
def test_multiply_command_cases(capsys, args, expected):
    cmd = MultiplyCommand()
    cmd.execute(*args)
    captured = capsys.readouterr().out.strip()
    assert captured == expected


# Extend tests for DivideCommand
@pytest.mark.parametrize("args, expected", [
    (["20", "4"], "Result of divide 20 and 4 is equal to 5"),
    (["20", "y"], "Invalid input. Please provide valid numbers. Received: ['20', 'y']"),
    (["10", "0"], "Error while performing division: Cannot divide by zero"),
    (["20"], "Error: 'divide' requires exactly two numbers. Example: divide 10 2"),
])
def test_divide_command_cases(capsys, args, expected):
    cmd = DivideCommand()
    cmd.execute(*args)
    captured = capsys.readouterr().out.strip()
    assert captured == expected


def test_menu_command(monkeypatch, capsys):
    def fake_load_plugins(_):
        return {"add": None, "subtract": None, "multiply": None, "divide": None, "menu": None}
    monkeypatch.setattr(plugin_loader, 'load_plugins', fake_load_plugins)

    cmd = MenuCommand()
    cmd.execute()
    output = capsys.readouterr().out
    assert "Available commands:" in output
    for command in ["add", "subtract", "multiply", "divide", "menu"]:
        assert command in output


def test_dummy_command(capsys):
    cmd = DummyCommand()
    assert cmd.name() == "dummy"
    cmd.execute("test")
    output = capsys.readouterr().out.strip()
    assert "Dummy executed with args:" in output
