from selenium import webdriver
import time
import math

link='http://suninjuly.github.io/execute_script.html'
try:
	browser=webdriver.Chrome()
	browser.get(link)
	node_value=browser.find_element_by_id('input_value')
	value=node_value.text
	def calc(x):
		return str(math.log(abs(12*math.sin(int(x)))))
	result=calc(value)
	form=browser.find_element_by_xpath('/html/body/div')	
	browser.execute_script("return arguments[0].scrollIntoView(true);",form)
	
	answer=browser.find_element_by_id('answer')
	answer.send_keys(result)
	robotsRule=browser.find_element_by_id('robotsRule')
	robotCheckbox=browser.find_element_by_id('robotCheckbox')
	robotCheckbox.click()
	
	robotsRule.click()
	button=browser.find_element_by_class_name('btn')
	button.click()
finally:
	time.sleep(15)
	browser.quit()	
		