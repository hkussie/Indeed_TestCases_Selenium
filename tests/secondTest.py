import time 
import unittest 
from selenium import webdriver 
from selenium.webdriver.common.keys import Keys

class testJobsPage(unittest.TestCase):
	def createSelf(self):
		self.driver = webdriver.Firefox()

	def test_job_page(self):
		driver = self.driver
		element_header = get_elem('')

	def tear_down(self):
		time.sleep(10)
		self.driver.close()

if __name__ == "__main__":
	unittest.main()	


'''
class testBeta(unittest.TestCase):
	def setUp(self):
		self.driver = webdriver.Firefox()

	def test_search_indeed(self):
		driver = self.driver
		driver.get("https://www.indeed.com")
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
'''

