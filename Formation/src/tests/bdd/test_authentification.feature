# test_authentication.feature

Feature: Authentification
  Scenario: Connexion réussie
    Given je suis sur la page de connexion
    When je saisis mon nom d'utilisateur et mon mot de passe
    And je clique sur le bouton "Se connecter"
    Then je suis redirigé vers la page d'accueil
    And je vois le message "Bienvenue, <nom d'utilisateur> !"
