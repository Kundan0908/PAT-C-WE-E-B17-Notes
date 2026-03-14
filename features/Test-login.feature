Feature: As a QA,
  I want to test login functionality
  so that I can verify the working of the functionality ( Test Functionality)

#  Scenario: Test login functionality with valid username and password
#    Given User is able to reach login url (# prerequisite step)
#    When User enters username in the username field "standard_user"
#    And  User enters password in the password field "secret_sauce"
#    And  User clicks on the login button
#    Then User should be navigated to the landing page

  @positive
  Scenario Outline: Test login functionality with different user credentials
    Given User is able to reach login url (# prerequisite step)
    When User enters username in the username field "<username>"
    And  User enters password in the password field "<password>"
    And  User clicks on the login button
    Then User should be navigated to the landing page
    Examples:
    |  username                   |    password         |
    |  standard_user              |    secret_sauce     |
    |  problem_user               |    secret_sauce     |
    |  performance_glitch_user    |    secret_sauce     |

# Positive testing -> giving correct steps -> correct username, correct password (Actual) Expected -> user should login if actual == expected -> Testcase passed
# Negative testing -> giving incorrect steps -> incorrect username, incorrect password (Actual) Expected -> user should not be logged in  if actual == expected -> Testcase passed

  @negative
  Scenario Outline: Test login functionality with wrong users
    Given User is able to reach login url (# prerequisite step)
    When User enters username in the username field "<username>"
    And  User enters password in the password field "<password>"
    And  User clicks on the login button
    Then User should not be navigated to the login page
    Examples:
    |  username                   |    password          |
    |  standard_users              |    secret_sauce     |
    |  problem_users               |    secret_sauce     |
