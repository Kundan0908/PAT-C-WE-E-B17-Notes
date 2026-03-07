# Various locators in playwright
# 1. Role- based locators -> get_by_role() -> roles like checkbox, radio buttons, buttons. ['button='']
# 2. label-placeholder locators -> get_by_label or get_by_placeholder -> attributes with label or placeholder attribute.
# 3. Text and title -> get_by_text, get_by_title -> finds element based on text and title attribute values.
# 4. Test_id_locators -> dynamic page loading, where data-testid attribute is present, this can be used.
# 5. Alt-text_locators -> for image attributes.
# 6. page.locators -> for xpath creations in  -> page.locators('//xpath')

from playwright.sync_api import sync_playwright, expect

with sync_playwright() as p:
    browser = p.firefox.launch(headless=False)
    page = browser.new_page()
    page.goto("https://www.saucedemo.com/")
    page.get_by_placeholder('Username').fill('standard_user')
    page.locator('#password').fill('secret_sauce') # id is represented with #
    page.locator('#login-button').click() # class-name are represented with '.'
    expect(page).to_have_title('Swag Labs')
    print("Login page loaded successfully")
    items = page.locator('.inventory_item_name').all_inner_texts()
    print(items)
    count = 0
    for each_item in items:
        if each_item == 'Sauce Labs Bike Light':
            count += 1
            page.locator(f"(//button[@class='btn btn_primary btn_small btn_inventory '])[{count}]").click()
            break
        count += 1
    expect(page.get_by_text('Remove')).to_contain_text('Remove') # Fix the remove verification with some good logic
    print("Item Sauce Labs Bike Light has been added to cart") # play with different locators available in playwright
    page.locator('.shopping_cart_badge').click() # Add verification step after every action performed
    page.locator('#checkout').click()
    page.get_by_placeholder('First Name').fill('Automation')
    page.get_by_placeholder('Last Name').fill('Testing')
    page.get_by_placeholder('Zip/Postal Code').fill('12344')
    page.locator('#continue').click()
    page.get_by_role(role='button',name="finish").click()



