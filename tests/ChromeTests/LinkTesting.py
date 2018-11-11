import time 
import unittest
from selenium import webdriver 
from selenium.webdriver.common.keys import Keys


class MainPageLinkTest(unittest.TestCase):

	def setUp(self):
		self.driver = webdriver.Chrome("/Users/harrisonk1/Downloads/chromedriver")

	def testJobSearch(self):
		driver = self.driver
		driver.get("https://www.indeed.com/")
		driver.findElement(By.linkText("data tester - Seattle, WA")).click()
		# recent_search_link = driver.find_element_by_link_text("data tester - Seattle, WA")

	# Close the browser after six seconds 	
	def tearDown(self):
		time.sleep(10)
		self.driver.close()

if __name__ == "__main__":
	unittest.main()