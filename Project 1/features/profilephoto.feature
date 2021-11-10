Feature: Profile Photo

  Scenario: Add a profile photo (1f)
    Given the user is on the platform login page 8
    When the user logins on the platform, goes to the Edit Profile zone, clicks on the Change Photo button and selects a profile picture
    Then the photo chosen by the user becomes their profile photo


    Scenario: Remove a profile photo (2f)
      Given the user is on the platform login page 9
      When the user logins on the platform, goes to the Edit Profile zone and clicks on the Remove Photo button
      Then the profile photo is removed
