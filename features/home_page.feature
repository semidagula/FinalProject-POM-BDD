Feature: Home page welcome message
  As a user
  I want to be welcome
  So that I know I am on the right spot
  Scenario: User can see the logo on the Home page
    Given User is on the Home page
    When User looks at the logo
    When Logo should be displayed
    Then Logo text should be Shine Boutique