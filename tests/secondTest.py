import time 
import unittest 
from selenium import webdriver 
from selenium.webdriver.common.keys import Keys

class BasicSecurityTest(unittest.TestCase):
	
	def setUp(self):
		self.driver = webdriver.Firefox()

	def clearCookies(self):
		driver = self.driver
		driver.get("https://Indeed.com") 
		# driver.get_cookies()

	def tearDown(self):
		time.sleep(5)
		self.driver.close()

if __name__ == "__main__":
	unittest.main()				

'''
class testJobsPage(unittest.TestCase):
	def setUp(self):
		self.driver = webdriver.Firefox()

	def test_main_page(self):
		driver = self.driver
		driver.get('https://www.indeed.com')

	def tear_down(self):
		time.sleep(3)
		self.driver.close()

if __name__ == "__main__":
	unittest.main()	
'''