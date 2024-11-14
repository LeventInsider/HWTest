from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class CategoryPage(BasePage):
    PROCUCT_IMAGE = (By.CLASS_NAME, 'product-image__image')
    QUICKFILTER_NEW = (By.CLASS_NAME, 'quick-filters__item--newest')
    KAZAK_BREADCRUMB = (By.CLASS_NAME, 'breadcrumb-item')
    product_index = '4'
    sub_category = 'Kazak'

    def get_breadcrumb_text(self, index):
        return self.get_nth_element(index, *self.KAZAK_BREADCRUMB).text

    def click_quick_filter(self):
        self.click_element(*self.QUICKFILTER_NEW)

    def click_product(self):
        self.wait_element(self.PROCUCT_IMAGE).click()
