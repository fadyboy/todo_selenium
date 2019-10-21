from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class LoginPage():

    def __init__(self, driver):
        self.driver = driver


    def navigate_to_login(self):
        login_btn = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "Log in")))
        login_btn.click()

    def login_to_app(self, username, password):
        username_fld = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "username")))
        username_fld.clear()
        username_fld.send_keys(username)
        password_fld = self.driver.find_element_by_id("password")
        password_fld.send_keys(password)
        login_btn = self.driver.find_element_by_id("login-button")
        login_btn.click()

    # def verify_add_task_field_present(self):
    #     add_task_field = WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.CLASS_NAME, "div.b-Rn-Um")))
    #     if add_task_field:
    #         return True
    #     return False