Feature: Register user
    Scenario: Should be able to successfully register on website
    	Given I go to the registration form
    	When I fill in field "username" with "<username>"
    	And I fill in field "password" with "<password>"
    	And I fill in field "name" with "name1"
    	And I fill in field "email" with "user1@mailinator.com"
    	And I fill in field "place" with "Barcelona"
    	And I submit the registration form
    	Then I should see "The user has been registered"

    Examples:
    | username | password |
    | user1    | pass1    |
    | user2    | pass2    |
