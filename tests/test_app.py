import pytest
from selenium import webdriver
import pythonserver.server as server
from multiprocessing import Process

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
def browser_init(request):
    print("Running firefox.")
    driver = webdriver.Firefox()
    request.cls.driver = driver
    yield
    driver.close()

@pytest.mark.usefixtures("browser_init")
class Test_App():
    def test_hello(self):
        self.driver.get("http://localhost:5000")
        return True
