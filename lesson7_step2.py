from selenium import webdriver
 
import math
import time
link='http://suninjuly.github.io/get_attribute.html'
try:
	browser= webdriver.Chrome()
	browser.get(link)
	value_node=browser.find_element_by_id('treasure') 
	value=value_node.get_attribute('valuex') 
	def calc(x):
		return str(math.log(abs(12*math.sin(int(x)))))
		
	x=calc(value)
	answer=browser.find_element_by_id('answer')
	answer.send_keys(x)
	robotCheckbox= browser.find_element_by_id('robotCheckbox')	
	robotCheckbox.click()
	robotsRule= browser.find_element_by_id('robotsRule')	
	robotsRule.click()
	button= browser.find_element_by_class_name('btn')	
	button.click()
finally:
	time.sleep(10)
	browser.quit()