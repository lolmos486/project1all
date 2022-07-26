As an employee,
I want to be able to view all of my reimbursements,
so that I can see the data of all of my reimbursement requests and the status of them (pending, approved, denied)

As an employee,
I want to be able to filter my past requests by status (approved, denied, pending),
so that I can more easily view them

Feature: viewing own reimbursement requests

  Scenario: viewing own reimbursement requests
    Given That I am logged in as an employee
    When I am on my homepage
    Then I will be able to see all my past reimbursement reqeusts

  Scenario: filter reimbursement requests to approved
    Given I am logged in as an employee
    And I have changed the filter status to approved
    When I click 'get reimbursements'
    Then I will see all my approved reimbursements

  Scenario: filter reimbursement requests to denied
    Given I am logged in as an employee
    And I have changed the filter status to denied
    When I click 'get reimbursements'
    Then I will see all my denied reimbursements

  Scenario: filter reimbursement requests to all
    Given I am logged in as an employee
    And I have changed the filter status to all-statuses
    When I click 'get reimbursements'
    Then I will see all my reimbursements