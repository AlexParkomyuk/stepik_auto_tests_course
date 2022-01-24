from selenium import webdriver
import time

link='http://suninjuly.github.io/find_xpath_form'
try:
	browser=webdriver.Chrome()
	browser.get(link)
	input1=browser.find_element_by_xpath('/html/body/div/form/div[1]/input')
	input1.send_keys('Alex')
	input2=browser.find_element_by_xpath('/html/body/div/form/div[2]/input')
	input2.send_keys('Par')
	input3=browser.find_element_by_xpath('/html/body/div/form/div[3]/input')
	input3.send_keys('Khabarovsk')
	input4=browser.find_element_by_xpath('/html/body/div/form/div[4]/input')
	input4.send_keys('Russia')
	button=browser.find_element_by_xpath('/html/body/div/form/div[6]/button[3]')
	button.click()
finally:
	time.sleep(30)		
	browser.quit()	