Feature: Home page welcome message
  As a user
  I want to be welcome
  So that I know I am on the right spot
  Background:
    When Login Page: I am on the shein  login page
  @smoke
  Scenario: Check welcome message
    When Logo is displayed
    Then I should see "Shein "