import pytest
from unittest.mock import MagicMock

# On import MagicMock de la librairie unittest.mock
# qui nous permet de mocker des fonctions

def test_my_function():
    my_function = MagicMock(return_value=10)
    my_function2 = MagicMock(return_value="Hello World")
    assert my_function() == 10
    assert my_function2() == "Hello World"
