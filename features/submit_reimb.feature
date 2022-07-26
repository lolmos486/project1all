As an employee,
I want to be able to add a reimbursement request,
so that they can either be approved or denied by a finance manager

Feature: Add reimbursement

  Scenario: Submitting reimbursement appropriately
    Given I am on the submit reimbursement page
    And I have entered a number in the amount box
    And I have selected a type
    And I have uploaded a receipt
    And I have entered a description
    When I click submit
    Then My reimbursement will be submitted
    And I will be redirected back to my home page

  Scenario: Submitting reimbursement without receipt
    Given I am on the submit reimbursement page
    And I have entered a number in the amount box
    And I have selected a type
    And I have entered a description
    When I click submit
    Then I will be given a 'must upload receipt' error.
