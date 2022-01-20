from selenium import webdriver
import math
import time
link='http://suninjuly.github.io/redirect_accept.html'
link2='http://suninjuly.github.io/redirect_page.html?'
try:
	browser=webdriver.Chrome()
	browser.get(link)
	button=browser.find_element_by_class_name('btn')
	button.click()
	new_window=browser.window_handles[1]
	 
	browser.switch_to.window(new_window)
	x=browser.find_element_by_id('input_value').text
	def calc(x):
		return str(math.log(abs(12*math.sin(int(x)))))
	
	result=calc(x)
	
	answer=browser.find_element_by_id('answer')
	answer.send_keys(result)
	button2=browser.find_element_by_class_name('btn-primary')
	button2.click()
finally:
	print("window handle has changed.")
	time.sleep(5)
	browser.quit()
	 
