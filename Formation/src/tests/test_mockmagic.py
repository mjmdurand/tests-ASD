import pytest
from unittest.mock import MagicMock
from form import Form

# On import MagicMock de la librairie unittest.mock
# qui nous permet de mocker des fonctions

def test_my_function():
    my_function = MagicMock(return_value='Sonia')
    my_function2 = MagicMock(return_value='Techie')
    assert Form.display(my_function()) != ''
    assert Form.display(my_function2()) != ''
