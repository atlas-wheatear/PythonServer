import pytest
from selenium import webdriver
import pythonserver.server as server
from multiprocessing import Process
from selenium.webdriver.chrome.options import Options as Chrome_Options
from selenium.webdriver.firefox.options import Options as Firefox_Options

def create_test_app():
    app_process = Process(target=server.run_app)
    app_process.start()
    return app_process

class Server_Driver():
    def __init__(self):
        self.app_process = create_test_app()
    def terminate(self):
        self.app_process.terminate()
        self.app_process.join()

# python-server fixture
@pytest.fixture(scope="class", autouse=True)
def server_init():
    print("Running flask server.")
    server_driver = Server_Driver()
    yield
    server_driver.terminate()

# firefox fixture
@pytest.fixture(scope="class")
def firefox_init(request):
    options = Firefox_Options()
    options.headless = True
    print("Running firefox.")
    driver = webdriver.Firefox(options=options)
    request.cls.firefox_driver = driver
    yield
    driver.close()

# chrome fixture
@pytest.fixture(scope="class")
def chrome_init(request):
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

@pytest.mark.usefixtures("firefox_init", "chrome_init")
class Test_Server():
    def get(self, url: str):
        for driver in (self.firefox_driver, self.chrome_driver):
            driver.get(url)
    def test_hello(self):
        self.get("http://localhost:5000")
        return True
