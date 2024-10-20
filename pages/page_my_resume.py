from pages.base_page import BasePage
from locators.my_resume_page import MyResumePageLocators
from time import sleep


class MyResumePage(BasePage):

    def click_on_button_rise_resume(self):
        
      
        self.click_on_element(MyResumePageLocators.button_cookie)
        self.find_element_with_wait(MyResumePageLocators.title_resume)
        self.scroll_to_locator(MyResumePageLocators.button_auto_rise_resume) 
        self.find_element_with_wait(MyResumePageLocators.button_auto_rise_resume)
        self.click_on_element(MyResumePageLocators.button_rise_without_text)
    
        
        assert self.check_element_on_page(MyResumePageLocators.resume_rised_up), "Резюме не поднято. Еще не прошло 4 часа"
            
