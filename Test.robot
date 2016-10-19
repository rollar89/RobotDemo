*** Settings ***
Library  Selenium2Library
Resource    Resource.robot
Suite Setup   Site Config

*** Variables ***
${Browser} =  ff

*** Test Cases ***
User Can Login successfully
    Login User

User Fill the User Form with valid data
    Login User
    Fill Valid Data
    Click Save button
    Logout

Navigate to DRAG AND DROP page
    Login User
    Navigate to DRAG AND DROP page
    Resort Items

*** Keywords ***
Site Config
    open browser    http://executeautomation.com/demosite/Login.html     ${Browser}
    Maximize Browser Window
    Set Selenium Implicit Wait  5





