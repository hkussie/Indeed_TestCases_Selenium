import time 
import unittest 
from selenium import webdriver 
from selenium.webdriver.common.keys import Keys

class ChromeBrowserTest(unittest.TestCase):

	# Open the browser 
	def setUp(self):
		self.driver = webdriver.Firefox()

	def testJobSearch(self):
		driver = self.driver
		driver.get("https://www.indeed.com/")
		driver.delete_all_cookies()
		elem = driver.find_element_by_name("q")
		elem.send_keys("Software Engineer")
		elem.send_keys(Keys.RETURN)
		assert "No results found." not in driver.page_source
	
	def testLocationSearch(self):
		driver = self.driver
		driver.get("https://www.indeed.com/")
		driver.delete_all_cookies()
		location_element = driver.find_element_by_name("l")
		location_element.send_keys("Santa Fe")
		location_element.send_keys(Keys.RETURN)
		assert "No results found." not in driver.page_source

	def tearDown(self):
		time.sleep(6)
		self.driver.close()

if __name__ == "__main__":
	unittest.main()