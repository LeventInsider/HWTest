from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class CartPage(BasePage):
    CART_HEADER = (By.CLASS_NAME, 'cart-header')
    MAIN_LOGO = (By.CLASS_NAME, 'main-header-logo')
    cart_header = 'Sepetim'

    def is_cart_header_present(self):
        return self.get_text(self.CART_HEADER)

    def click_main_header_logo(self):
        self.click_element(*self.MAIN_LOGO)