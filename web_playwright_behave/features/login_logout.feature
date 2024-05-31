Feature: Login and logout functionality

  Scenario: The user logs in successfully
    Given the login page is open
    When the user logs in with username "tomsmith" and password "SuperSecretPassword!"
    Then the message "You logged into a secure area!" is shown

  Scenario: The user logs out successfully
    Given the login page is open
    When the user logs in with username "tomsmith" and password "SuperSecretPassword!"
    And the user logs out
    Then the message "You logged out of the secure area!" is shown
