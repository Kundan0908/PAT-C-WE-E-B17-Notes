Feature: As a QA,
  I want to test login functionality
  so that I can verify the working of the functionality ( Test Functionality)

  Scenario: Test login functionality with valid username and password (TestCase)
    Given User navigates to url
    When  User enters the username "standard_user"
    And   User enters the password "secret_sauce"
    And   I click on login button
    Then  I should be able to reach dashboard page