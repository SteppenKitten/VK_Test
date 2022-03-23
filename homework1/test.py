import pytest
from base import BaseCase
from ui.locators import basic_locators
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
import conftest
import time

class TestExample(BaseCase):

    @pytest.mark.UI
    def test_login(self):
        self.login()
        assert self.driver.current_url == 'https://target.my.com/dashboard'

    @pytest.mark.UI
    def test_logout(self):
        self.login()
        time.sleep(2)
        self.logout()
        assert self.driver.current_url == 'https://target.my.com/'

    @pytest.mark.UI
    def test_change_name(self):
        self.login()
        self.change_name()
        assert 'Грегори Пек' in self.driver.page_source

    @pytest.mark.parametrize("test_input,expected", [(BaseCase.walk_on_personal_info, 'https://target.my.com/profile/contacts'),(BaseCase.walk_on_statistics, 'https://target.my.com/statistics/summary')])
    def test_walk_around(self, test_input, expected):
        self.login()
        test_input(self)
        assert self.driver.current_url == expected




