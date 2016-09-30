*** Settings ***
Documentation	  Flow Manager UI 
...
...               Python RobotFramework with Selenium 2 Library
...               Create By Hariharaselvam Balasubramanian
...               Email : hbalasubramanian@asmltd.com
Library           Selenium2Library
Library           Collections

*** Variables ***

${SERVER URL}	  http://192.168.2.35:5000

${BROWSER}        Firefox
${DELAY}          0


${USERNAME}	hariharaselvam@sdnhackfest.org
${PASSWORD}	hariharaselvam





*** Test Cases ***
Login To Flow Manager
    Open Browser    ${SERVER URL}    ${BROWSER}
    Maximize Browser Window
    Title Should Be	Faucet Flow Manager | Login
    Input Text    username    ${USERNAME}
    Input Text    password    ${PASSWORD}
    Submit Form

Test Login
    Page Should Contain    ${USERNAME}


Logout From Flow Manager
    Mouse Over    partial link = ${USERNAME}
    Click Element    link = Sign out
    [Teardown]    Close Browser


*** Keywords ***

Test List page
    [Arguments]	${mainmenu}	${submenu}	${link}	${text}
    Mouse Over    partial link = ${mainmenu}
    Click Element    link = ${submenu}
    Sleep	5s
    Page Should Contain    ${text}

    




  


       



    
