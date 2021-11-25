Feature: Recover password

  Scenario: The user try to recover your password using valid credentials (1a)

    Given the user is on the SGME login page
    When the user clicks on recover password button, inputs his email or phone on the blank field and clicks on the ‘Request recovery’ button
    Then a recovery email is sent to the user.

