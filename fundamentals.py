from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service = Service(executable_path = "")
driver = webdriver.Chrome(service = service)