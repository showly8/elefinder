CREATE TABLE `web_test_case` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `case_id` varchar(32) NOT NULL,
  `url` varchar(1024) DEFAULT NULL,
  `find_type` enum('id','xpath','link_text','partial_link_text','name','tag_name','class_name','css_selector') DEFAULT NULL,
  `find_value` varchar(1024) DEFAULT NULL,
  `expected_condition` enum('title_is','title_contains','presence_of_element','visibility_of_element','visibility_of','presence_of_all_elements','text_to_be_present_in_element','text_to_be_present_in_element_value','frame_to_be_available_and_switch_to_it','invisibility_of_element','element_to_be_clickable','staleness_of','element_to_be_selected','element_selection_state_to_be','alert_is_present','text_is','attribute_is','is_selected','is_enabled') DEFAULT NULL,
  `expected_value` varchar(1024) DEFAULT NULL COMMENT '如果为“属性值”，填写“attr=value”；否则，直接填写',
  `action_type` enum('click','click_and_hold','context_click','double_click','drag_and_drop','drag_and_drop_by_offset','key_down','key_up','move_by_offset','move_to_element','move_to_element_with_offset','release','send_keys','send_keys_to_element','screenshot','submit','clear') DEFAULT NULL,
  `action_value` varchar(1024) DEFAULT NULL COMMENT '如果传的是按键，需要使用 ` 括起来：`key`；文字可以直接传值',
  `step` int(11) NOT NULL,
  `create_time` datetime DEFAULT NULL,
  `is_run` tinyint(4) NOT NULL DEFAULT '0',
  `run_time` datetime DEFAULT NULL,
  `is_match` tinyint(4) DEFAULT NULL,
  `test_by` varchar(16) DEFAULT NULL,
  `remark` varchar(1024) DEFAULT NULL,
  `is_delete` tinyint(4) NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

