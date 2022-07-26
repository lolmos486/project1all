Feature: Logging in
  As a user
  I want to log into my account
  So I can access the reinbursements framework

  Acceptance criteria:


  Scenario: logging in with valid username and valid password
    Given I am on the login page
    When I input a valid username
    And I input a valid password
    And I click the login button
    Then I will be redirected to my homepage

  Scenario: logging in with valid username and invalid password
    Given I am on the login page
    When I input a valid username
    And I input an invalid password
    And I click the login button
    Then I will be given an "invalid password" error


  Scenario: logging in with an invalid username and valid password
    Given I am on the login page
    When I input an invalid username
    And I input a valid password
    And I click the login button
    Then I will be given a "username not found" error


  Scenario: logging in with valid username and valid password
    Given I am on the login page
    When I input an invalid username
    And I input an invalid password
    And I click the login button
    Then I will be given a "username not found" error

