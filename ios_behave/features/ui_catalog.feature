Feature: UiCatalog

  Scenario: User can access to the Alerts view page
    Given the UICatalog page is opened
     When navigates to the Alerts view page
     And clicks on the simple alert option
     Then the alert is displayed
