from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

def get_driver():
    chrome_options = Options()
    chrome_options.add_argument("--window-size=1920,800")
    chrome_options.add_argument('--headless')
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()),
                              options=chrome_options)
    driver.maximize_window()
    driver.implicitly_wait(10)
    return driver

def open_page(driver, URL):
    driver.get(URL)

def get_element_by_id(driver,locator):
    return driver.find_element(By.ID, locator)

def click_element(driver,locator):
    element = get_element_by_id(driver,locator)
    element.click()

def send_keys_element(driver, locator, text):
    element = get_element_by_id(driver, locator)
    element.send_keys(text)

def login(driver, LOGIN, PASSWORD):
    send_keys_element(driver, 'user-name', LOGIN)
    send_keys_element(driver, 'password', PASSWORD)
    click_element(driver, 'login-button')

URL = 'https://www.saucedemo.com'
LOGIN='standard_user'
PASSWORD='secret_sauce'
driver = get_driver()
open_page(driver, URL)
login(driver, LOGIN, PASSWORD)
driver.quit()