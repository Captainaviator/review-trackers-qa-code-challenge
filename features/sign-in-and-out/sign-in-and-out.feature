Feature: Sign-in and sign-out
  In order for customers to be able to manage their accounts, they have to be able to sign in/out of the site

  Scenario: Selecting Sign In / Sign Up should take users to the sign-in page
    Given I am on the main page
     When I click the "Sign In / Sign Up link"
     Then I should be on the "Login" page

  Scenario: Users should be able to log in with a valid username and password and be able to log out
    Given I am on the login page
     When I enter "lvc.reviewtrackers@mailinator.com" in the "email" field
      And I enter "Tester123" in the "password" field
      And I click the sign in button
     Then I should be on the "My Account" page
      And the account link in the header should say "My Account"
     When I click the sign out link
     Then I should be on the "main" page
      And the account link in the header should say "Sign In / Sign Up"

  Scenario: Users should not be able to log in with an invalid username and password combo
    Given I am on the login page
     When I enter "lvc.reviewtrackers@mailinator.com" in the "email" field
      And I enter "Wrongpassword" in the "password" field
      And I click the sign in button
     Then I should see the incorrect email or password error message
      And the account link in the header should say "Sign In / Sign Up"