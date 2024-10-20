
from pages.base_page import BasePage
from locators.sign_in_page import LocatorsSignIn
from locators.vacancy_catalog_page import LocatorsCatalogVacancy
from data.data import DataUser


class SignInPage(BasePage):
    def sign_in_true(self):
        self.fill_the_field(LocatorsSignIn.field_email,DataUser.email)
        self.click_on_element(LocatorsSignIn.button_sign_in_with_password)
        self.fill_the_field(LocatorsSignIn.field_password,DataUser.password)
        self.click_on_element(LocatorsSignIn.button_visible_password)
        self.click_on_element(LocatorsSignIn.button_next)
        self.find_element_with_wait(LocatorsCatalogVacancy.tittle_vacancy)
