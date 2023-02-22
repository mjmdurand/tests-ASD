# test_authentication.feature

Feature: Formulaire
  Scenario: Affichage du nom et du prenom
    Given je suis sur la page du formulaire
    When je saisis mon nom et le prenom
    And je clique sur le bouton "Envoyer"
    Then j'affiche les informations saisies en dessous
    And j'insere les informations saisies dans la base de données
    And je vois les 10 dernières insertions en dessous dans une tableau
