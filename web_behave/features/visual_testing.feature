Feature: Login and logout functionality using Visual Testing

  Scenario: The user logs in successfully
    Given the login page is open
    # Assert the full screen
    Then the full screenshot is equal to "login_form" image
    When the user logs in with username "tomsmith" and password "SuperSecretPassword!"
    Then the message "You logged into a secure area!" is shown
    # Assert the full screen
    And the full screenshot is equal to "login_secure_area" image

  Scenario: The user logs out successfully
    Given the login page is open
    When the user logs in with username "tomsmith" and password "SuperSecretPassword!"
    And the user logs out
    Then the message "You logged out of the secure area!" is shown
    # Assert the full screen
    And the full screenshot is equal to "login_logout" image

  Scenario: Trying multiple Visual Testing assertions
    Given the login page is open
    # Assert the full screen
    Then the full screenshot is equal to "login_form" image
    # Assert the full screen excluding a web element
    And the full screenshot is equal to "login_form_no_password" image excluding elements
      | type    | locator  |
      | element | password |
    # Assert the full screen excluding a web element, nonexistent excluded elements are ignored
    And the full screenshot is equal to "login_form_no_password" image excluding elements
      | type    | locator  |
      | element | password |
      | ID      | asdad    |
    # Assert only a web element
    And the "login_button" element screenshot is equal to "login_submit_button" image
    # Assert the full screen with a non-related baseline, it will generate an error in visual testing report
    And the full screenshot is equal to "login_form_old_version" image
    # Assert a web element with a different size baseline image, it will generate an error in visual testing report
    And the "login_button" element screenshot is equal to "login_submit_button_old_version" image
    When the user logs in with username "tomsmith" and password "SuperSecretPassword!"
    Then the message "You logged into a secure area!" is shown
    # Assert the full screen
    And the full screenshot is equal to "login_secure_area" image
