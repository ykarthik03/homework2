"""Configuration file for pytest fixtures."""

import pytest
from app.calculator import Calculator

@pytest.fixture
def calculator():
    """Fixture to provide a Calculator instance."""
    return Calculator()