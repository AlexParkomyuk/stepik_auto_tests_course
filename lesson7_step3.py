from selenium import webdriver
from selenium.webdriver.support.ui import Select
import math
import time
link='http://suninjuly.github.io/selects1.html'
try:
	browser=webdriver.Chrome()
	browser.get(link)
	def summ_values(v1,v2):
		return str(int(v1)+int(v2))
	value1=browser.find_element_by_id('num1').text
	value2=browser.find_element_by_id('num2').text
	result=summ_values(value1, value2)	
	select= Select(browser.find_element_by_tag_name('select')) 
	select.select_by_value(result)
	button=browser.find_element_by_class_name('btn')
	button.click()
finally:
	time.sleep(10) 
	browser.quit()	