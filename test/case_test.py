import case
import case_dao
from selenium import webdriver


def run_test():
    c = case.Case(webdriver.Chrome())
    dao = case_dao.CaseDao()
    dao.creat_cursor(user='root', password='root', database='pis')
    c.run(dao, 1)

run_test()






