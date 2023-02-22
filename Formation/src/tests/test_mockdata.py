import pytest
from form import Form

# On utilise le décorateur pytest.fixture pour créer une fixture
# qui va nous permettre de mocker les données
@pytest.fixture

# On crée une fonction qui va mocker les données et qui va retourner
# un dictionnaire avec les données
def mock_data():
    return {'first_name': 'Andew', 'last_name': 'Little'}

# On crée une fonction de test qui va prendre en paramètre la fixture
# mock_data et qui va vérifier que les données sont correctes
def test_my_function(mock_data):
    assert Form.display(mock_data['first_name']) != ''
    assert Form.display(mock_data['last_name']) != ''
