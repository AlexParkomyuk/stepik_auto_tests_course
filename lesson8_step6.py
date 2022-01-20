from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

link='http://suninjuly.github.io/explicit_wait2.html'

try:
	browser=webdriver.Chrome()
	browser.get(link)
	WebDriverWait(browser,12).until(
			EC.text_to_be_present_in_element((By.ID, 'price'), '$100')
		)
	button=browser.find_element_by_id('book')
	button.click()	
	def calc(x):
		return str(math.log(abs(12*math.sin(int(x)))))
	x=browser.find_element_by_id('input_value').text
	result=calc(x)
	answer= browser.find_element_by_id('answer')
	answer.send_keys(result)
	 
	button2=browser.find_element(By.ID,'solve')
	button2.click()
finally:
	time.sleep(5)
	browser.quit()