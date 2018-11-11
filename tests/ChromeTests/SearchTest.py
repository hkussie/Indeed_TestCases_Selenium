import time
import unittest 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys 

class MainSearchBarTest(unittest.TestCase):

	# Open the browser 
	def setUp(self):
		self.driver = webdriver.Chrome("/Users/harrisonk1/Downloads/chromedriver")

	# Get the browser and search for a particular job in input tag: q	
	def testJobSearch(self):
		driver = self.driver
		driver.get("https://www.indeed.com/")
		driver.delete_all_cookies()
		elem = driver.find_element_by_name("q")
		elem.clear()
		elem.send_keys("Software Engineer")
		elem.send_keys(Keys.RETURN)
		assert "No results found." not in driver.page_source
	
	# Get the browser and search for location in input tag: l 
	def testLocationSearch(self):
		driver = self.driver
		driver.get("https://www.indeed.com/")
		driver.delete_all_cookies()
		location_element = driver.find_element_by_name("l")
		location_element.clear()
		location_element.send_keys("Santa Fe")
		location_element.send_keys(Keys.RETURN)
		assert "No results found." not in driver.page_source

	# Close the browser after six seconds 	
	def tearDown(self):
		time.sleep(6)
		self.driver.close()

if __name__ == "__main__":
	unittest.main()