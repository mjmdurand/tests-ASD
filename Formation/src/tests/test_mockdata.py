import pytest

# On utilise le décorateur pytest.fixture pour créer une fixture
# qui va nous permettre de mocker les données
@pytest.fixture

# On crée une fonction qui va mocker les données et qui va retourner
# un dictionnaire avec les données
def mock_data():
    return {'name': 'John', 'age': 30}

# On crée une fonction de test qui va prendre en paramètre la fixture
# mock_data et qui va vérifier que les données sont correctes
def test_my_function(mock_data):
    assert mock_data['name'] == 'John'
    assert mock_data['age'] == 30
