*** Settings ***
Resource  resource.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser
Test Setup      Reset Application Create User And Go To Login Page

*** Test Cases ***
Login With Correct Credentials
    Set Username  kalle
    Set Password  kalle123
    Click Button  Login
    Login Should Succeed

Login With Incorrect Password
    Set Username  kalle
    Set Password  kalle456
    Click Button  Login
    Login Should Fail With Message  Invalid username or password

Login With Nonexistent Username
    Go To Login Page
    Set Username  nonexistent
    Set Password  wrongpassword
    Click Button  Login
    Login Should Fail With Message  Invalid username or password

*** Keywords ***
Reset Application Create User And Go To Login Page
    Reset Application
    Create User  kalle  kalle123
    Go To Login Page
