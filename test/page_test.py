from page import BasePage
from selenium import webdriver
from time import sleep





def find_element_by_id_test():
    page = BasePage(webdriver.Chrome(), 'http://www.baidu.com')
    page.open()
    page.set_time_out(10)
    element = page.find_element_by_id('kw')
    print(element)

find_element_by_id_test()

# def find_element_by_name_test():
#     page = BasePage(webdriver.Chrome(), 'http://www.baidu.com')
#     page.open()
#     page.set_time_out(10)
#     element = page.find_element_by_name('tj_trnuomi')
#     print(element)


# def find_element_by_xpath_test():
#     page = BasePage(webdriver.Chrome(), 'http://www.baidu.com')
#     page.open()
#     page.set_time_out(10)
#     element = page.find_element_by_xpath('//a[@class="mnav"]')
#     print(element)



# def find_element_by_link_text_test():
#     page = BasePage(webdriver.Chrome(), 'http://www.baidu.com')
#     page.open()
#     page.set_time_out(60)
#     element = page.find_element_by_link_text('新闻')
#     print(element)



# def find_element_by_partial_link_text_test():
#     page = BasePage(webdriver.Chrome(), 'http://www.baidu.com')
#     page.open()
#     page.set_time_out(30)
#     element = page.find_element_by_partial_link_text('hao123')
#     print(element)



# def find_element_by_tag_name_test():
#     page = BasePage(webdriver.Chrome(), 'http://www.baidu.com')
#     page.open()
#     page.set_time_out(10)
#     element = page.find_element_by_tag_name('img')
#     print(element)




# def find_element_by_class_name_test():
#     page = BasePage(webdriver.Chrome(), 'http://www.baidu.com')
#     page.open()
#     page.set_time_out(10)
#     element = page.find_element_by_class_name('s_ipt')
#     print(element)




# def find_element_by_css_selector_test():
#     page = BasePage(webdriver.Chrome(), 'http://www.baidu.com')
#     page.open()
#     page.set_time_out(20)
#     element = page.find_element_by_css_selector('a.mnav')
#     print(element)




# def find_elements_by_id_test():
#     page = BasePage(webdriver.Chrome(), 'http://www.baidu.com')
#     page.open()
#     page.set_time_out(10)
#     element = page.find_elements_by_id('kw')
#     print(element)

# def find_elements_by_name_test():
#     page = BasePage(webdriver.Chrome(), 'http://www.baidu.com')
#     page.open()
#     page.set_time_out(10)
#     element = page.find_elements_by_name('tj_trnuomi')
#     print(element)



# def find_elements_by_xpath_test():
#     page = BasePage(webdriver.Chrome(), 'http://www.baidu.com')
#     page.open()
#     page.set_time_out(10)
#     element = page.find_elements_by_xpath('//a[@class="mnav"]')
#     print(element)



# def find_elements_by_link_text_test():
#     page = BasePage(webdriver.Chrome(), 'http://www.baidu.com')
#     page.open()
#     page.set_time_out(60)
#     element = page.find_elements_by_link_text('新闻')
#     print(element)


# def find_elements_by_partial_link_text_test():
#     page = BasePage(webdriver.Chrome(), 'http://www.baidu.com')
#     page.open()
#     page.set_time_out(30)
#     element = page.find_elements_by_partial_link_text('hao123')
#     print(element)


#
# def find_elements_by_tag_name_test():
#     page = BasePage(webdriver.Chrome(), 'http://www.baidu.com')
#     page.open()
#     page.set_time_out(10)
#     element = page.find_elements_by_tag_name('head')
#     print(element)
#
#
# def find_elements_by_class_name_test():
#     page = BasePage(webdriver.Chrome(), 'http://www.baidu.com')
#     page.open()
#     page.set_time_out(10)
#     element = page.find_elements_by_class_name('s_ipt')
#     print(element)
#
#
# def find_elements_by_css_selector_test():
#     page = BasePage(webdriver.Chrome(), 'http://www.baidu.com')
#     page.open()
#     page.set_time_out(20)
#     element = page.find_elements_by_css_selector('a.mnav')
#     print(element)
