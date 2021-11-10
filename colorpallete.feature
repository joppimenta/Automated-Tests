Feature: Color Palette

	Scenario: Change background color (1e)

        Given the user is on the platform login page 6
        When the user logins on the DAL platform, clicks on the Color Palette button and changes the background color
		Then the background color of the platform changes to the color chosen by the user

    Scenario: Change the font color (2e)

        Given the user is on the platform login page 7
        When the user logins on the DAL platform, clicks on the Color Palette button and changes the font color
		Then the font color changes to the color chosen by the user
