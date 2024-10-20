from selenium.webdriver.common.by import By


class LocatorsSignIn:
    button_sign_in_with_password = By.XPATH, "//span[@data-qa='expand-login-by-password-text']"
    field_email = By.XPATH, "(//input[@class='magritte-field___9S8Tw_6-0-9'])[2]"
    field_password = By.XPATH, "(//input[@name='password'])[2]"
    button_next = By.XPATH,"(//span[@class='magritte-button__content___BXYU0_5-1-12'])[3]"
    button_visible_password = By.XPATH, "//button[contains(@class,'magritte-action___JtMQB_4-4-4 magritte-action-mode-secondary___jvHEK_4-4-4')]"

    