from selenium import webdriver
import math
import time

link='http://suninjuly.github.io/math.html'
try:
	browser=webdriver.Chrome()
	browser.get(link)
	x_selector=browser.find_element_by_id('input_value')
	x_value=x_selector.text
	def calc(x):
		return str(math.log(abs(12*math.sin(int(x)))))
	result=calc(x_value)
	answer=browser.find_element_by_id('answer')
	answer.send_keys(result)	
	checkbox_robot=browser.find_element_by_id('robotCheckbox')
	checkbox_robot.click()
	radio_robots_rule=browser.find_element_by_id('robotsRule')
	radio_robots_rule.click()
	button= browser.find_element_by_class_name('btn')
	button.click()
	
finally:
	time.sleep(30)	
	browser.quit()