Feature: Check the functionality of the login page
  As a user
  I want to be able to make an account
  So that I can enter my details

  Background:
    Given Login Page: I am on the shein  login page


  @T1 @validLogin @smoke
  Scenario:  Check that you can login into the application when providing correct credentials
    Given Go to Login page
    When  I insert email "sem.gula@gmail.com"
    And I insert  password "1234Supersecret!"
    And  I click submit
    Then  I am logged into the application and I should see PERSONAL CENTER MENU







"""