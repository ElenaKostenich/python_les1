from itertools import product

import time
from pages.homepage import HomePage
from pages.product import ProductPage




def test_open_s6(browserDriver):
    homepage = HomePage(browserDriver)
    homepage.open()
    homepage.click_galaxy_s6()
    productPage = ProductPage(browserDriver)
    productPage.check_title_is("Samsung galaxy s6")


def test_two_monitors(browserDriver):
    homepage = HomePage(browserDriver)
    homepage.open()

    # browserDriver.get("https://www.demoblaze.com/")
    homepage.click_monitor()
   # monitor_link = browserDriver.find_element(By.CSS_SELECTOR, '''[onclick="byCat('monitor')"]''')
    # monitor_link.click()
    time.sleep(2) # don't use this method in real life ))
    homepage.check_product_count(2)
    # monitors = browserDriver.find_elements(By.CSS_SELECTOR, '.card')
    # assert len(monitors) == 2
