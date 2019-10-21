from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class HomePage:

    def __init__(self, driver):
        self.driver = driver
        # self.search_txt_fld = self.driver.find_element_by_css_selector("#fakebox-input")


    def search_using_text(self, text):
        # search_field = self.driver.find_element_by_css_selector("#fakebox-input")
        search_field = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.NAME, "q")))
        search_field.clear()
        search_field.send_keys(text)
        search_field.send_keys(Keys.RETURN)
