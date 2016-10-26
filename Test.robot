*** Settings ***
Library  Selenium2Library
Resource    Resource.robot
#Suite Setup   Site Config
Library     Collections
Library     EATestLib.py

*** Variables ***


*** Test Cases ***
User Can Login successfully
    [Tags]      Smoke1
    Login User


User Fill the User Form with valid data
    [Tags]      Smoke2
    Login User
    Fill Valid Data
    Click Save button
    Logout

HTML POPUP
    [Tags]        Smoke3
    Login User
    Click HTML POPUP
    ${L}=   list windows
    ${H}=   get from list  ${L}     1
    select window   ${H}
    fILL Data 2

Generating JavaScript Alert
    [Tags]        Smoke4
    Login User
    Click for Generating JavaScript Alert
    confirm action
    Sleep   5
    input text into prompt  {TAB}{SPACE}{TAB}{ENTER}

Automation Tools
    [Tags]        Smoke5
    Aut login
    Fill Data
    HTML Popup
    Alert Dis


*** Keywords ***
Site Config
    open browser    http://executeautomation.com/demosite/Login.html     ${Browser}
    Maximize Browser Window
    Set Selenium Implicit Wait  5







