from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
import time 

browser = webdriver.Firefox()
browser.get('https://www.indeed.com')

assert "Job Search | Indeed" in browser.title
elem = browser.find_element_by_name("q")
elem.clear()
elem.send_keys("Software Engineer")
elem.send_keys(Keys.RETURN)
assert "No results found." not in browser.page_source

time.sleep(5)  
browser.close()
