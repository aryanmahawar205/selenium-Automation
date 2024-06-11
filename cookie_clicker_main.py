from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

service = Service(executable_path = "chromedriver.exe")

driver = webdriver.Chrome(service = service)
driver.get("https://orteil.dashnet.org/cookieclicker/")

time.sleep(10)

driver.quit()