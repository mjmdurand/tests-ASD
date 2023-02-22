from calculatrice import Calculatrice

# Test de la classe Calculatrice
# Test simple avec la librairie pytest
class TestCalculatrice:
    
    # On crée une fonction de test qui va vérifier que la méthode addition
    def test_addition(self):
        assert Calculatrice.addition(1, 1) == 2

    # On crée une fonction de test qui va vérifier que la méthode addition avec un nombre négatif
    def test_additionzero(self):
        assert Calculatrice.addition(1, -1) == 0