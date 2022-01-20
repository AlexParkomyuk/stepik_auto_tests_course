from selenium import webdriver

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/wait1.html")

 # говорим WebDriver искать каждый элемент в течение 5 секунд
browser.implicitly_wait(5)
button = browser.find_element_by_id("verify")
button.click()
message = browser.find_element_by_id("verify_message")

assert "successful" in message.text
-Если элемент не был найден за отведенное время, то мы получим NoSuchElementException.
Если элемент был найден в момент поиска, но при последующем обращении к элементу DOM изменился,
 то получим StaleElementReferenceException. Например, мы нашли элемент Кнопка и через какое-то время
 решили выполнить с ним уже известный нам метод click. Если кнопка за это время была скрыта скриптом, 
 то метод применять уже бесполезно — элемент "устарел" (stale) и мы увидим исключение.
Если элемент был найден в момент поиска, но сам элемент невидим (например, имеет нулевые размеры), 
и реальный пользователь не смог бы с ним взаимодействовать, то получим ElementNotVisibleException.

Explicit Waits(expected_conditions)
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/wait2.html")

# говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
button = WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.ID, "verify"))
    )
button.click()
message = browser.find_element_by_id("verify_message")

assert "successful" in message.text

В модуле expected_conditions есть много других правил, которые позволяют реализовать необходимые ожидания:

title_is
title_contains
presence_of_element_located
visibility_of_element_located
visibility_of
presence_of_all_elements_located
text_to_be_present_in_element
text_to_be_present_in_element_value
frame_to_be_available_and_switch_to_it
invisibility_of_element_located
element_to_be_clickable
staleness_of
element_to_be_selected
element_located_to_be_selected
element_selection_state_to_be
element_located_selection_state_to_be
alert_is_present

Event listener must subclass and implement this fully or partially

after_change_value_of(element, driver)
after_click(element, driver)
after_close(driver)
after_execute_script(script, driver)
after_find(by, value, driver)
after_navigate_back(driver)
after_navigate_forward(driver)
after_navigate_to(url, driver)
after_quit(driver)
before_change_value_of(element, driver)
before_click(element, driver)
before_close(driver)
before_execute_script(script, driver)
before_find(by, value, driver)
before_navigate_back(driver)
before_navigate_forward(driver)
before_navigate_to(url, driver)
before_quit(driver)
on_exception(exception, driver)
7.39. Expected conditions Support
class selenium.webdriver.support.expected_conditions.alert_is_present
Bases: object

Expect an alert to be present.

__init__()
Initialize self. See help(type(self)) for accurate signature.

class selenium.webdriver.support.expected_conditions.element_located_selection_state_to_be(locator, is_selected)
Bases: object

An expectation to locate an element and check if the selection state specified is in that state. locator is a tuple of (by, path) is_selected is a boolean

__init__(locator, is_selected)
Initialize self. See help(type(self)) for accurate signature.

class selenium.webdriver.support.expected_conditions.element_located_to_be_selected(locator)
Bases: object

An expectation for the element to be located is selected. locator is a tuple of (by, path)

__init__(locator)
Initialize self. See help(type(self)) for accurate signature.

class selenium.webdriver.support.expected_conditions.element_selection_state_to_be(element, is_selected)
Bases: object

An expectation for checking if the given element is selected. element is WebElement object is_selected is a Boolean.”

__init__(element, is_selected)
Initialize self. See help(type(self)) for accurate signature.

class selenium.webdriver.support.expected_conditions.element_to_be_clickable(locator)
Bases: object

An Expectation for checking an element is visible and enabled such that you can click it.

__init__(locator)
Initialize self. See help(type(self)) for accurate signature.

class selenium.webdriver.support.expected_conditions.element_to_be_selected(element)
Bases: object

An expectation for checking the selection is selected. element is WebElement object

__init__(element)
Initialize self. See help(type(self)) for accurate signature.

class selenium.webdriver.support.expected_conditions.frame_to_be_available_and_switch_to_it(locator)
Bases: object

An expectation for checking whether the given frame is available to switch to. If the frame is available it switches the given driver to the specified frame.

__init__(locator)
Initialize self. See help(type(self)) for accurate signature.

class selenium.webdriver.support.expected_conditions.invisibility_of_element(locator)
Bases: selenium.webdriver.support.expected_conditions.invisibility_of_element_located

An Expectation for checking that an element is either invisible or not present on the DOM.

element is either a locator (text) or an WebElement

class selenium.webdriver.support.expected_conditions.invisibility_of_element_located(locator)
Bases: object

An Expectation for checking that an element is either invisible or not present on the DOM.

locator used to find the element

__init__(locator)
Initialize self. See help(type(self)) for accurate signature.

class selenium.webdriver.support.expected_conditions.new_window_is_opened(current_handles)
Bases: object

An expectation that a new window will be opened and have the number of windows handles increase

