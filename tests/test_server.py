import pytest
from selenium import webdriver
import pythonserver.server as server
from multiprocessing import Process
from selenium.webdriver.chrome.options import Options

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
    print("Running firefox.")
    driver = webdriver.Firefox()
    request.cls.firefox_driver = driver
    yield
    driver.close()

# chrome fixture
@pytest.fixture(scope="class")
def chrome_init(request):
    chrome_options = Options()
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--remote-debugging-port=9222")
    chrome_options.add_argument("--disable-dev-shm-usage")
    print("Running chrome.")
    driver = webdriver.Chrome(options=chrome_options)
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
