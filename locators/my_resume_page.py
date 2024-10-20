from selenium.webdriver.common.by import By

class MyResumePageLocators:

    button_auto_rise_resume = By.XPATH,"//span[text()='Поднимать автоматически']"
    button_manual_rise_resume = By.XPATH,"//span[text()='Поднять в поиске']"
    button_rise_without_text = By.XPATH, "//button[@data-qa='resume-update-button_actions']//div"