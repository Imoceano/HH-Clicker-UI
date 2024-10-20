
import pytest
from locators.main_page import LocatorsMainPage
from pages.main_page import MainPage
from pages.sign_in_page import SignInPage
from pages.catalog_page import CatalogPage
from pages.page_my_resume import MyResumePage


class TestRiseResumeManual:
    def test_sign_in_and_rise_up(self,driver):
        main_page = MainPage(driver)
        main_page.go_to_sign_in_window()
        sign_in_page = SignInPage(driver)
        sign_in_page.sign_in_true()
        catalog_page = CatalogPage(driver)
        catalog_page.go_to_the_my_resume_page()
        my_resume_page = MyResumePage(driver)
        my_resume_page.click_on_button_rise_resume()
        
        