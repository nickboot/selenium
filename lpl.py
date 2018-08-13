# coding:utf-8
# coding:cp936
from selenium import webdriver
from time import sleep

browser = webdriver.Chrome()    #调用谷歌浏览器
#options = webdriver.ChromeOptions()    #调用谷歌浏览器设置
#options.add_argument("--start-maximized")  # 启动时最大化，Mac不能最大化
#options.add_argument("--kiosk")         # 启用kiosk模式。（一种类似于全屏的浏览模式）
#browser = webdriver.Chrome(chrome_options = options)
url = "http://lpl.qq.com"
browser.get(url)
#browser.maximize_window()       #浏览器窗口最大化
browser.set_window_size(1920, 1080)
browser.implicitly_wait(30)     #隐式等待30s
sleep(5)
print ("退出浏览器")
browser.quit()