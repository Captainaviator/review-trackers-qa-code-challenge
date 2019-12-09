Feature: Reviews
  In order for customers to have confidence in what they're buying, they have to be able to see reviews

  Scenario: Clicking on the review stars should scroll the user down to the reviews
    Given I am on a product page
     When I click reviews stars
     Then the reviews section should be scrolled into view

  Scenario: Clicking on a keyword should filter the reviews and highlight that word
    Given I am on a product page
      And I click reviews stars
     When I click on the keyword in position "1"
     Then the reviews should filter correctly by "keyword"

  Scenario: Clicking on an 'Ideal For' filter should filter the reviews
    Given I am on a product page
      And I click reviews stars
     When I select "Intermediate" from the "Ideal For" filter
     Then the reviews should filter correctly by "filter"