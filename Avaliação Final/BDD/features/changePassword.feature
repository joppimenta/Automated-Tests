Feature: Change password

  Scenario: Try to change password inputting on the ‘New password’ and ‘Confirm password’ fields the same passwords (1d)

	Given the user is on the SGME login page, logins on the platform using valid credentials and goes to the ‘Profile’ section 1
	When the user clicks on the ‘Change password’ button and inputs on the ‘New password’ and ‘Confirm password’ the password: ‘abcd1234’
	Then a message that says the password has been changed appears on the screen



  Scenario: Try to change password inputting on the ‘New password’ and ‘Confirm password’ fields different passwords (2d)

	Given the user is on the SGME login page, logins on the platform using valid credentials and goes to the ‘Profile’ section 2
	When the user clicks on the ‘Change password’ button and inputs on the ‘New password’ and ‘Confirm password’ the passwords: ‘abcd1234’ and ‘abcd1230’, respectively
	Then an error message appears on the screen
