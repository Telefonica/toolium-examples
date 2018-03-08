# -*- coding: utf-8 -*-
# Execution:  behave features/dyn_environment_test.feature -s -k --no-capture

Feature: Tests with the dynamic environment
  As a behave operator using multiples scenarios
  I want to append actions before the feature, before each scenario, after each scenario and after the feature.

  Actions Before the Feature:
    Given wait 3 seconds
    And wait 3 seconds
    And wait 3 seconds
    And step with a table
      | parameter     | value       |
      | sub_fields_1  | sub_value 1 |
      | sub_fields_2  | sub_value 2 |

  Actions Before each Scenario:
    Given the user navigates to the "www.google.es" url
    When the user logs in with username and password
    And wait 1 seconds
    And wait 1 seconds

  Actions After each Scenario:
    And wait 2 seconds
    And wait 2 seconds

  Actions After the Feature:
    And wait 4 seconds
    And step with another step executed dynamically
    And wait 4 seconds

  @test
  Scenario Outline: Login using valid credentials
    Then the welcome message is displayed
    Examples:
      | case |
      | 1    |
      | 2    |
      | 3    |

  @test_table
  Scenario: Login using valid credentials
    Then the welcome message is displayed
    And step with another step using table executed dynamically
    And step with a table
      | parameter | value   |
      | fields_1  | value 1 |
      | fields_2  | value 2 |
      | fields_3  | value 3 |

  @test_dyn
  Scenario: Login using valid credentials
    Then the welcome message is displayed
    And step with another step executed dynamically
