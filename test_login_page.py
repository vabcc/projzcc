from .pages.login_page import LoginPage
import time

def test_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_form()
    page.should_be_login_url()
    page.should_be_register_form()
    time.sleep(10)
