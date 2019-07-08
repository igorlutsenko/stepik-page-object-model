import pytest
from pages.product_page import ProductPage
from pages.cart_page import CartPage


LINKS = ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"]
#          ,
#         "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
#         "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
#         "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
#         "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
#         "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
#         "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
#         "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
#         "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
#         "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"]

@pytest.mark.skip
@pytest.mark.parametrize('link', LINKS)
def test_guest_can_add_product_to_cart(browser, link):
    link = link
    page = ProductPage(browser, link)
    page.open()
    page.should_be_add_to_cart_link()
    page.add_product_to_cart()
    page.solve_quiz_and_get_code()
    page.check_info(link)

@pytest.mark.skip
def test_guest_cant_see_success_message_after_adding_product_to_cart(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_cart()
    page.should_not_be_success_message()

@pytest.mark.skip
def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()

@pytest.mark.skip
def test_message_disappeared_after_adding_product_to_cart(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_cart()
    page.should_not_be_success_message_is_disappeared()

@pytest.mark.skip
def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

@pytest.mark.skip
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()

def test_guest_cant_see_product_in_cart_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_cart_page()
    cart_page = CartPage(browser, browser.current_url)
    cart_page.should_not_be_items_in_cart()
    cart_page.should_be_text_cart_is_empty()
