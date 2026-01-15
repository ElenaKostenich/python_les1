from selenium.webdriver.common.by import By


class HomePage:

    def __init__(self, browserDriver):
        self.browser = browserDriver

    def open(self):
       self.browser.get("https://www.demoblaze.com/")


    def click_galaxy_s6(self):
        galaxy_x6 = self.browser.find_element(By.XPATH, '//a[text()="Samsung galaxy s6"]')
        galaxy_x6.click()

    def click_monitor(self):
        monitor_link =self.browser.find_element(By.CSS_SELECTOR, '''[onclick="byCat('monitor')"]''')
        monitor_link.click()

    def check_product_count(self, count):
        monitors = self.browser.find_elements(By.CSS_SELECTOR, '.card')
        assert len(monitors) == count