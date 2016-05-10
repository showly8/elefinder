from selenium.webdriver.support.ui import WebDriverWait


class BasePage:
    def __init__(self, driver, url, parent=None):
        self._driver = driver
        self._url = url
        self._parent = parent
        self._time_out = 10
        self._locating_function = None
        self._target = None

    def set_time_out(self, seconds):
        self._time_out = seconds

    def set_url(self, url):
        self._url = url

    def get_url(self):
        return self._url

    def get_title(self):
        return self._driver.title()

    def open(self):
        self._driver.get(self._url)

    def find(self, driver):
        if not self._locating_function:
            raise Exception('定位函数不能为空')
        if not self._target:
            raise Exception('查找目标不能为空')
        element = self._locating_function(self._target)
        if isinstance(element, list):
            if len(element) > 0:
                return element
            else:
                print('没有任何元素被找到')
                return False
        if not element.is_displayed():
            print('没有元素被找到')
            return False
        return element

    def find_element_by_id(self, element_id):
        self._locating_function = self._driver.find_element_by_id
        self._target = element_id
        element = WebDriverWait(self._driver, self._time_out).until(self.find)
        return element

    def find_element_by_name(self, element_name):
        self._locating_function = self._driver.find_element_by_name
        self._target = element_name
        element = WebDriverWait(self._driver, self._time_out).until(self.find)
        return element

    def find_element_by_xpath(self, xpath):
        self._locating_function = self._driver.find_element_by_xpath
        self._target = xpath
        element = WebDriverWait(self._driver, self._time_out).until(self.find)
        return element

    def find_element_by_link_text(self, link_text):
        self._locating_function = self._driver.find_element_by_link_text
        self._target = link_text
        element = WebDriverWait(self._driver, self._time_out).until(self.find)
        return element

    def find_element_by_partial_link_text(self, partial_link_text):
        self._locating_function = self._driver.find_element_by_partial_link_text
        self._target = partial_link_text
        element = WebDriverWait(self._driver, self._time_out).until(self.find)
        return element

    def find_element_by_tag_name(self, tag_name):
        self._locating_function = self._driver.find_element_by_tag_name
        self._target = tag_name
        element = WebDriverWait(self._driver, self._time_out).until(self.find)
        return element

    def find_element_by_class_name(self, class_name):
        self._locating_function = self._driver.find_element_by_class_name
        self._target = class_name
        element = WebDriverWait(self._driver, self._time_out).until(self.find)
        return element

    def find_element_by_css_selector(self, css_selector):
        self._locating_function = self._driver.find_element_by_css_selector
        self._target = css_selector
        element = WebDriverWait(self._driver, self._time_out).until(self.find)
        return element

    def find_elements_by_id(self, element_id):
        self._locating_function = self._driver.find_elements_by_id
        self._target = element_id
        element = WebDriverWait(self._driver, self._time_out).until(self.find)
        return element

    def find_elements_by_name(self, element_name):
        self._locating_function = self._driver.find_elements_by_name
        self._target = element_name
        element = WebDriverWait(self._driver, self._time_out).until(self.find)
        return element

    def find_elements_by_xpath(self, xpath):
        self._locating_function = self._driver.find_elements_by_xpath
        self._target = xpath
        element = WebDriverWait(self._driver, self._time_out).until(self.find)
        return element

    def find_elements_by_link_text(self, link_text):
        self._locating_function = self._driver.find_elements_by_link_text
        self._target = link_text
        element = WebDriverWait(self._driver, self._time_out).until(self.find)
        return element

    def find_elements_by_partial_link_text(self, partial_link_text):
        self._locating_function = self._driver.find_elements_by_partial_link_text
        self._target = partial_link_text
        element = WebDriverWait(self._driver, self._time_out).until(self.find)
        return element

    def find_elements_by_tag_name(self, tag_name):
        self._locating_function = self._driver.find_elements_by_tag_name
        self._target = tag_name
        element = WebDriverWait(self._driver, self._time_out).until(self.find)
        return element

    def find_elements_by_class_name(self, class_name):
        self._locating_function = self._driver.find_elements_by_class_name
        self._target = class_name
        element = WebDriverWait(self._driver, self._time_out).until(self.find)
        return element

    def find_elements_by_css_selector(self, css_selector):
        self._locating_function = self._driver.find_elements_by_css_selector
        self._target = css_selector
        element = WebDriverWait(self._driver, self._time_out).until(self.find)
        return element
