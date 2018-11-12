import time 
import unittest
from selenium import webdriver 
from selenium.webdriver.common.keys import Keys


class MainPageLinkTest(unittest.TestCase):

	# Open the chrome browser 
	def setUp(self):
		self.driver = webdriver.Chrome("/Users/harrisonk1/Downloads/chromedriver")

	# Search through the recommended jobs links
	def testRecentSearchLinks(self):
		driver = self.driver
		driver.get("https://www.indeed.com/")
		driver.findElement(By.linkText("data tester - Seattle, WA")).click()
		driver.navigate().back()
		driver.findElement(By.linkText("qa tester - Seattle, WA")).click()
		driver.navigate().back()
		driver.findElement(By.linkText("etl tester - Seattle, WA")).click()
		driver.navigate().back()
		driver.findElement(By.linkText("software engineer - Seattle, WA")).click()
		driver.navigate().back()

	# Close the browser after six seconds 	
	def tearDown(self):
		time.sleep(10)
		self.driver.close()

if __name__ == "__main__":
	unittest.main()