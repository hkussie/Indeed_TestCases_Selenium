import time
import unittest 
from selenium import webdriver 

class ChromeBrowserTest(unittest.TestCase):

	# Open the browser 
	def setUp(self):
		self.driver = webdriver.Chrome("/Users/harrisonk1/Downloads/chromedriver")

	def testCookies(self):
		driver = self.driver
		driver.get("http://google.com")
		driver.delete_all_cookies()
	
	def testCloseBrowser(self):
		time.sleep(5)
		self.driver.close()

if __name__ == "__main__":
	unittest.main()