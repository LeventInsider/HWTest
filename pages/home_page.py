from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class HomePage(BasePage):
    CATEGORY_ERKEK = (By.LINK_TEXT, "ERKEK")
    CATEGORY_KAZAK = (By.LINK_TEXT, "Kazak")

    def hover_category_erkek(self):
        self.hover_element(*self.CATEGORY_ERKEK)

    def click_sub_category(self):
        self.click_element(*self.CATEGORY_KAZAK)

