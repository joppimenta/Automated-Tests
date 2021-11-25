Feature: Search a company

  Scenario: Search a company by its name (1c)

	Given the user is on the SGME login page, logins on the platform using valid credentials and goes to the ‘Companies’ section 1
	When the user inputs on the ‘Name’ field ‘Acme Miniempresa’ and clicks on the ‘Search’ button
	Then a company with the searched name appears on the companies table

  Scenario: Search a company by its key (2c)

    Given the user is on the SGME login page, logins on the platform using valid credentials and goes to the ‘Companies’ section 2
	When the user inputs on the ‘Key’ field ‘A25J9M6DG5’ and clicks on the ‘Search’ button
	Then a company with the searched key appears on the companies table

  Scenario: Search a company by its Edition (3c)

    Given the user is on the SGME login page, logins on the platform using valid credentials and goes to the ‘Companies’ section 3
	When the user inputs on the ‘Edition’ field ‘A Diego Edition’ and clicks on the ‘Search’ button
	Then a company with the searched edition appears on the companies table

  Scenario: Search a company by its Educational Institution (4c)

    Given the user is on the SGME login page, logins on the platform using valid credentials and goes to the ‘Companies’ section 4
	When the user inputs on the ‘Educational institution’ field ‘A Diego Institute’ and clicks on the ‘Search’ button
	Then a company with the searched institution appears on the companies table

  Scenario: Search a company by its Year (5c)

    Given the user is on the SGME login page, logins on the platform using valid credentials, goes to the ‘Companies’ section and clicks on the ‘More options’ button 1
	When the user inputs on the ‘Year’ field ‘2023’ and clicks on the ‘Search’ button
	Then a company with the searched year appears on the companies table

  Scenario: Search a company by its Country (6c)

    Given the user is on the SGME login page, logins on the platform using valid credentials, goes to the ‘Companies’ section and clicks on the ‘More options’ button 2
	When the user inputs on the ‘Country’ field ‘A Diego Country’ and clicks on the ‘Search’ button
	Then a company that is from the searched country appears on the companies table

  Scenario: Search a company by its State (7c)

    Given the user is on the SGME login page, logins on the platform using valid credentials, goes to the ‘Companies’ section and clicks on the ‘More options’ button 3
	When the user inputs on the ‘State’ field ‘A Diego State’ and clicks on the ‘Search’ button
	Then a company that is from the searched state appears on the companies table

  Scenario: Search a company by its City (8c)

    Given the user is on the SGME login page, logins on the platform using valid credentials, goes to the ‘Companies’ section and clicks on the ‘More options’ button 4
	When the user inputs on the ‘City’ field ‘A Diego City’ and clicks on the ‘Search’ button
	Then a company that is from the searched city appears on the companies table
