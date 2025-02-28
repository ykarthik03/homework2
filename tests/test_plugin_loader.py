import pytest
import pkgutil
from plugin_loader import load_plugins

def test_load_plugins():
    plugins = load_plugins("commands")
    # Check that the expected command names are present.
    assert "add" in plugins
    assert "subtract" in plugins
    assert "multiply" in plugins
    assert "divide" in plugins

def test_load_plugins_empty(monkeypatch):
    # Monkeypatch pkgutil.iter_modules to return an empty list
    monkeypatch.setattr(pkgutil, "iter_modules", lambda paths: [])
    plugins = load_plugins("commands")
    assert not plugins
