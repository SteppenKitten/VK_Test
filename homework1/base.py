import pytest
from ui.locators import basic_locators
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time



CLICK_RETRY = 3


class BaseCase:
    driver = None

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver):
        self.driver = driver

    def find(self, locator):
        return self.driver.find_element(*locator)

    def login(self):
        self.find(basic_locators.LOGIN_INITIALIZE_BUTTON_LOCATOR).click()
        self.find(basic_locators.EMAIL_INPUT_LOCATOR).send_keys('misterm60@mail.ru')
        self.find(basic_locators.PASSWORD_INPUT_LOCATOR).send_keys('vktest1!')
        self.find(basic_locators.SIGN_IN_BUTTON_LOCATOR).click()

    def logout(self):
        WebDriverWait(self.driver, 30, ignored_exceptions=StaleElementReferenceException).until(
            EC.visibility_of_element_located(basic_locators.USER_NAME_ABOVE_LOCATOR)).click()
        time.sleep(2)
        WebDriverWait(self.driver, 30, ignored_exceptions=StaleElementReferenceException).until(
            EC.visibility_of_element_located(basic_locators.SIGN_OUT_BUTTON_LOCATOR)).click()

        WebDriverWait(self.driver, 30, ignored_exceptions=StaleElementReferenceException).until(
            EC.visibility_of_element_located(basic_locators.LOGIN_INITIALIZE_BUTTON_LOCATOR))


    def change_name(self):
        WebDriverWait(self.driver, 40, ignored_exceptions=StaleElementReferenceException).until(
            EC.visibility_of_element_located(basic_locators.PROFILE_PAGE_LOCATOR)).click()

        WebDriverWait(self.driver, 40, ignored_exceptions=StaleElementReferenceException).until(
            EC.visibility_of_element_located(basic_locators.CHANGE_NAME_FIELD_LOCATOR))
        self.find(basic_locators.CHANGE_NAME_FIELD_LOCATOR).clear()
        self.find(basic_locators.CHANGE_NAME_FIELD_LOCATOR).send_keys('Грегори Пек')

        self.find(basic_locators.SUBMIT_CHANGE_BUTTON_LOCATOR).click()
        time.sleep(3)

        self.driver.get('https://target.my.com/dashboard')
        WebDriverWait(self.driver, 40, ignored_exceptions=StaleElementReferenceException).until(
            EC.visibility_of_element_located(basic_locators.PROFILE_PAGE_LOCATOR))


    def walk_on_personal_info(self):
        WebDriverWait(self.driver, 40, ignored_exceptions=StaleElementReferenceException).until(
            EC.visibility_of_element_located(basic_locators.PROFILE_PAGE_LOCATOR)).click()

        WebDriverWait(self.driver, 10, ignored_exceptions=StaleElementReferenceException).until(
            EC.visibility_of_element_located(basic_locators.CONTACT_INFORMATION_BUTTON_LOCATOR))


    def walk_on_statistics(self):
        WebDriverWait(self.driver, 30, ignored_exceptions=StaleElementReferenceException).until(
            EC.visibility_of_element_located(basic_locators.STATISTICS_PAGE_LOCATOR)).click()

        WebDriverWait(self.driver, 30, ignored_exceptions=StaleElementReferenceException).until(
            EC.visibility_of_element_located(basic_locators.CONTACT_INFORMATION_BUTTON_LOCATOR))

