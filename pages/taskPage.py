import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
import time

class TaskPage():

    def __init__(self, driver):
        self.driver = driver


    def verify_add_task_field_present(self):
        add_task_field = WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.b-Rn-Um")))
        if add_task_field:
            return True
        return False


    def enter_new_task(self, task):
        task_txt_fld = WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.b-Rn-tm-Zs-at")))
        task_txt_fld.clear()
        task_txt_fld.send_keys(task)
        task_txt_fld.click # enables the add task btn to be visible
        # task_txt_fld.send_keys(Keys.RETURN)
        add_task_btn = WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.b-Rn-i-Zn.Vm-i")))
        add_task_btn.click()


    def verify_task_entered(self, task):
        task_details = WebDriverWait(self.driver, 15).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "b-fb-bn-Oj")))
        time.sleep(0.5)
        for item in task_details:
            WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.CLASS_NAME, "b-fb-bn-Oj")))
            if task == item.text:
                return True
        return False


    def verify_if_tasks_present(self):
        try:
            time.sleep(0.5)
            # tasks_list = self.driver.find_elements_by_css_selector("div.Vm-Np-Op.Vm-Wm-i-Ck-Sj>div.Vm-Np-Op.Vm-Wm-i-Ij-Sj>span.b-po")
            tasks_list = self.driver.find_elements_by_css_selector("span.b-fb-bn-Oj")
            # tasks_list = WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "span.b-fb-bn-Oj")))
            if tasks_list:
                return True
        except TimeoutException:
            return False


    def delete_all_tasks(self):
        # check if list of task exist
        all_task_chk_box = WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.Vm-Np-Op.Vm-Wm-i-Ck-Sj>div.Vm-Np-Op.Vm-Wm-i-Ij-Sj>span.b-po")))
        time.sleep(0.5)
        all_task_chk_box.click()
        menu_items = self.driver.find_elements_by_css_selector("div.Vm-Np-Op.Vm-Wm-i-Ck-Sj>div.Vm-Np-Op.Vm-Wm-i-Ij-Sj")
        time.sleep(0.5)
        menu_items[-1].click() # click on last menu item
        time.sleep(0.5)
        sub_menu_items = self.driver.find_elements_by_css_selector("div.Vm-tn>div.Vm-tn-En")
        for sub_item in sub_menu_items:
            if sub_item.text == "Delete Tasks":
                sub_item.click()


    def logout_of_app(self):
        # sign out of app by clicking the setting button
        settings = WebDriverWait(self.driver, 15).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "i.Dj-Ej")))
        time.sleep(0.5)
        settings[0].click()
        settings_menu_items = WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.Vm-tn-En")))
        for item in settings_menu_items:
            if item.text == "Sign out":
                item.click()




