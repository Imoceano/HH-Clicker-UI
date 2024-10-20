from pages.base_page import BasePage
from locators.vacancy_catalog_page import LocatorsCatalogVacancy

class CatalogPage(BasePage):
    def go_to_the_my_resume_page(self):
        self.click_on_element(LocatorsCatalogVacancy.button_my_resume)
    
    
        
        