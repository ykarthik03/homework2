import pytest
from main import start_repl

# Test REPL 'exit' branch: simulate input "exit" to break out of the loop.
def test_start_repl_exit(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda prompt="": "exit")
    with pytest.raises(SystemExit):
        start_repl()

# Test REPL 'menu' branch: simulate input "menu" then "exit"
def test_start_repl_menu(monkeypatch, capsys):
    inputs = iter(["menu", "exit"])
    monkeypatch.setattr("builtins.input", lambda prompt="": next(inputs))
    with pytest.raises(SystemExit):
        start_repl()
    output = capsys.readouterr().out
    assert "Available commands:" in output

def test_repl_unknown_command(monkeypatch, capsys):
    # Simulate an unknown command followed by "exit" to break out of the loop.
    inputs = iter(["foobar", "exit"])
    monkeypatch.setattr("builtins.input", lambda prompt="": next(inputs))
    with pytest.raises(SystemExit):
        start_repl()
    output = capsys.readouterr().out
    assert "Unknown command: foobar" in output
