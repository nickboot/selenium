# coding:utf-8
# coding:cp936

from selenium import webdriver
from time import sleep

browser = webdriver.Chrome()
browser.implicitly_wait(5)      #隐式等待
browser.set_window_size(1920, 1080)     #设置浏览器窗口大小
url = "https://www.douyu.com/"
browser.get(url)

browser.find_element_by_xpath('//*[@id="header"]/div/div/div[8]/a[1]').click()      #登录
"""
弹出框定位 iframe 内嵌框架定位 
browser.switch_to.frame(browser.find_element_by_id("Iframe元素位置通常通过id定位")) 
browser.switch_to.default_content()
"""
sleep(1)
browser.switch_to_frame(browser.find_element_by_id('login-passport-frame'))        #切换到iframe
sleep(1)
browser.find_element_by_xpath('//*[@id="loginbox"]/div[2]/div[2]/div[3]/div/span[2]').click()   #密码登录
"""
获取斗鱼窗口handle
"""
douyuWindow = browser.current_window_handle
browser.find_element_by_xpath('//*[@id="loginbox"]/div[3]/div[2]/div[2]/div[2]/a[1]').click()   #使用QQ登录
"""
使用QQ登录 会打开一个新网页
通过窗口handle切换,for循环判断切切换窗口
driver.switch_to.window(window_handle)  切换窗口
driver.current_window_handle        获取当前窗口handle
driver.window_handles            获取所有窗口handle
"""
"""
获取所有页面窗口handle
"""
allWindow = browser.window_handles
"""
for 循环判断 switch切换窗口
"""
for handle in allWindow:
    if handle != douyuWindow:
        browser.switch_to_window(handle)    #切换到QQ页面窗口
        sleep(1)
        browser.find_element_by_id("select_all").click()    #取消全选
        """
        iframe 切换
        """
        browser.switch_to.frame(browser.find_element_by_id("ptlogin_iframe"))
        sleep(3)
        browser.find_element_by_id("nick_2256395943").click()  # 点击QQ头像登录

sleep(10)
print ("退出浏览器")
browser.quit()