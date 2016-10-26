*** Settings ***
Documentation    Suite description
Library  Selenium2Library

*** Variables ***
${Username} =   Rola
${Pass} =   Khalaf

*** Keywords ***
Login User
    Press Key       name=UserName    ${Username}
    Press Key       name=Password    ${Pass}
    Click button      name=Login

Fill Valid Data
    select from list    id=TitleId  Ms.
    Input Text   id=Initial     10
    Input Text   name=FirstName     rola
    Input Text  name=MiddleName  Khalaf
    select radio button     Female     value=female
    select checkbox  name=Hindi

Logout
    click element  CSS=#cssmenu > ul:nth-child(2) > li:nth-child(1) > a:nth-child(1) > span:nth-child(1)

Navigate to DRAG AND DROP page
    click element   CSS=li.last:nth-child(4) > a:nth-child(1) > span:nth-child(1)

Resort Items
    drag and drop by offset  item1     0     100

Click Save button
    click button    name=Save

Click HTML POPUP
     click link  CSS=div.detail_box:nth-child(3) > p:nth-child(2) > a:nth-child(2)

fILL Data 2
    select from list    id=TitleId  Ms.
    Input Text   id=Initial     10
    Input Text   name=FirstName     rola
    Input Text  name=MiddleName  Khalaf
     Input Text        id=LastName     Shannaq
    select radio button     Female     value=female
    select from list    id=Country  USA

Click for Generating JavaScript Alert
     click button   name=generate

Tools
    click button    id=Automation Tools