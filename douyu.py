# coding:utf-8
# coding:cp936

from selenium import webdriver
from time import sleep

browser = webdriver.Chrome()
url = "https://www.douyu.com/"
browser.get(url)
sleep(5)
print ("退出浏览器")
browser.quit()