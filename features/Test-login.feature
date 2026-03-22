Feature: As a QA,
  I want to test login functionality
  so that I can verify the working of the functionality ( Test Functionality)

#  Scenario: Test login functionality with valid username and password
#    Given User is able to reach login url (# prerequisite step)
#    When User enters username in the username field "standard_user"
#    And  User enters password in the password field "secret_sauce"
#    And  User clicks on the login button
#    Then User should be navigated to the landing page

#  @positive @regression
#  Scenario Outline: Test login functionality with different user credentials
#    Given User is able to reach login url (# prerequisite step)
#    When User enters username in the username field "<username>"
#    And  User enters password in the password field "<password>"
#    And  User clicks on the login button
#    Then User should be navigated to the landing page
#    Examples:
#    |  username                   |    password         |
#    |  standard_user              |    secret_sauce     |
#    |  problem_user               |    secret_sauce     |

# Positive testing -> giving correct steps -> correct username, correct password (Actual) Expected -> user should login if actual == expected -> Testcase passed
# Negative testing -> giving incorrect steps -> incorrect username, incorrect password (Actual) Expected -> user should not be logged in  if actual == expected -> Testcase passed

#  @negative
#  Scenario Outline: Test login functionality with wrong users
#    Given User is able to reach login url (# prerequisite step)
#    When User enters username in the username field "<username>"
#    And  User enters password in the password field "<password>"
#    And  User clicks on the login button
#    Then User should not be navigated to the login page
#    Examples:
#    |  username                   |    password          |
#    |  standard_users              |    secret_sauce     |
#    |  problem_users               |    secret_sauce     |


#  @positive @regression
#  Scenario: Test Adding items to cart
#    Given User is able to reach login url (# prerequisite step)
#    When User enters username in the username field "standard_user"
#    And  User enters password in the password field "secret_sauce"
#    And  User clicks on the login button
#    And  User is able to pick item "Sauce Labs Bike Light" and click on add to cart button
#    Then User should be able to verify item added to cart

#  Scenario: Test login functionality with valid username and password from excel sheet
#    Given User is able to reach login url (# prerequisite step)
#    When User enters username in the username field from excel-sheet
#    And  User enters password in the password field from excel-sheet
#    And  User clicks on the login button
#    Then User should be navigated to the landing page

  Scenario: Test login functionality with valid username and password from json files
    Given User is able to reach login url (# prerequisite step)
    When User enters username in the username field from json file
    And  User enters password in the password field from json file
    And  User clicks on the login button
    Then User should be navigated to the landing page