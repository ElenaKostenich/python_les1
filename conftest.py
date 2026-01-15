import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture
def browserDriver():
   options = Options()
   options.add_argument('--headless')
   browserDriver = webdriver.Chrome(options=options)
   browserDriver.maximize_window()
   browserDriver.implicitly_wait(3) #delay 3 sec
   yield browserDriver
   browserDriver.close()