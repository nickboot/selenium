# coding:utf-8
# coding:cp936
from time import sleep
class login1014():
    def login(self, broswer, username, userpwd):
        broswer.find_element_by_id("loguserName").clear()
        broswer.find_element_by_id("loguserName").send_keys(username)
        sleep(0.1)
        broswer.find_element_by_id("loguserPwd").clear()
        broswer.find_element_by_id("loguserPwd").send_keys(userpwd)
        sleep(0.1)
        broswer.find_element_by_id("btnLogin").click()