from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait as WAIT
import logging
logging.basicConfig(level=logging.INFO)


class BasePage:


    
    def __init__(self,driver):
        self.driver = driver

    def find_element_with_wait(self,locator):
        WAIT(self.driver, 10).until(EC.visibility_of_element_located(locator)) #Поиск элемента с ожиданием
        return self.driver.find_element(*locator)
    
    def click_on_element(self, locator):
        element = self.find_element_with_wait(locator)
        element.click() #клик на элемент

    def get_text_from_element(self,locator):
        element = self.find_element_with_wait(locator) 
        return element.text
    
    def scroll_down(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);") #Скролл к подвалу
    

    def scroll_to_locator(self,locator):
        element = self.find_element_with_wait(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
    
    def get_url(self,url):
        self.driver.get(url)

    def switch_window(self,element):
        self.driver.switch_to.window(self.driver.window_handles[element])
    
    # def check_element_on_page(self,locator):
    #     self.driver.is_element_present(locator)
    def check_element_on_page(self, locator):
        try:
            return self.driver.is_element_present(locator)
        except Exception as e:
            logging.error(f'Ошибка при проверке элемента: {str(e)}')
            return False  # Возврат False в случае ошибки

    def fill_the_field(self,locator,data):
        element = self.find_element_with_wait(locator)
        element.click()
        element.clear() 
        element.send_keys(data) 

 