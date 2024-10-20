from selenium.webdriver.common.by import By
class LocatorsMainPage:
        button_accept_city = By.XPATH, "//button[@data-qa='region-clarification-confirm']//span[1]"
        button_choose_another_city = By.XPATH, "//button[@data-qa='region-clarification-clarify']//span[1]"
        field_search_city = By.XPATH, "//input[@class='bloko-input-text']"
        subbutton_choose_city = By.XPATH, "////li[@class= 'suggest__item suggest__item_state_highlighted']"
        button_sign_in = By.XPATH, "//a[@data-qa='login']"
        button_go_to_choose_city = By.XPATH, "supernova-navi-item_area-switcher-button"
    