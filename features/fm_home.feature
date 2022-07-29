As a finance manager,
I want to be able to view ALL employee reimbursements,
so that I can see the data of the entire company's reimbursement requests and approve/deny the requests that are pending

As a finance manager,
I want to be able to filter all past requests by all employees by status (approved, denied, pending),
so that I can more easily view them

As a finance manager,
I want to be able to approve/deny a pending reimbursement request,
so that I can proceed with transferring money to the employee if the reimbursement is approved or not if it's denied

Feature: Viewing and approving/denying employee reimbursement requests

  Scenario: view pending reimbursement requests
    Given I am logged in as a finance manager
    When I am on my home page
    Then I will be able to view all pending reimbursement requests

  Scenario: approve reimbursement requests
    Given I am logged in as a finance manager
    And I have selected pending reimbursements
    When I click 'approve reimbursements'
    Then The reimbursements will be marked as approved

  Scenario: deny reimbursement requests
    Given I am logged in as a finance manager
    And I have selected pending reimbursements
    When I click 'deny reimbursements'
    Then The reimbursements will be marked as denied

  Scenario: filter reimbursement requests to approved
    Given I am logged in as a finance manager
    And I have changed the filter status to approved
    When I click 'get reimbursements'
    Then I will see all the approved reimbursements

  Scenario: filter reimbursement requests to denied
    Given I am logged in as a finance manager
    And I have changed the filter status to denied
    When I click 'get reimbursements'
    Then I will see all the denied reimbursements

  Scenario: filter reimbursement requests to all
    Given I am logged in as a finance manager
    And I have changed the filter status to all-statuses
    When I click 'get reimbursements'
    Then I will see all the reimbursements