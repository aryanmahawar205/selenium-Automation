from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# for older versions of Selenium, the chrome driver path had to be explicitly mentioned
# PATH = "D:\selenium-Automation\chromedriver-win64\chromedriver.exe"
# chrome_service = webdriver.ChromeService(PATH)

driver = webdriver.Chrome()
driver.get("https://www.amazon.in")

print("Title - ", driver.title)
driver.quit()