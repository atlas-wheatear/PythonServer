import pytest
from selenium import webdriver
import pythonserver.server as server
from multiprocessing import Process

def create_test_app():
    app_process = Process(target=server.run_app)
    app_process.start()
    return app_process

# firefox fixture
@pytest.fixture(scope="class")
def gecko_driver_init(request):
    gecko_driver = webdriver.Firefox()
    request.cls.driver = gecko_driver
    yield
    gecko_driver.close()

# python-server fixture
@pytest.fixture(scope="class")
def server_init(request):
    app_process = create_test_app()
    yield
    app_process.terminate()
    app_process.join()


@pytest.mark.usefixtures("gecko_driver_init", "server_init")
class Test_App:
    def test_hello(self):
        return True
