import time

from pages.cart_page import CartPage
from pages.category_page import CategoryPage
from pages.home_page import HomePage
from pages.product_page import ProductPage
from tests.base_test import BaseTest


class TestCheckLcwAddToCart(BaseTest):
    def test_check_lcw_add_to_cart(self):
        home_page = HomePage(self.driver)
        self.assertEqual(self.base_url, home_page.get_current_url(), "Lcw Anasayfa Açılmadı")
        home_page.hover_category_erkek()
        home_page.click_sub_category()

        category_page = CategoryPage(self.driver)
        self.assertIn(category_page.sub_category, category_page.get_breadcrumb_text(3),
                      "Kazak Kategorisinde Değilsin")
        category_page.click_quick_filter()
        time.sleep(1)
        category_page.click_product()

        product_page = ProductPage(self.driver)
        self.assertTrue(product_page.is_add_to_cart_present(), "Product sayfasında degilsin")
        product_page.click_beden_secenekleri()
        product_page.click_add_to_cart_button()
        self.assertEqual(product_page.cart_count, product_page.is_product_added(),
                         "Sepete urun eksik ya da eklenemedi")
        product_page.click_cart_icon()

        cart_page = CartPage(self.driver)
        self.assertIn(cart_page.cart_header, cart_page.is_cart_header_present(), "Card sayfasinda degilsin")
        cart_page.click_main_header_logo()
