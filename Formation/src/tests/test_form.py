from form import Form

# Test de la classe Form
# Test simple avec la librairie pytest
class TestForm:
    
    # On crée une fonction de test qui va mettre en erreur
    #def test_display_error(self):
    #    first_name = ''
    #    assert Form.display(first_name) != ''

    # On crée une fonction de test qui va vérifier que le prenom n'est pas vide
    def test_display_first_name(self):
        first_name = 'John'
        assert Form.display(first_name) != ''

    # On crée une fonction de test qui va vérifier que le nom n'est pas vide
    def test_display_last_name(self):
        last_name = 'Doe'
        assert Form.display(last_name) != ''