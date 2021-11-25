Feature: Acessibility Bar functions

	Scenario: Turn on High Contrast mode (1b)

	  Given the user is on the SGME login page and logins using valid credentials 1
	  When the user clicks on the Turn On High Contrast mode button
	  Then the high contrast mode is activated

	Scenario: Increase font (2b)

      Given the user is on the SGME login page and logins using valid credentials 2
	  When the user clicks on the Increase Font mode button
	  Then the font size of the texts on the page is increased

	Scenario: Decrease font (3b)

      Given the user is on the SGME login page and logins using valid credentials 3
	  When the user clicks on the Decrease Font mode button
	  Then the font size of the texts on the page is decreased

    Scenario: Restore font (4b)

      Given the user is on the SGME login page and logins using valid credentials 4
	  When the user clicks on the Restore Font mode button
	  Then the font size of the texts on the page is restored
