from selenium import webdriver
from page import BasePage
from enum import Enum
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from builtins import Exception
import time
import getpass
import logging

class FindType(Enum):
    id = By.ID
    xpath = By.XPATH
    link_text = By.LINK_TEXT
    partial_link_text = By.PARTIAL_LINK_TEXT
    name = By.NAME
    tag_name = By.TAG_NAME
    class_name = By.CLASS_NAME
    css_selector = By.CSS_SELECTOR


class ExpectedCondition(Enum):
    title_is = 'title_is'
    title_contains = 'title_contains'
    presence_of_element = 'presence_of_element'
    visibility_of_element = 'visibility_of_element'
    visibility_of = 'visibility_of'
    presence_of_all_elements = 'presence_of_all_elements'
    text_to_be_present_in_element = 'text_to_be_present_in_element'
    text_to_be_present_in_element_value = 'text_to_be_present_in_element_value'
    frame_to_be_available_and_switch_to_it = 'frame_to_be_available_and_switch_to_it'
    invisibility_of_element = 'invisibility_of_element'
    element_to_be_clickable = 'element_to_be_clickable'
    staleness_of = 'staleness_of'
    element_to_be_selected = 'element_to_be_selected'
    element_selection_state_to_be = 'element_selection_state_to_be'
    alert_is_present = 'alert_is_present'
    text_is = 'text_is'
    attribute_is = 'attribute_is'
    is_selected = 'is_selected'
    is_enabled = 'is_enabled'


class ActionType(Enum):
    click = 'click'
    click_and_hold = 'click_and_hold'
    context_click = 'context_click'
    double_click = 'double_click'
    # 暂未实现，不支持查找两个元素
    drag_and_drop = 'drag_and_drop'
    # 暂未实现，不支持查找两个元素
    drag_and_drop_by_offset = 'drag_and_drop_by_offset'
    key_down = 'key_down'
    key_up = 'key_up'
    move_by_offset = 'move_by_offset'
    move_to_element = 'move_to_element'
    move_to_element_with_offset = 'move_to_element_with_offset'
    release = 'release'
    send_keys = 'send_keys'
    send_keys_to_element = 'send_keys_to_element'


