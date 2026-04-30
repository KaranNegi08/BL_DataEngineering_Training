import pytest
from task5 import sanitize_input, InputSanitizationError

def test_one():
    text= "John Doe!."

    sanitize_input(text) 

def test_second():
    text= "!@#$%."

    with pytest.raises(InputSanitizationError, match= "Text is empty after removing special character"):
        sanitize_input(text)

def test_third():
    text= "Payment: 100$."

    sanitize_input(text) 


