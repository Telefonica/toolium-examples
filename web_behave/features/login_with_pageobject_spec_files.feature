Feature: Login

  Scenario: successful login
    Given SpecFilesExample: the home page is open
     When SpecFilesExample: the user logs in with username "tomsmith" and password "SuperSecretPassword!"
     Then SpecFilesExample: the message "You logged into a secure area!" is shown

  Scenario: successful logout
    Given SpecFilesExample: the home page is open
     When SpecFilesExample: the user logs in with username "tomsmith" and password "SuperSecretPassword!"
      And SpecFilesExample: the user logs out
     Then SpecFilesExample: the message "You logged out of the secure area!" is shown
