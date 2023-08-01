import pytest
import time
from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage


class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)  # добавить фикстуру сетап. внутри нее
    def setup(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"  # открыть страницу регистрации
        page = LoginPage(browser, link)
        page.open()
        email = str(time.time()) + "@fakemail.org"
        password ='password#1'
        page.register_new_user(email, password)  # зарегать нового польщователя
        page.should_be_authorized_user()  # проверить ,что пользователь залогинен

    def test_user_cant_see_success_message(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
        page = ProductPage(browser, link)
        page.open()
        page.click_add_to_card()
        # page.solve_quiz_and_get_code()
        page.product_name_is_correct()
        page.product_price_is_correct()


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.click_add_to_card()
    page.should_not_be_success_message()

def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()

@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser):
     link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
     page = ProductPage(browser, link)
     page.open()
     page.click_add_to_card()
     page.product_name_is_correct()
     page.product_price_is_correct()

@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.click_add_to_card()
    page.should_be_disappearing_message()

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()

@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    # Гость открывает страницу товара
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    # Переходит в корзину по кнопке в шапке сайта
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    # Ожидаем, что в корзине нет товаров
    basket_page.should_not_be_items()
    # Ожидаем, что есть текст о том что корзина пуста
    basket_page.should_be_text_in_empty_basket()

@pytest.mark.xfail
def test_guest_can_see_product_in_basket_opened_from_product_page(browser):
    # Гость открывает страницу товара
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    # Переходит в корзину по кнопке в шапке сайта
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    # Ожидаем, что в корзине есть товары
    basket_page.should_be_items()

