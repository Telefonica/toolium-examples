Feature: OpenShop.io catalog

  Scenario: view just arrived collections
    Given OpenShop.io app is open
    When the user goes to the shop
    Then just arrived collections are shown
