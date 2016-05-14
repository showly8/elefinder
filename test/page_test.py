from page import BasePage
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement

def title_is():
    page = BasePage(webdriver.Chrome(), 'http://mail.163.com')
    page.open()
    page.set_time_out(10)
    value = page.title_is('百度一下，你就知道')
    print(value)

title_is()


def title_contains_test():
    page = BasePage(webdriver.Chrome(), 'http://www.baidu.com')
    page.open()
    page.set_time_out(10)
    value = page.title_contains('百度一下')
    print(value)


def presence_of_element_located_test():
    page = BasePage(webdriver.Chrome(), 'http://www.baidu.com')
    page.open()
    page.set_time_out(10)
    value = page.presence_of_element_located((By.ID, 'kw'))
    print(value)


def visibility_of_element_located_test():
    page = BasePage(webdriver.Chrome(), 'http://www.baidu.com')
    page.open()
    page.set_time_out(10)
    value = page.presence_of_element_located((By.ID, 'kw'))
    print(value)


def visibility_of_test():
    page = BasePage(webdriver.Chrome(), 'http://www.baidu.com')
    page.open()
    page.set_time_out(10)
    element = page.find_element_by_name('rsv_idx')
    value = page.visibility_of(element)
    print(value)



def presence_of_all_elements_located_test():
    page = BasePage(webdriver.Chrome(), 'http://www.baidu.com')
    page.open()
    page.set_time_out(10)
    value = page.presence_of_all_elements_located((By.CSS_SELECTOR, 'a.mnav'))
    print(value)  # 返回元素，并不是true


def text_to_be_present_in_element_test():
    page = BasePage(webdriver.Chrome(), 'http://www.baidu.com')
    page.open()
    page.set_time_out(10)
    value = page.text_to_be_present_in_element((By.ID, 'lh'), '把百度设为主页')
    print(value)


def invisibility_of_element_located_test():
    page = BasePage(webdriver.Chrome(), 'http://www.baidu.com')
    page.open()
    page.set_time_out(10)
    element=page.find_element_by_id('kw')
    value = page.invisibility_of_element(element)
    print(value)

invisibility_of_element_located_test()

def element_to_be_clickable_test():
    page = BasePage(webdriver.Chrome(), 'http://www.baidu.com')
    page.open()
    page.set_time_out(10)
    value = page.element_to_be_clickable((By.ID, 'cp'))
    print(value)  # ?


def staleness_of_test():
    page = BasePage(webdriver.Chrome(), 'http://www.baidu.com')
    page.open()
    page.set_time_out(10)
    element = page.find_element_by_id('kw')
    value = page.staleness_of(element)
    print(value)  # TimeoutException


def element_to_be_selected_test():
    page = BasePage(webdriver.Chrome(), 'http://www.hao123.com')
    page.open()
    page.set_time_out(10)
    element = page.find_element_by_class_name('tab-curr')
    value = page.element_to_be_selected(element)
    print(value)  # TimeoutException


def element_located_to_be_selected_test():
    page = BasePage(webdriver.Chrome(), 'http://www.baidu.com')
    page.open()
    page.set_time_out(10)
    value = page.element_located_to_be_selected((By.ID, 'cp'))
    print(value)  # TimeoutException


def element_selection_state_to_be_test():
    page = BasePage(webdriver.Chrome(), 'http://www.hao123.com')
    page.open()
    page.set_time_out(10)
    element = page.find_element_by_class_name('tab-curr')
    value = page.element_selection_state_to_be(element)
    print(value)

def element_located_selection_state_to_be_test():
    page = BasePage(webdriver.Chrome(), 'http://www.baidu.com')
    page.open()
    page.set_time_out(10)
    value = page.element_located_selection_state_to_be((By.ID, 'cp'))
    print(value)


#########################################################################
def find_element_by_id_test():
    page = BasePage(webdriver.Chrome(), 'http://www.baidu.com')
    page.open()
    page.set_time_out(10)
    element = page.find_element_by_id('kw')
    print(element)


def find_element_by_name_test():
    page = BasePage(webdriver.Chrome(), 'http://www.baidu.com')
    page.open()
    page.set_time_out(10)
    element = page.find_element_by_name('tj_trnuomi')
    print(element)


def find_element_by_xpath_test():
    page = BasePage(webdriver.Chrome(), 'http://www.baidu.com')
    page.open()
    page.set_time_out(10)
    element = page.find_element_by_xpath('//a[@class="mnav"]')
    print(element)


def find_element_by_link_text_test():
    page = BasePage(webdriver.Chrome(), 'http://www.baidu.com')
    page.open()
    page.set_time_out(60)
    element = page.find_element_by_link_text('新闻')
    print(element)


def find_element_by_partial_link_text_test():
    page = BasePage(webdriver.Chrome(), 'http://www.baidu.com')
    page.open()
    page.set_time_out(30)
    element = page.find_element_by_partial_link_text('hao123')
    print(element)


def find_element_by_tag_name_test():
    page = BasePage(webdriver.Chrome(), 'http://www.baidu.com')
    page.open()
    page.set_time_out(10)
    element = page.find_element_by_tag_name('img')
    print(element)


def find_element_by_class_name_test():
    page = BasePage(webdriver.Chrome(), 'http://www.baidu.com')
    page.open()
    page.set_time_out(10)
    element = page.find_element_by_class_name('s_ipt')
    print(element)


def find_element_by_css_selector_test():
    page = BasePage(webdriver.Chrome(), 'http://www.baidu.com')
    page.open()
    page.set_time_out(20)
    element = page.find_element_by_css_selector('a.mnav')
    print(element)


def find_elements_by_id_test():
    page = BasePage(webdriver.Chrome(), 'http://www.baidu.com')
    page.open()
    page.set_time_out(10)
    element = page.find_elements_by_id('kw')
    print(element)


def find_elements_by_name_test():
    page = BasePage(webdriver.Chrome(), 'http://www.baidu.com')
    page.open()
    page.set_time_out(10)
    element = page.find_elements_by_name('tj_trnuomi')
    print(element)


def find_elements_by_xpath_test():
    page = BasePage(webdriver.Chrome(), 'http://www.baidu.com')
    page.open()
    page.set_time_out(10)
    element = page.find_elements_by_xpath('//a[@class="mnav"]')
    print(element)


def find_elements_by_link_text_test():
    page = BasePage(webdriver.Chrome(), 'http://www.baidu.com')
    page.open()
    page.set_time_out(60)
    element = page.find_elements_by_link_text('新闻')
    print(element)


def find_elements_by_partial_link_text_test():
    page = BasePage(webdriver.Chrome(), 'http://www.baidu.com')
    page.open()
    page.set_time_out(30)
    element = page.find_elements_by_partial_link_text('hao123')
    print(element)


def find_elements_by_tag_name_test():
    page = BasePage(webdriver.Chrome(), 'http://www.baidu.com')
    page.open()
    page.set_time_out(10)
    element = page.find_elements_by_tag_name('head111')
    print(element)


def find_elements_by_class_name_test():
    page = BasePage(webdriver.Chrome(), 'http://www.baidu.com')
    page.open()
    page.set_time_out(10)
    element = page.find_elements_by_class_name('s_ipt')
    print(element)


def find_elements_by_css_selector_test():
    page = BasePage(webdriver.Chrome(), 'http://www.baidu.com')
    page.open()
    page.set_time_out(20)
    element = page.find_elements_by_css_selector('a.mnav')
    print(element)
