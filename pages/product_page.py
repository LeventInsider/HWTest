from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class ProductPage(BasePage):
    ADD_TO_CART_ICON = (By.ID, 'pd_add_to_cart')
    BEDEN_SECENEKLERI = (By.CSS_SELECTOR, 'a:not([class="disabledSelected"])[data-tracking-label="BedenSecenekleri"]')
    CART_COUNT = (By.CLASS_NAME, 'badge-circle')
    cart_count = '1'

    def is_add_to_cart_present(self):
        return self.find(*self.ADD_TO_CART_ICON)

    def click_beden_secenekleri(self):
        self.click_element(*self.BEDEN_SECENEKLERI)

    def click_add_to_cart_button(self):
        self.click_element(*self.ADD_TO_CART_ICON)

    def is_product_added(self):
        return self.get_text(self.CART_COUNT)

    def click_cart_icon(self):
        self.click_element(*self.CART_COUNT)
