Feature: Login

  Scenario: Valid Login (1a)
    Given a user is in the LEAD platform login page
    When the user input his valid credentials
    Then LEAD platform redirects the user to the home page



  Scenario: Invalid Login (2a)
    Given the user is in the LEAD platform login page
    When the user input invalid credentials
    Then LEAD platform reports an error on the login page

