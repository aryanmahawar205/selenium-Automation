# making necessary package imports
from selenium import webdriver #basic webdriver import
from selenium.webdriver.chrome.service import Service #importing chrome webdriver Service
from selenium.webdriver.common.by import By #importing searching techniques to find HTML elements
from selenium.webdriver.common.keys import Keys #keyboard keys like enter, arrow keys, function keys, etc
from selenium.webdriver.support.ui import WebDriverWait #module to intermittently wait for the element to exist on the webpage
from selenium.webdriver.support import expected_conditions as EC #to detect the presence of element located by the HTML element
import time #time module to freeze the page intermittently

# setting up service with chrome webdriver
service = Service(executable_path = "chromedriver.exe")
driver = webdriver.Chrome(service = service)

# accessing a website through the driver
driver.get("https://www.google.com")

# freezing the website for 5 seconds
time.sleep(5)

# sometimes we might encounter a condition that the website is loading and the element we actually want to locate has not shown up
# in such a cases the program would crash and to avoid this we use the WebDriverWait function
# this makes the driver wait for a few seconds which we specify
# after the wait we use the expected_condition (EC) attribute to make sure that the HTML elements we wish to search by is located
WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, "gLFyf")))

# creating an input element
# here the input element is the search box in google.com
# on inspecting the page, it is found that the search field has a class "gLFyf"
input_element = driver.find_element(By.CLASS_NAME, "gLFyf")

# clearing the search box
# once we send keys to the input element, it only appends it to them and does not clear the field at first
# therefore it is good to manually clear the search field
input_element.clear()

# sending a key or a query for search - tech with tim
# in order to search for it, we have to press enter which is done with the Keys attribute
input_element.send_keys("tech with tim" + Keys.ENTER)

# freezing the website for 5 seconds
time.sleep(5)

# the same WebDriverWait check as explained in line 17
# the By.Partial_Link_Text will look for the text - "Tech With Tim" if found in any anchor tag
WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "Tech With Tim")))

# finding the clickable link with text - "Tech With Tim" and clicking it
link = driver.find_element(By.PARTIAL_LINK_TEXT, "Tech With Tim")
link.click()

# freezing the entire process for 10 seconds
time.sleep(30)

# quitting the driver once website has been automated
driver.quit()