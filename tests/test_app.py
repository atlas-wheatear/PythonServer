import pytest
from selenium import webdriver
import pythonserver.server.main as server
from flask import Flask

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
    app = server.create_app()
    request.cls.driver = app
    

@pytest.mark.usefixtures("gecko_driver_init")
class Test_App:
    def test_hello(self):
        return True
