import pytest
from faker import Faker
from form import Form

# On import la libraire faker
# On crée une instance de la classe Faker
# Cela nous permet de générer des données aléatoires
fake = Faker()

# On test que la fonction name() retourne bien une chaîne de caractères
def test_my_function():
    # On utilise la méthode name() de l'instance fake
    first_name = fake.first_name()
    last_name = fake.last_name()
    # On utilise la fonction isinstance() pour vérifier que name est bien une chaîne de caractères
    assert Form.display(isinstance(first_name, str)) != ''
    assert Form.display(isinstance(last_name, str)) != ''
