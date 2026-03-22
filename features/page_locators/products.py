from selenium.webdriver.common.by import By

class Products:
    def __init__(self,driver):
        self.driver = driver
        self.count = 1
        self.items_loc = By.CLASS_NAME,"inventory_item_name']"
        self.item_add_cart_btn_loc = By.XPATH,f"(//button[@class='btn btn_primary btn_small btn_inventory '])[{self.count}]"
        self.add_items_in_cart_loc = By.XPATH,'//a[@class="shopping_cart_link"]'
        self.menu_loc = By.XPATH,'//button[text()="Open Menu"]'
        self.items_in_cart_loc = (By.XPATH,"//span[@class='shopping_cart_badge']")

    def selecting_items(self,user_choice):
        available_items = self.driver.find_elements(*self.items_loc)
        for each_item in available_items:
            if each_item.text == user_choice:
                self.driver.find_element(*self.item_add_cart_btn_loc).click()
        self.count += 1

    def click_add_to_cart_btn(self):
        self.driver.find_element(*self.add_items_in_cart_loc).click()

    def validate_item_added_cart(self):
        try:
            items_in_cart = self.driver.find_element(*self.items_in_cart_loc).text
            return items_in_cart
        except Exception as e:
            print("No item in cart")
            self.click_add_to_cart_btn()

