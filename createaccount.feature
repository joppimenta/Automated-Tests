Feature: Create an account (1d)

  Scenario: Create an account using valid credentials
    Given the user is on the platform login page 5
    When the user clicks on the Create Profile button and fills in the blank fields
    Then the account is created