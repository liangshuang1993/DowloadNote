from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import time
import sys
import os

path = "E:\\Notes\\"

def save_article(floder_, title_ele, names, count):
    if count < len(title_ele):
        title_ele[count].click()
        time.sleep(1)
        # change to iframe to get content
        try:
            iframe = browser.find_element_by_id("wiz_doc_iframe")
        except NoSuchElementException:
            assert 0, "can't find frame"
        browser.switch_to.frame(iframe)
        content = browser.page_source
        #change pitcure address, add wiznode
        new_content = content.replace("src=\"", "src=\"https://note.wiz.cn")
        new_content = new_content.replace("img data-src", "img class=\" \" src")
        name = unicode(names[count]) + ".html"

        # some encode issue
        reload(sys)
        sys.setdefaultencoding("utf-8")
        f = file(path + floder_ + "\\" + name, "w+")
        f.write(new_content)
        f.close()

        # return to default frame
        count = count + 1
        browser.switch_to.default_content()
        time.sleep(1)

    else:
        print "No more articles"

browser = webdriver.Firefox()
browser.get("https://note.wiz.cn/login?p=login")  # Load page
# assert "WitzNote!" in browser.title
# elem = browser.find_element_by_name("p") # Find the query box
# elem.send_keys("seleniumhq" + Keys.RETURN)
time.sleep(0.2)  # Let the page load, will be added to the API

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
# submit
browser.find_element_by_id("loginbtn").click()
time.sleep(2)
# elements = browser.find_elements_by_class_name("doclist-noteinfo")
# print len(elements)
# for element in elements:
#    print element.text

browser.find_element_by_class_name("toolbar").click()
time.sleep(0.5)

folder_names = []
elements = browser.find_elements_by_class_name("level1")
length = len(elements)

# get folders name
for i in range(length / 3 - 3):
#    print elements[3 * i].text
    folder_names.append(elements[3 * i].text)

#read each folder, id begins with 2
for folder_id in range(2, 3):
                       #len(folder_names) + 2):
    button_id = "categoryTree_" + str(folder_id) + "_a"
    browser.find_element_by_id(button_id).click()
    time.sleep(1)

    elements = browser.find_elements_by_class_name("doclist-noteinfo")
    titles = []
    for element in elements:
        temp = element.text.split("\n")
        titles.append(temp[0].replace("/", " "))

    title_elements = browser.find_elements_by_class_name("list-item")

    #first folder
    folder_name = folder_names[folder_id - 2]
    print folder_name
    os.mkdir(path + folder_name )
    for article_id in range(len(title_elements)):
        save_article(folder_name, title_elements, titles, article_id)


browser.close()
