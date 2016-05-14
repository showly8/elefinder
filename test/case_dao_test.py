import case_dao


def read_case_test():
    dao = case_dao.CaseDao()
    dao.creat_cursor(user='root', password='root', database='test_database')
    case = dao.read_case(1)
    print(case)


read_case_test()
