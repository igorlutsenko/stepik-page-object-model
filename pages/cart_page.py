from .base_page import BasePage
from .locators import CartPageLocators


class CartPage(BasePage):
    def should_not_be_items_in_cart(self):
        assert self.is_not_element_present(*CartPageLocators.CART_ITEM), \
            "Cart item is presented, but should not be"

    def should_be_text_cart_is_empty(self):
        assert self.is_element_present(*CartPageLocators.EMPTY_CART_TEXT), "'Your basket is empty.' text is not presented on cart"
