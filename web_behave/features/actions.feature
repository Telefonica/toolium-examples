Feature: Selenium Actions

  Scenario: Mouse over an element
    Given the hovers page is open
    When the user moves mouse over the second image
    Then the second image text shows "name: user2"

  Scenario: User opens and closes a tab using keyboard shortcuts
    Given the login page is open
    When the user opens a new tab
    And the user closes the tab
    Then the username field is visible
