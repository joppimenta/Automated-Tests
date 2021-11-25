Feature: Add user

  Scenario: Create an user using valid credentials (1e)

    Given the user is on the SGME login page, logins on the platform using valid credentials, goes to the ‘Users’ section and clicks on the ‘Create user’ button
    When the user fills the blank fields and clicks on the ‘Save data’ button
    Then the user is created
