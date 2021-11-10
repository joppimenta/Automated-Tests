Feature: High Contrast mode

  Scenario: Turn On High Contrast mode (1b)
    Given the user is in the platform login page
    When the user logins on the DAL platform, goes to the home page and click on the High Contrast mode button
    Then the high contrast mode is activated

  Scenario: Turn Off High Contrast mode (2b)
    Given the user is on the platform login page and the high contrast mode is activated
    When the user logins on the DAL platform, goes to the home page and click on the High Contrast mode button 2
    Then the High Contrast mode is disabled
