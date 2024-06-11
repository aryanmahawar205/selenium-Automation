# making necessary package imports
from selenium import webdriver #basic webdriver import
from selenium.webdriver.chrome.service import Service #importing chrome webdriver Service
from selenium.webdriver.common.by import By #importing searching techniques to find HTML elements
from selenium.webdriver.support.ui import WebDriverWait #module to intermittently wait for the element to exist on the webpage
from selenium.webdriver.support import expected_conditions as EC #to detect the presence of element located by the HTML element
import time #time module to freeze the page intermittently

# setting up service with chrome webdriver
service = Service(executable_path = "chromedriver.exe")
driver = webdriver.Chrome(service = service)

# accessing cookie clickers website through the driver
driver.get("https://orteil.dashnet.org/cookieclicker/")

# freezing the website for 10 seconds after loading
time.sleep(10)

# ID names for various HTML elements on the webpage
cookie_ID = "bigCookie"
cookies_count_ID = "cookies"
product_price_prefix = "productPrice"
product_prefix = "product"

# sometimes we might encounter a condition that the website is loading and the element we actually want to locate has not shown up
# in such a cases the program would crash and to avoid this we use the WebDriverWait function
# this makes the driver wait for a few seconds which we specify
# after the wait we use the expected_condition (EC) attribute to make sure that the HTML elements we wish to search by is located
# when we load up the website, we get an intermittent screen where the game asks us to choose a language to proceed
# after we choose the language, the webpage refreshes itself with the selected language and then we can start clicking the cookie
# this line incorporated the WEbDriverWait functionality with the search of HTML element by the XPATH method
# XPATH method is a convenient way to access the language block by passing the text to contains function for 'English' language
WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'English')]")))

# after the WebDriverWait function waits for 5 seconds for the language selection to show we, we click on the language 'English'
language = driver.find_element(By.XPATH, "//*[contains(text(), 'English')]")
language.click()

# freezing the website for 5 seconds after selecting English language
time.sleep(5)


# the same WebDriverWait check as explained in line 25
# the By.ID will look for the ID - "bigCookie" stored in the variable cookie_ID
WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, cookie_ID)))

# instance for the cookie to be clicked
cookie = driver.find_element(By.ID, cookie_ID)

# an infinite while loop to simulate continuous clicks to automate the game
while True:
    cookie.click()
    # cookies_count variable keeps track of the count of the cookies clicked
    # we find its corresponding HTML element by the ID = "cookies" which is stored in variable cookies_count_ID
    # once we have that it is important to split the string at white space and access the 0th element from it
    # the 0th element will essentially contain the count or the actual number of the cookies count
    cookies_count = driver.find_element(By.ID, cookies_count_ID).text.split(" ")[0]
    # we have to take care of cases where the number is greater than 3 digit, say 12,000 where the string has a comma in it
    # therefore replacing the comma with an empty string and typecasting the entire thing the integer
    # this will finally provide us an integer number without any commas
    cookies_count = int(cookies_count.replace(",", ""))
    
    #running the for loop for 4 iterations because essentially when a new instance of cookie clickers is run it has 4 upgrade options
    # applying similar methodology as above for the upgrades
    for i in range(4):
        product_price = driver.find_element(By.ID, product_price_prefix + str(i)).text.replace(",", "")
        
        if not product_price.isdigit():
            continue
        
        product_price = int(product_price)
        
        # if enough cookies are available in order to upgrade, we click on the upgrade option
        # after that, break from the for loop and continue the process again
        if (cookies_count >= product_price):
            product = driver.find_element(By.ID, product_prefix + str(i))
            product.click()
            break