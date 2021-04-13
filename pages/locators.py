from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, 'a[class="btn btn-default"]')
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    BASKET_LINK = (By.CSS_SELECTOR, 'a[class="btn btn-default"]')


class LoginPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, 'input[name="login-username"')
    LOGIN_PASSWORD_LINK = (By.CSS_SELECTOR, 'input[name="login-password"')
    REG_EMAIL_LINK = (By.CSS_SELECTOR, 'input[name="registration-email"')
    REG_PASS_LINK = (By.CSS_SELECTOR, 'input[name="registration-password1"')
    REG_PASS_RE_LINK = (By.CSS_SELECTOR, 'input[name="registration-password2"')
    LOGIN_FORM = (By.CSS_SELECTOR, 'form[id="login_form"]')
    REGISTER_FORM = (By.CSS_SELECTOR, 'form[id="register_form"]')
    REGISTER_BUTTON = (By.CSS_SELECTOR, 'button[name="registration_submit"]')
    LOGIN_BUTTON = (By.CSS_SELECTOR, 'button[name="login_submit"]')


class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, 'form[id="add_to_basket_form"] > button')
    PRODUCT_NAME = (By.CSS_SELECTOR, "h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    ALLERT_NAME = (By.CSS_SELECTOR, 'div[class="alertinner "] > strong')
    ALLERT_PRICE = (By.CSS_SELECTOR, 'div[class="alertinner "]>P > strong')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages .alert-success")
    BASKET_LINK = (By.CSS_SELECTOR, 'a[class="btn btn-default"]')
    MESSAGE_PRODUCT_NAME = (By.CSS_SELECTOR, "#messages .alert-success .alertinner strong")
    MESSAGE_PRODUCT_PRICE = (By.CSS_SELECTOR, "#messages .alert-info .alertinner strong")


class BasketPageLocators():
    EMPTY_TEXT = (By.CSS_SELECTOR, "#content_inner p")
    BASKET_ITEMS = (By.CSS_SELECTOR, ".basket-items")
