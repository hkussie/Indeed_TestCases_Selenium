import time 
import unittest 
from selenium import webdriver 
from selenium.webdriver.common.keys import Keys

class LinksTest(unittest.TestCase):
	def setUp(self):
		self.driver = webdriver.Firefox()

	def testMainPage(self):
		driver = self.driver 
		driver.get("https://www.youtube.com")
		
	def closeBrowser(self):
		time.sleep(5)
		self.driver.close()	 

if __name__ == "__main__":
	unittest.main()

