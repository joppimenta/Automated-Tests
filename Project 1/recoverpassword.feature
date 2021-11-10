Feature: Recover password

    Scenario: Recover password using valid credentials (1c)
        Given the user is on the platform login page 3
        When the user clicks on the 'Forgot your password' button, puts your email/username on the username field and clicks on the 'Send Request' button
        Then a password recovery email is sent to the user

    Scenario: Recover password using invalid credentials (2c)
        Given the user is on the platform login page 4
        When the user clicks on the 'Forgot your password' button, puts an invalid email/username in the blank field and clicks on the 'Send Request' button
        Then an error message appears on the screen
