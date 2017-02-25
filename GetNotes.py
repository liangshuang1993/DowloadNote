from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Firefox()
browser.get("https://note.wiz.cn/login?p=login") # Load page
#assert "WitzNote!" in browser.title
#elem = browser.find_element_by_name("p") # Find the query box
#elem.send_keys("seleniumhq" + Keys.RETURN)
time.sleep(0.2) # Let the page load, will be added to the API

try:
    email = browser.find_element_by_xpath("//input[@name='email']")
except NoSuchElementException:
    assert 0, "can't find email"
email.clear()
email.send_keys("1371685081@qq.com")

try:
    password = browser.find_element_by_xpath("//input[@name='password']")
except NoSuchElementException:
    assert 0, "can't find email"
password.clear()
password.send_keys("543212")
#submit
browser.find_element_by_id("loginbtn").click()
time.sleep(2)
#elements = browser.find_elements_by_class_name("doclist-noteinfo")
#print len(elements)
#for element in elements:
#    print element.text

browser.find_element_by_class_name("toolbar").click()
time.sleep(0.5)

folders = []
elements = browser.find_elements_by_class_name("level1")
length = len(elements)
for i in range(length/3 - 3):
    print elements[3 * i].text
    folders.append(elements[3 * i].text)
    
#print folders

button_id = "categoryTree_" + str(2) + "_a" 
elements = browser.find_elements_by_id(button_id)
element = elements[0]
element.click()
time.sleep(0.5)


elements = browser.find_elements_by_class_name("doclist-noteinfo")
for element in elements:
    print element.text


browser.close()
