from selenium import webdriver
import os
import time

link='http://suninjuly.github.io/file_input.html'
try:
	browser=webdriver.Chrome()
	browser.get(link)
	input1=browser.find_element_by_name('firstname')
	input1.send_keys('Ivan')
	input2=browser.find_element_by_name('lastname')
	input2.send_keys('Ivanov')
	input3=browser.find_element_by_name('email')
	input3.send_keys('IvanIvanov@mail.com')
	current_dir=os.path.abspath(os.path.dirname(__file__))
	file_path=os.path.join(current_dir,'lesson7_step5.txt')
	file_input=browser.find_element_by_id('file')
	file_input.send_keys(file_path)
	button=browser.find_element_by_class_name('btn')
	button.click()
finally:
	time.sleep(10)
	browser.quit()	
	