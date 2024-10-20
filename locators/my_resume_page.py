from selenium.webdriver.common.by import By


class MyResumePageLocators:
    button_auto_rise_resume = By.XPATH, "//span[text()='Поднимать автоматически']"
    button_manual_rise_resume = By.XPATH, "//span[text()='Поднять в поиске']"
    button_rise_without_text = By.XPATH, "(//button[@data-sentry-element='Button']//div)[2]"
    div_with_resume = By.XPATH, "//div[@class='footer--N5G4lLi_lfYcj7V1olYU']"
    text_area_resume = By.XPATH, "//div[@class='content--d5g8z5Moz30d1W63FFtm']"
    button_cookie = By.XPATH, "//button[@class='bloko-button bloko-button_kind-primary']"
    button_change_visibility = By.XPATH, "//span[text()='Изменить видимость']"
    title_resume = By.XPATH,"//h3[@data-sentry-element='Title']"
    resume_rised_up = By.XPATH, "//h2[text()='Готово, вы подняли резюме']"
