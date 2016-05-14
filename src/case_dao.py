import mysql.connector


class CaseDao:
    def __init__(self, connector=None):
        self._conn = connector
        self._cursor = None

    def creat_cursor(self, user, password, database, host='127.0.0.1', port=3306):
        self._conn = mysql.connector.connect(user=user, password=password, database=database, host=host, port=port)
        self._cursor = self._conn.cursor()

    def read_case(self, case_id):
        query = ('''SELECT
                      `id`,
                      `case_id`,
                      `url`,
                      `find_type`,
                      `find_value`,
                      `expected_condition`,
                      `expected_value`,
                      `action_type`,
                      `action_value`,
                      `step`,
                      `create_time`,
                      `is_run`,
                      `run_time`,
                      `is_match`,
                      `test_by`,
                      `remark`
                    FROM
                      `web_test_case`
                    WHERE is_delete = 0
                      AND is_run = 0
                      AND case_id = %s ''')
        self._cursor.execute(query, (case_id,))
        case = {}
        for (id, case_id, url, find_type, find_value, expected_condition, expected_value, action_type,
             action_value, step, create_time, is_run, run_time, is_match, test_by, remark) in self._cursor:
            step_context = {}
            step_context['id'] = id
            step_context['case_id'] = case_id
            step_context['url'] = url
            step_context['find_type'] = find_type
            step_context['find_value'] = find_value
            step_context['expected_condition'] = expected_condition
            step_context['expected_value'] = expected_value
            step_context['action_type'] = action_type
            step_context['action_value'] = action_value
            step_context['step'] = step
            step_context['create_time'] = create_time
            step_context['is_run'] = is_run
            step_context['run_time'] = run_time
            step_context['is_match'] = is_match
            step_context['test_by'] = test_by
            step_context['remark'] = remark
            case[step] = step_context
        return case

    def update_case(self, case):
        update = ('''UPDATE web_test_case
                    SET is_run = %s,
                     run_time = %s,
                     is_match = %s,
                     test_by = %s,
                     remark = %s
                    WHERE id = %s''')
        self._cursor.execute(update, (case['is_run'], case['run_time'], case['is_match'], case['test_by'], case['remark'], case['id']))
        self._conn.commit()
