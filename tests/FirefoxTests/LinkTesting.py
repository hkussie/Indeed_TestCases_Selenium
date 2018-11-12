import time 
import unittest 
from selenium import webdriver 
from selenium.webdriver.common.keys import Keys

class LinksTest(unittest.TestCase):

	# Open the chrome browser 
	def setUp(self):
		self.driver = webdriver.Firefox()

	# Search through the recommended jobs links
	def testMainPage(self):
		driver = self.driver 
		driver.get("https://www.Indeed.com")
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
		time.sleep(5)
		self.driver.close()	 

if __name__ == "__main__":
	unittest.main()

