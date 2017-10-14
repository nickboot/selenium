# coding:utf-8
# coding:cp936
from selenium import webdriver
from time import sleep
from Aclass_login_1014 import login1014
broswer = webdriver.Chrome()
listlogin = ["http://192.168.129.38", "admin", 12345678]
url , username, userpwd = listlogin
# url = "http://192.168.129.11"
broswer.get(url)
broswer.maximize_window()
login1014().login(broswer, username, userpwd)