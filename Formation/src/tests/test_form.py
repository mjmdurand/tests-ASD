from form import Form
import pytest
from pytest_bdd import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from faker import Faker

# Fixtures
@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    #driver = webdriver.Firefox()
    #driver = webdriver.Edge()
    yield driver
    driver.quit()

fake = Faker()
first_name = fake.first_name()
last_name = fake.last_name()

class TestForm:
    # On crée une fonction de test qui va mettre en erreur
    #def test_display_error(self):
    #    first_name = ''
    #    assert Form.display(first_name) != ''

    # On crée une fonction de test qui va vérifier que le prenom n'est pas vide
    def test_display_first_name(self):
        assert Form.display(first_name) != ''

    # On crée une fonction de test qui va vérifier que le nom n'est pas vide
    def test_display_last_name(self):
        assert Form.display(last_name) != ''


# Steps
@given('je suis sur la page du formulaire')
def test_navigateur(browser):
    browser.get('http://localhost:5000/')

@when('je saisis mon nom et le prenom')
def test_remplissageFormulaire(browser):
    test_navigateur(browser)
    first_name_input = browser.find_element(By.ID, 'first_name')
    last_name_input = browser.find_element(By.ID, 'last_name')
    submit_button_input = browser.find_element(By.ID, 'submit')
    first_name_input.send_keys(first_name)
    last_name_input.send_keys(last_name)
    submit_button_input.click()

@then('j\'affiche les informations saisies en dessous')
def test_display_infos(browser):
    test_remplissageFormulaire(browser)
    display_infos = browser.find_element(By.ID,'submitted_infos')
    assert display_infos.text == 'Vous avez saisi ' + first_name + ' ' + last_name
