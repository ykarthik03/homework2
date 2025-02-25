import sys
import pytest
from main import main, calculate_and_print, start_repl

# Test when invalid arguments are provided (branch that prints usage and exits)
def test_main_invalid_args(monkeypatch):
    monkeypatch.setattr(sys, "argv", ["main.py", "only_one_arg"])
    with pytest.raises(SystemExit) as e:
        main()
    # Optionally check that the exit code is 1
    assert e.value.code == 1

# Test single-run mode (4 arguments)
def test_main_single_run(monkeypatch, capsys):
    monkeypatch.setattr(sys, "argv", ["main.py", "5", "3", "add"])
    main()  # should print result using calculate_and_print
    output = capsys.readouterr().out.strip()
    assert output == "The result of 5 add 3 is equal to 8"
