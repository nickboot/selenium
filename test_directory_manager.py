# coding:utf-8
# coding:cp936
# 创建目录（默认情况）
from selenium import webdriver
from time import sleep
from Aclass_1014_login import login1014
from Aclass_mouse import mouse
from Aclass_directory_manager import directory_manager
from selenium.webdriver.common.action_chains import ActionChains
broswer = webdriver.Chrome()
listlogin = ["http://192.168.129.11", "admin", 12345678]
url, username, userpwd = listlogin
broswer.get(url)
broswer.maximize_window()
login1014().login(broswer, username, userpwd)
sleep(2)
listDir = ["cifsPublic", 16]
dirname , dirNum = listDir
directory_manager().mkdir_directory(broswer, dirname, dirNum)

