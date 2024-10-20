import allure
from base_page import BasePage
from locators.main_page import LocatorsMainPage
from locators.sign_in_page import LocatorsSignIn
from data import data


class MainPage(BasePage):
   @allure.step('Подвердить выбор города, который предложен сейчас')
   def accept_city_on_start_page(self):
      self.click_on_element(LocatorsMainPage.button_accept_city)
      return self.get_text_from_element(LocatorsMainPage.button_accept_city)
    
   
   @allure.step('Выбор другого города')
   def choose_another_city(self):
      self.click_on_element(LocatorsMainPage.button_choose_another_city)
      self.find_element_with_wait(LocatorsMainPage.field_search_city)
      self.fill_the_field(LocatorsMainPage.field_search_city,data.DataUser.city)
      self.click_on_element(LocatorsMainPage.subbutton_choose_city)
      self.find_element_with_wait(LocatorsMainPage.button_go_to_choose_city)
    
   @allure.step('Перейти на страницу "Войти"')
   def sign_in_true(self):
      self.click_on_element(LocatorsMainPage.button_sign_in)
      self.find_element_with_wait(LocatorsSignIn.field_email)

      
      