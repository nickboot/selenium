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
browser.implicitly_wait(10)     #隐式等待30s
sleep(1)
browser.find_element_by_xpath('//*[@id="unlogin"]/a').click()      #登录
"""
弹出框 iframe 切换
browser.switch_to.frame(browser.find_element_by_id("loginIframe")) 
browser.switch_to.default_content()
"""
browser.switch_to.frame(browser.find_element_by_id("loginIframe"))      #切换到QQ登录页面
#browser.find_element_by_id("nick_2256395943").click()           #点击QQ昵称
browser.find_element_by_id("img_out_2256395943").click()        #点击QQ头像

sleep(10)
print ("退出浏览器")
browser.quit()