Feature: Search functionality
  In order for customers to easily find a specific pen, they must be able to search the site

  Scenario: Selecting the search field should show trending searches and products
    Given I am on the main page
     When I click the "search field"
     Then the site search drop-down should appear
      And the site search drop-down should have "trending searches"
      And the site search drop-down should have "trending products"

  Scenario: Selecting a trending search should take me to the correct search results
    Given I am on the main page
     When I click the "search field"
      And I click on item "3" in trending "searches"
     Then the search results should match what I searched for

  Scenario: Selecting a trending product should take me to the correct product page
    Given I am on the main page
     When I click the "search field"
      And I click on item "1" in trending "products"
     Then I should be on the correct product page

  Scenario: Searching by entering text should take me to the correct search results
    Given I am on the main page
     When I click the "search field"
      And I search for "rose"
     Then the search results should match what I searched for
