Feature: simple appium test

  Scenario: Discover feed should be turn off in Chrome
    Then I click on the "Options for Discover"
    And "Turn off" the discovered feed
    And I click on the "Options for Discover"
    And the discovered feed should be "Turn on"

  Scenario: Discover feed should be turn on in Chrome
    Then "Turn on" the discovered feed
    And I click on the "Options for Discover"
    And the discovered feed should be "Turn off"