class Parse:
    @staticmethod
    def parse_case(page, case):
        find_type = case['find_type']
        find_value = case['find_value']
        expected_condition = case['expected_condition']
        expected_value = case['expected_value']
        action_type = case['action_type']
        action_value = case['action_value']

        element = Parse.find_type_parse(page, case, find_type, find_value)
        if not element:
            return None
        expected = Parse.expected_condition_parse(page, element, case, expected_condition, expected_value)
        if not expected:
            return None
        action_result = Parse.action_parse(page, element, case, action_type, action_value)
        if not action_result:
            return None
        if element and expected and action_result:
            case['is_match'] = 1

    @staticmethod
    def find_type_parse(page, case, find_type, find_value):
        if find_type:
            try:
                element = page.find_element(FindType[find_type].value, find_value)
                if not element:
                    case['is_match'] = 0
                    case['remark'] = '元素[ {}={} ] 未找到'.format(find_type, find_value)
                    return False
                return element
            except Exception as e:
                logging.error(e)
                case['is_match'] = 0
                case['remark'] = '元素[ {}={} ] 未找到'.format(find_type, find_value)
                return False
        return True
            
    @staticmethod
    def expected_condition_parse(page, element, case, expected_condition, expected_value):
        if expected_condition:
            try:
                if ExpectedCondition.title_is.value == expected_condition or ExpectedCondition.title_contains.value == expected_condition:
                    value = getattr(page, expected_condition)(expected_value)
                elif ExpectedCondition.presence_of_element.value == expected_condition or ExpectedCondition.visibility_of_element.value == expected_condition or ExpectedCondition.visibility_of.value == expected_condition or ExpectedCondition.presence_of_all_elements.value == expected_condition or ExpectedCondition.is_selected.value == expected_condition or ExpectedCondition.is_enabled.value == expected_condition or ExpectedCondition.frame_to_be_available_and_switch_to_it.value == expected_condition or ExpectedCondition.invisibility_of_element.value == expected_condition or ExpectedCondition.element_to_be_clickable.value == expected_condition or ExpectedCondition.staleness_of.value == expected_condition or ExpectedCondition.element_to_be_selected.value == expected_condition:
                    value = getattr(page, expected_condition)(element)
                elif ExpectedCondition.text_to_be_present_in_element.value == expected_condition or ExpectedCondition.text_to_be_present_in_element_value.value == expected_condition or ExpectedCondition.element_selection_state_to_be.value == expected_condition or ExpectedCondition.text_is.value == expected_condition:
                    value = getattr(page, expected_condition)(element, expected_value)
                elif ExpectedCondition.alert_is_present.value == expected_condition:
                    value = getattr(page, expected_condition)()
                elif ExpectedCondition.attribute_is.value == expected_condition:
                    _expected_value = expected_value.split('=')
                    value = getattr(page, expected_condition)(element, _expected_value[0], _expected_value[1])
                if not value:
                    case['is_match'] = 0
                    case['remark'] = '元素[ {} ], 验证[ {}={} ]失败'.format(element, expected_condition, expected_value)
                    return False
                return value
            except Exception as e:
                logging.error(e)
                case['is_match'] = 0
                case['remark'] = '元素[ {} ], 验证[ {}={} ]失败'.format(element, expected_condition, expected_value)
                return False
        return True

    @staticmethod
    def action_parse(page, element, case, action_type, action_value):
        def _parse_key(key_name):
            if key_name[0] == '`' and key_name[-1] == '`':
                return getattr(Keys, key_name)
            else:
                return key_name
            
        if not element:
            element = None
        if action_type:
            try:
                action_chain = ActionChains(page._driver)
                if ActionType.click.value == action_type or ActionType.click_and_hold.value == action_type or ActionType.context_click.value == action_type or ActionType.double_click.value == action_type or ActionType.move_to_element.value == action_type or ActionType.release.value == action_type:
                    getattr(action_chain, action_type)(element).perform()
                elif ActionType.send_keys.value == action_type:
                    keys_name = action_value.split(',')
                    keys = []
                    for key_name in keys_name:
                        keys.append(_parse_key(key_name))
                    getattr(action_chain, action_type)(*tuple(keys)).perform()
                elif ActionType.key_down.value == action_type or ActionType.key_up.value == action_type:
                    getattr(action_chain, action_type)(_parse_key(action_value), element).perform()
                elif ActionType.send_keys_to_element.value == action_type:
                    keys_name = action_value.split(',')
                    keys = []
                    for key_name in keys_name:
                        keys.append(_parse_key(key_name))
                    getattr(action_chain, action_type)(element, *tuple(keys)).perform()
                elif ActionType.move_by_offset.value == action_type:
                    _location = action_value.split(':')
                    getattr(action_chain, action_type)(_location[0], _location[1]).perform()
                elif ActionType.move_to_element_with_offset.value == action_type:
                    _location = action_value.split(':')
                    getattr(action_chain, action_type)(element, _location[0], _location[1]).perform()
            except Exception as e:
                logging.error(e)
                case['is_match'] = 0
                case['remark'] = '元素[ {} ], 动作[ {}={} ]失败'.format(element, action_type, action_value)
                return False
        return True
        
        
class Case:
    def __init__(self, driver=None):
        self._driver = driver

    def create_driver(self):
        self._driver = webdriver.Chrome()

    def run(self, dao, case_id):
        _case = dao.read_case(case_id)
        page = None
        for k in sorted(_case.keys()):
            step = _case[k]
            url = step['url']
            if url:
                page = BasePage(self._driver, url)
                page.open()
            Parse.parse_case(page, step)
            logging.warning(step)
            step['is_run'] = 1
            step['run_time'] = time.localtime()
            step['test_by'] = getpass.getuser()
            dao.update_case(step)
