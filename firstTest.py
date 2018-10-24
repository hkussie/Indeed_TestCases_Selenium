import time 
import unittest 
from selenium import webdriver 
from selenium.webdriver.common.keys import Keys

class PythonSearchIndeed(unittest.TestCase):

	def setUp(self):
		self.driver = webdriver.Firefox()

	def test_search_indeed(self):
		driver = self.driver
		driver.get("https://Indeed.com")
		self.assertIn("Indeed", driver.title)
		elem = driver.find_element_by_name("q")
		elem.send_keys("Software Engineer")
		elem.send_keys(Keys.RETURN)
		assert "No results found." not in driver.page_source

	def tearDown(self):
		time.sleep(5)
		self.driver.close()

if __name__ == "__main__":
	unittest.main()