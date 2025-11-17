*** Settings ***
Resource  resource.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser
Test Setup      Reset Application Create User And Go To Register Page

*** Test Cases ***

Register With Valid Username And Password
    Set Username  newuser
    Set Password  validpass123
    Set Password Confirmation  validpass123
    Submit Credentials
    Registration Should Succeed

Register With Too Short Username And Valid Password
    Set Username  ab
    Set Password  validpass123
    Set Password Confirmation  validpass123
    Submit Credentials
    Registration Should Fail With Message  Username must be at least 3 characters long

Register With Valid Username And Too Short Password
    Set Username  validuser
    Set Password  abc
    Set Password Confirmation  abc
    Submit Credentials
    Registration Should Fail With Message  Password must be at least 8 characters long

Register With Valid Username And Invalid Password
    Set Username  validuser
    Set Password  password
    Set Password Confirmation  password
    Submit Credentials
    Registration Should Fail With Message  Password must contain letters and numbers

Register With Nonmatching Password And Password Confirmation
    Set Username  validuser
    Set Password  validpass123
    Set Password Confirmation  differentpass123
    Submit Credentials
    Registration Should Fail With Message  Password and password confirmation do not match

Register With Username That Is Already In Use
    Set Username  kalle
    Set Password  validpass123
    Set Password Confirmation  validpass123
    Submit Credentials
    Registration Should Fail With Message  User with username kalle already exists

*** Keywords ***
Registration Should Succeed
    Welcome Page Should Be Open

Registration Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Set Password Confirmation
    [Arguments]  ${password}
    Input Text  password_confirmation  ${password}

Submit Credentials
    Click Button  Register

Reset Application Create User And Go To Register Page
    Reset Application
    Create User  kalle  kalle123
    Go To Register Page