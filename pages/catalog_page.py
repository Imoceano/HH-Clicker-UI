import allure
from base_page import BasePage
from locators.vacancy_catalog_page import LocatorsCatalogVacancy
from locators.my_resume_page import MyResumePageLocators
from data.data import DataUser

class CatalogPage(BasePage):
    @allure.step('Перейти на страницу "Мое резюме"')
    def go_to_the_my_resume_page(self):
        self.click_on_element(LocatorsCatalogVacancy.button_my_resume)
        text = 'Поднять в поиске'
        if text in MyResumePageLocators == MyResumePageLocators.button_rise_without_text:
            self.find_element_with_wait(MyResumePageLocators.button_manual_rise_resume)
        else:
            print('Еще не прошло 4 часа!')
    
    
        
        