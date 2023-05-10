Feature: Check the functionality of the login page
  As a user
  I want to be able to make an account
  So that I can enter my details




  @T1 @validLogin @smoke
  Scenario:  Check that you can login into the application when providing correct credentials
    Given the user is on the login page
    When  the user enters their email "sem.gula@gmail.com"
    When the user enters their password "1234Supersecret!"
    When  the user clicks the login button
    Then  the user should see an success message: PERSONAL CENTER MENU

  @T2 @invalidpassword @smoke
  Scenario Outline:  Check that you can login into the application when providing invalid credentials
    Given the user is on the login page
    When  the user enters their email "<email>"
    When the user enters their password "<password>"
    When  the user clicks the login button
    Then  the user should see an error message: "<error>"
    Examples:
      | email              | password | error                                                               |
      | sem.gula@gmail.com | 1234d    | "Please enter more characters or clean leading or trailing spaces." |
      | email              | password | error                                                               |







