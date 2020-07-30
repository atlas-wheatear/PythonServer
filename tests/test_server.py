import pytest
from selenium import webdriver
import pythonserver.server as server
import pythonserver.models as models
from multiprocessing import Process
from selenium.webdriver.chrome.options import Options as Chrome_Options
from selenium.webdriver.firefox.options import Options as Firefox_Options
from selenium.webdriver.common.keys import Keys
import random
import string
from mock import patch

server_root = "http://localhost:5000"

class Mock_Model():
    pass

class Server_Driver():
    @patch('models.Model')
    def patch_model(self, Mock_Model):
        pass

    def create_test_app_process(self):
        app_process = Process(target=server.run_app)
        app_process.start()
        return app_process

    def __init__(self):
        self.app_process = self.create_test_app_process()
    
    def terminate(self):
        self.app_process.terminate()
        self.app_process.join()


class Test_Server():
    # python-server fixture
    @pytest.fixture(scope="class", autouse=True)
    def server_init(self):
        print("Running flask server.")
        server_driver = Server_Driver()
        yield
        server_driver.terminate()

    # firefox fixture
    @pytest.fixture(scope="class", autouse=True)
    def firefox_init(self, request):
        options = Firefox_Options()
        options.headless = True
        print("Running firefox.")
        driver = webdriver.Firefox(options=options)
        request.cls.firefox_driver = driver
        yield
        driver.close()

    # chrome fixture
    @pytest.fixture(scope="class", autouse=True)
    def chrome_init(self, request):
        options = Chrome_Options()
        options.add_argument("--no-sandbox")
        options.add_argument("--headless")
        options.add_argument("--disable-gpu")
        options.add_argument("--remote-debugging-port=9222")
        options.add_argument("--disable-dev-shm-usage")
        print("Running chrome.")
        driver = webdriver.Chrome(options=options)
        request.cls.chrome_driver = driver
        yield
        driver.close()
    
    def get(self, url: str):
        for driver in (self.firefox_driver, self.chrome_driver):
            driver.get(url)
    
    def test_hello(self):
        self.get(server_root)
    
    def test_update_word(self):
        for driver in (self.firefox_driver, self.chrome_driver):
            driver.get(server_root)
            word_form = driver.find_element_by_name("word-of-the-day")
            test_string = "".join(random.choices(string.ascii_letters, k=random.randint(1, 20)))
            word_form.send_keys(test_string)
            word_form.submit()
            driver.get(server_root)
            word_div = driver.find_element_by_id("word-container")
            assert word_div.text == "The word of the day is {}!".format(test_string)