__init__(current_handles)
Initialize self. See help(type(self)) for accurate signature.

class selenium.webdriver.support.expected_conditions.number_of_windows_to_be(num_windows)
Bases: object

An expectation for the number of windows to be a certain value.

__init__(num_windows)
Initialize self. See help(type(self)) for accurate signature.

class selenium.webdriver.support.expected_conditions.presence_of_all_elements_located(locator)
Bases: object

An expectation for checking that there is at least one element present on a web page. locator is used to find the element returns the list of WebElements once they are located

__init__(locator)
Initialize self. See help(type(self)) for accurate signature.

class selenium.webdriver.support.expected_conditions.presence_of_element_located(locator)
Bases: object

An expectation for checking that an element is present on the DOM of a page. This does not necessarily mean that the element is visible. locator - used to find the element returns the WebElement once it is located

__init__(locator)
Initialize self. See help(type(self)) for accurate signature.

class selenium.webdriver.support.expected_conditions.staleness_of(element)
Bases: object

Wait until an element is no longer attached to the DOM. element is the element to wait for. returns False if the element is still attached to the DOM, true otherwise.

__init__(element)
Initialize self. See help(type(self)) for accurate signature.

class selenium.webdriver.support.expected_conditions.text_to_be_present_in_element(locator, text_)
Bases: object

An expectation for checking if the given text is present in the specified element. locator, text

__init__(locator, text_)
Initialize self. See help(type(self)) for accurate signature.

class selenium.webdriver.support.expected_conditions.text_to_be_present_in_element_value(locator, text_)
Bases: object

An expectation for checking if the given text is present in the element’s locator, text

__init__(locator, text_)
Initialize self. See help(type(self)) for accurate signature.

class selenium.webdriver.support.expected_conditions.title_contains(title)
Bases: object

An expectation for checking that the title contains a case-sensitive substring. title is the fragment of title expected returns True when the title matches, False otherwise

__init__(title)
Initialize self. See help(type(self)) for accurate signature.

class selenium.webdriver.support.expected_conditions.title_is(title)
Bases: object

An expectation for checking the title of a page. title is the expected title, which must be an exact match returns True if the title matches, false otherwise.

__init__(title)
Initialize self. See help(type(self)) for accurate signature.

class selenium.webdriver.support.expected_conditions.url_changes(url)
Bases: object

An expectation for checking the current url. url is the expected url, which must not be an exact match returns True if the url is different, false otherwise.

__init__(url)
Initialize self. See help(type(self)) for accurate signature.

class selenium.webdriver.support.expected_conditions.url_contains(url)
Bases: object

An expectation for checking that the current url contains a case-sensitive substring. url is the fragment of url expected, returns True when the url matches, False otherwise

__init__(url)
Initialize self. See help(type(self)) for accurate signature.

class selenium.webdriver.support.expected_conditions.url_matches(pattern)
Bases: object

An expectation for checking the current url. pattern is the expected pattern, which must be an exact match returns True if the url matches, false otherwise.

__init__(pattern)
Initialize self. See help(type(self)) for accurate signature.

class selenium.webdriver.support.expected_conditions.url_to_be(url)
Bases: object

An expectation for checking the current url. url is the expected url, which must be an exact match returns True if the url matches, false otherwise.

__init__(url)
Initialize self. See help(type(self)) for accurate signature.

class selenium.webdriver.support.expected_conditions.visibility_of(element)
Bases: object

An expectation for checking that an element, known to be present on the DOM of a page, is visible. Visibility means that the element is not only displayed but also has a height and width that is greater than 0. element is the WebElement returns the (same) WebElement once it is visible

__init__(element)
Initialize self. See help(type(self)) for accurate signature.

class selenium.webdriver.support.expected_conditions.visibility_of_all_elements_located(locator)
Bases: object

An expectation for checking that all elements are present on the DOM of a page and visible. Visibility means that the elements are not only displayed but also has a height and width that is greater than 0. locator - used to find the elements returns the list of WebElements once they are located and visible

__init__(locator)
Initialize self. See help(type(self)) for accurate signature.

class selenium.webdriver.support.expected_conditions.visibility_of_any_elements_located(locator)
Bases: object

An expectation for checking that there is at least one element visible on a web page. locator is used to find the element returns the list of WebElements once they are located

__init__(locator)
Initialize self. See help(type(self)) for accurate signature.

class selenium.webdriver.support.expected_conditions.visibility_of_element_located(locator)
Bases: object

An expectation for checking that an element is present on the DOM of a page and visible. Visibility means that the element is not only displayed but also has a height and width that is greater than 0. locator - used to find the element returns the WebElement once it is located and visible

__init__(locator)
Initialize self. See help(type(self)) for accurate signature.

https://selenium-python.readthedocs.io/api.html#module-selenium.webdriver.support.expected_conditions