from selenium import webdriver
import math
import time
link='http://suninjuly.github.io/alert_accept.html'

try:
	browser=webdriver.Chrome()
	browser.get(link)
	button=browser.find_element_by_class_name('btn')
	button.click()
	alert=browser.switch_to.alert
	alert.accept()
	x=browser.find_element_by_id('input_value').text
	def calc(x):
		return str(math.log(abs(12*math.sin(int(x)))))
	result=calc(x)	
	answer=browser.find_element_by_id('answer')
	answer.send_keys(result)
	btn2= browser.find_element_by_class_name('btn-primary')	
	btn2.click()
finally:
	time.sleep(5)
	browser.quit()	
	