# test_authentication.py

import pytest
from pytest_bdd import given, when, then
from selenium import webdriver

# Fixtures
@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

# Steps
@given('je suis sur la page de connexion')
def test_navigateur(browser):
    browser.get('https://example.com/login')

@when('je saisis mon nom d\'utilisateur et mon mot de passe')
def test_remplissageCredential(browser):
    identifiant = browser.find_element_by_id('identifiant')
    password = browser.find_element_by_id('password')
    submit_button = browser.find_element_by_id('submit')
    identifiant.send_keys('mon_nom_utilisateur')
    password.send_keys('mon_mot_de_passe')
    submit_button.click()

@then('je suis redirigé vers la page d\'accueil')
def test_redirectionAccueil(browser):
    assert browser.current_url == 'https://example.com/home'

@then('je vois le message "Bienvenue, <nom d\'utilisateur> !"')
def test_messageBienvenue(browser):
    message_bienvenue = browser.find_element_by_id('welcome-message')
    assert message_bienvenue.text == 'Bienvenue, mon_nom_utilisateur !'
