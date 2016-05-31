Feature: Tabs

  Scenario: change tab
    Given the menu is open
     When the user goes to the tabs-by-id screen
      And the user opens the second tab
     Then the second tab contains "tab2"

