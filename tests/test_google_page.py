import unittest
import json
from selenium.webdriver import Chrome, Firefox
from pages.loginPage import LoginPage
from pages.taskPage import TaskPage


class GoogleTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.data = cls.read_test_file()
        cls.driver = Chrome(executable_path=cls.data["chrome_driver_path"])
        # cls.driver = Firefox(executable_path=cls.data["gecko_driver_path"])


    @classmethod
    def tearDownClass(cls):
        cls.driver.close()


    def setUp(self):
        driver = self.driver
        default_url = self.data["url"]
        driver.get(default_url)
        driver.maximize_window()


    def tearDown(self):
        task_page = TaskPage(self.driver)
        task_page.logout_of_app()


    def test_login_to_app(self):
        login_page = LoginPage(self.driver)
        self.login_to_app(login_page)
        task_page = TaskPage(self.driver)
        self.assertTrue(task_page.verify_add_task_field_present())


    def test_login_and_create_multiple_tasks(self):
        login_page = LoginPage(self.driver)
        self.login_to_app(login_page)
        task_page = TaskPage(self.driver)
        task = self.data["task1"]
        task_page.enter_new_task(task)
        self.assertTrue(task_page.verify_task_entered(task))
        task_2 = self.data["task2"]
        task_page.enter_new_task(task_2)
        self.assertTrue(task_page.verify_task_entered(task_2))


    def test_delete_all_task(self):
        login_page = LoginPage(self.driver)
        self.login_to_app(login_page)
        task_page = TaskPage(self.driver)
        check_if_tasks = task_page.verify_if_tasks_present()
        if check_if_tasks:
            task_page.delete_all_tasks()
        self.assertFalse(task_page.verify_if_tasks_present())


    def test_select_specific_task(self):
        login_page = LoginPage(self.driver)
        self.login_to_app(login_page)
        task_page = TaskPage(self.driver)
        task_page.enter_new_task(self.data["task3"])
        self.assertTrue(task_page.verify_task_entered(self.data["task3"]))
        task_page.enter_new_task(self.data["task4"])
        self.assertTrue(self.data["task4"])
        selected_task = task_page.select_specific_task(self.data["task3"])
        self.assertTrue(selected_task["selected"])
        self.assertIn(self.data["task3"], selected_task["innerText"])


    def login_to_app(self, login_page):
        username = self.data["username"]
        password = self.data["password"]
        login_page.navigate_to_login()
        login_page.login_to_app(username, password)


    @classmethod
    def read_test_file(self):
        with open("/Users/anthonyfadero/automation/test_data.json", "r") as test_data:
            data = json.load(test_data)

        return data




