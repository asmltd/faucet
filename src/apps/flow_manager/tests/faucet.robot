*** Settings ***
Documentation	  Flow Manager UI 
...
...               Python RobotFramework with Selenium 2 Library
...               Create By Hariharaselvam Balasubramanian
...               Email : hbalasubramanian@asmltd.com
...               Default Browser Firefox
Library           Selenium2Library
Library           Collections

*** Variables ***

${SERVER URL}	  http://localhost:5000

${BROWSER}        Firefox
${DELAY}          0


${USERNAME}	testflowmgr@faucetsdn.org
${PASSWORD}	testflowmgr



*** Test Cases ***
Login To Flow Manager
    Open Browser    ${SERVER URL}    ${BROWSER}
    Maximize Browser Window
    Title Should Be	Faucet Flow Manager | Login
    Input Text    username    ${USERNAME}
    Input Text    password    ${PASSWORD}
    Click Element     tag=button

Test Login
    Sleep   5s
    Page Should Contain    ${USERNAME}


Logout From Flow Manager
    Click Element    partial link = ${USERNAME}
    Click Element    link = Sign out
    [Teardown]    Close Browser