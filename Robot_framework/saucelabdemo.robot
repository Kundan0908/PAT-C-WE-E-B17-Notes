*** Settings ***
Documentation    MySaucedemo Application Flow
Library    SeleniumLibrary

*** Variables ***
${browser}        ff
${url}            https://www.saucedemo.com/
${user_id}        standard_user
${password}       secret_sauce

*** Keywords ***
Selecting Items from Products Page Automation
    Open Browser        ${url}                                    ${browser}
    Log To Console    Login Page loaded for saucedemo website
    Set Selenium Implicit Wait        2 seconds
    Element Should Be Visible    id:user-name                     Username Field is visible
    Input Text        id:user-name                                ${user_id}
    Element Should Be Visible    name:password                    Password Field is visible
    Input Password    name:password                               ${password}
    Element Should Be Visible    xpath://input[@type="submit"]    Submit Button is visible
    Click Button      xpath://input[@type="submit"]
    Page Should Contain    Sauce Labs Backpack
    @{list_items}     Get Webelements       xpath://div[@class="inventory_item_name "]
    FOR    ${items}    IN    @{list_items}
        ${text}    Get Text    ${items}
        IF    '${text}' == 'Sauce Labs Bike Light'
            Log To Console    ${text}
            BREAK
        END
    END
    Close Browser

*** Test Cases ***
SauceDemo Login Testcase
    Open Browser      https://www.saucedemo.com/                    firefox
    Log To Console    Login Page loaded for saucedemo website
    Input Text        id:user-name                                standard_user
    Input Password    name:password                               secret_sauce
    Click Button      xpath://input[@type="submit"]
    Close Browser

*** Test Cases ***
SauceDemo Login Testcase using variables
    Open Browser        ${url}                                    ${browser}
    Log To Console    Login Page loaded for saucedemo website
    Set Selenium Implicit Wait        2 seconds
    Element Should Be Visible    id:user-name                     Username Field is visible
    Input Text        id:user-name                                ${user_id}
    Element Should Be Visible    name:password                    Password Field is visible
    Input Password    name:password                               ${password}
    Element Should Be Visible    xpath://input[@type="submit"]    Submit Button is visible
    Click Button      xpath://input[@type="submit"]
    Page Should Contain    Sauce Labs Backpack
    Close Browser

*** Test Cases ***
Adding Items to Cart
    Open Browser        ${url}                                    ${browser}
    Log To Console    Login Page loaded for saucedemo website
    Set Selenium Implicit Wait        2 seconds
    Element Should Be Visible    id:user-name                     Username Field is visible
    Input Text        id:user-name                                ${user_id}
    Element Should Be Visible    name:password                    Password Field is visible
    Input Password    name:password                               ${password}
    Element Should Be Visible    xpath://input[@type="submit"]    Submit Button is visible
    Click Button      xpath://input[@type="submit"]
    Page Should Contain    Sauce Labs Backpack
    @{list_items}     Get Webelements       xpath://div[@class="inventory_item_name "]
    FOR    ${items}    IN    @{list_items}
        ${text}    Get Text    ${items}
        IF    '${text}' == 'Sauce Labs Bike Light'
            Log To Console    ${text}
            BREAK
        END
    END
    Close Browser


*** Test Cases ***
Picking Items for cart
    Selecting Items From Products Page Automation