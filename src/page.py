from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchFrameException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import NoAlertPresentException


class BasePage:
    def __init__(self, driver, url, parent=None):
        self._driver = driver
        self._url = url
        self._parent = parent
        self._time_out = 10
        self._by = By.ID
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

    def element_finder(self, driver):
        element = self._driver.find_element(self._by, self._target)
        return element if element else False

    def elements_finder(self, driver):
        element = self._driver.find_elements(self._by, self._target)
        return element if element else False

    def find_element_by_id(self, element_id):
        self._by = By.ID
        self._target = element_id
        element = WebDriverWait(self._driver, self._time_out).until(self.element_finder)
        return element

    def find_element_by_name(self, element_name):
        self._by = By.NAME
        self._target = element_name
        element = WebDriverWait(self._driver, self._time_out).until(self.element_finder)
        return element

    def find_element_by_xpath(self, xpath):
        self._by = By.XPATH
        self._target = xpath
        element = WebDriverWait(self._driver, self._time_out).until(self.element_finder)
        return element

    def find_element_by_link_text(self, link_text):
        self._by = By.LINK_TEXT
        self._target = link_text
        element = WebDriverWait(self._driver, self._time_out).until(self.element_finder)
        return element

    def find_element_by_partial_link_text(self, partial_link_text):
        self._by = By.PARTIAL_LINK_TEXT
        self._target = partial_link_text
        element = WebDriverWait(self._driver, self._time_out).until(self.element_finder)
        return element

    def find_element_by_tag_name(self, tag_name):
        self._by = By.TAG_NAME
        self._target = tag_name
        element = WebDriverWait(self._driver, self._time_out).until(self.element_finder)
        return element

    def find_element_by_class_name(self, class_name):
        self._by = By.CLASS_NAME
        self._target = class_name
        element = WebDriverWait(self._driver, self._time_out).until(self.element_finder)
        return element

    def find_element_by_css_selector(self, css_selector):
        self._by = By.CSS_SELECTOR
        self._target = css_selector
        element = WebDriverWait(self._driver, self._time_out).until(self.element_finder)
        return element

    def find_elements_by_id(self, element_id):
        self._by = By.ID
        self._target = element_id
        element = WebDriverWait(self._driver, self._time_out).until(self.elements_finder)
        return element

    def find_elements_by_name(self, element_name):
        self._by = By.NAME
        self._target = element_name
        element = WebDriverWait(self._driver, self._time_out).until(self.elements_finder)
        return element

    def find_elements_by_xpath(self, xpath):
        self._by = By.XPATH
        self._target = xpath
        element = WebDriverWait(self._driver, self._time_out).until(self.elements_finder)
        return element

    def find_elements_by_link_text(self, link_text):
        self._by = By.LINK_TEXT
        self._target = link_text
        element = WebDriverWait(self._driver, self._time_out).until(self.elements_finder)
        return element

    def find_elements_by_partial_link_text(self, partial_link_text):
        self._by = By.PARTIAL_LINK_TEXT
        self._target = partial_link_text
        element = WebDriverWait(self._driver, self._time_out).until(self.elements_finder)
        return element

    def find_elements_by_tag_name(self, tag_name):
        self._by = By.TAG_NAME
        self._target = tag_name
        element = WebDriverWait(self._driver, self._time_out).until(self.elements_finder)
        return element

    def find_elements_by_class_name(self, class_name):
        self._by = By.CLASS_NAME
        self._target = class_name
        element = WebDriverWait(self._driver, self._time_out).until(self.elements_finder)
        return element

    def find_elements_by_css_selector(self, css_selector):
        self._by = By.CSS_SELECTOR
        self._target = css_selector
        element = WebDriverWait(self._driver, self._time_out).until(self.elements_finder)
        return element

    def find_element(self, by, value=None):
        self._by = by
        self._target = value
        element = WebDriverWait(self._driver, self._time_out).until(self.element_finder)
        return element

    def find_elements(self, by, value=None):
        self._by = by
        self._target = value
        element = WebDriverWait(self._driver, self._time_out).until(self.elements_finder)
        return element

    def title_is(self, title):
        return self.get_title() == title

    def title_contains(self, title):
        return title in self.get_title()

    def presence_of_element(self, element):
        return element if element else False

    def visibility_of_element(self, element):
        return element if element.is_displayed() == True else False

    def visibility_of(self, element):
        return element if element.is_displayed() == True else False

    def presence_of_all_elements(self, elements):
        for element in elements:
            if not element:
                return False
        return elements

    def text_to_be_present_in_element(self, element, text):
        return text in element.text

    def text_to_be_present_in_element_value(self, element, text):
        return text in element.get_attribute("value")

    def frame_to_be_available_and_switch_to_it(self, element):
        try:
            self._driver.switch_to.frame(element)
            return True
        except NoSuchFrameException:
            return False

    def invisibility_of_element(self, element):
        if not element:
            return True
        return element if element.is_displayed() == False else False

    def element_to_be_clickable(self, element):
        element = self.visibility_of_element(element)(self._driver)
        if element and element.is_enabled():
            return element
        else:
            return False

    def staleness_of(self, element):
        try:
            element.is_enabled()
            return False
        except StaleElementReferenceException:
            return True

    def element_to_be_selected(self, element):
        return element.is_selected()

    def element_selection_state_to_be(self, element, is_selected):
        return element.is_selected() == is_selected

    def alert_is_present(self):
        try:
            alert = self._driver.switch_to.alert
            alert.text
            return alert
        except NoAlertPresentException:
            return False

    def text_is(self, element, text):
        return element.text == text

    def attribute_is(self, element, attribute, value):
        return element.get_attribute(attribute) == value

    def is_selected(self, element):
        return element.is_selected()

    def is_enabled(self, element):
        return element.is_enabled()

    def screenshot(self, element, filename):
        if element.screenshot(filename):
            return filename
        else:
            return False

    def submit(self, element):
        element.submit()

    def clear(self, element):
        element.clear()
