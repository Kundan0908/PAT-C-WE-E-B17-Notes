from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.firefox.launch(headless=False)
    page = browser.new_page()
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    print(page.title())
    page.locator('[name="username"]').fill('Admin')
    page.locator('[type="password"]').fill('admin123')
    page.locator('[type="submit"]').click()
    browser.close()