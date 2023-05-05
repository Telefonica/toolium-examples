Feature: Multiple drivers

  Scenario: Two users log in simultaneously
    Given the login page is open in browser1
    And the login page is open in browser2
    When the user logs in with username "tomsmith" and password "SuperSecretPassword!" in browser1
    And the user logs in with username "tomsmith" and password "SuperSecretPassword!" in browser2
    Then the message "You logged into a secure area!" is shown in browser1
    And the message "You logged into a secure area!" is shown in browser2
