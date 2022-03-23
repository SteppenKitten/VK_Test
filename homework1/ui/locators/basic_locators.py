from selenium.webdriver.common.by import By

LOGIN_INITIALIZE_BUTTON_LOCATOR = (By.CLASS_NAME, "responseHead-module-button-2yl51i")
EMAIL_INPUT_LOCATOR = (By.NAME, 'email')
PASSWORD_INPUT_LOCATOR = (By.NAME, 'password')
SIGN_IN_BUTTON_LOCATOR = (By.CLASS_NAME, "authForm-module-button-1u2DYF")
PROFILE_PAGE_LOCATOR = (By.CLASS_NAME, 'center-module-button-14O4yB.center-module-profile-1kuUOa')
CHANGE_NAME_FIELD_LOCATOR = (By.XPATH, "//*[@class='input__inp js-form-element' and @maxlength='100']")
SUBMIT_CHANGE_BUTTON_LOCATOR = (By.CLASS_NAME, 'button.button_submit')
SIGN_OUT_BUTTON_LOCATOR = (By.XPATH, "//*[@href='/logout']")
USER_NAME_ABOVE_LOCATOR = (By.CLASS_NAME, 'right-module-userNameWrap-3Odw2D')
STATISTICS_PAGE_LOCATOR = (By.CLASS_NAME, 'center-module-button-14O4yB.center-module-statistics-2Wbrwh')
AUDIENCE_PAGE_LOCATOR = (By.CLASS_NAME, 'center-module-button-14O4yB center-module-segments-1MqckW')
CONTACT_INFORMATION_BUTTON_LOCATOR = (By.CLASS_NAME, 'left-nav__text.js-align-info-bubble')