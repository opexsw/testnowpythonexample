# Name: login.feature
# Copyright 2015, Opex Software
# Apache License, Version 2.0
# This is a behave feature file containing scenarios in GWT format

Feature: Verifying the Login and registration functionality

  Background:
    Given I am on magento login page


  Scenario: Login using valid and invalid users
    Given I follow login link in account section
    When I login with username "admin@mailinator.com" and password "adminadmin"
    Then I should be on "My Dashboard" page
    When I logout
    Then I should be on "Logout" page
    Given I am on magento login page
    And I follow login link in account section
    When I login with username "invalid@email.com" and password "fake_password"
    Then I should see invalid_credentials message for login
    Given I follow login link in account section
    When I login with username " " and password " "
    Then I should see mandatory_fields message for login


#
#  Scenario: Register a new user and verify successful registration
#    Given I follow register link in account section
#    When I click the register button
#    Then I should see mandatory_fields message for registration
#    When I follow register link in account section
#    And I register existing user
#    And I click the register button
#    Then I should see existing_user message for registration
#    When I follow register link in account section
#    And I register new user
#    And I click the register button
#    Then I should see new_user message for registration