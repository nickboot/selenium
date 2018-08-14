# coding:utf-8
# coding:cp936

from selenium import webdriver
from time import sleep

browser = webdriver.Chrome()
browser.implicitly_wait(10)      #隐式等待
browser.set_window_size(1920, 1080)     #设置浏览器窗口大小
url = "https://www.douyu.com/"
browser.get(url)

browser.find_element_by_xpath('//*[@id="header"]/div/div/div[8]/a[1]').click()      #登录
"""
弹出框定位 iframe 内嵌框架定位 
browser.switch_to.frame(browser.find_element_by_id("Iframe元素位置通常通过id定位")) 
browser.switch_to.default_content()
"""
sleep(2)
browser.switch_to_frame(browser.find_element_by_id('login-passport-frame'))        #切换到iframe
sleep(2)
browser.find_element_by_xpath('//*[@id="loginbox"]/div[2]/div[2]/div[3]/div/span[2]').click()   #密码登录
"""
获取斗鱼窗口handle
"""
douyuWindow = browser.current_window_handle
browser.find_element_by_xpath('//*[@id="loginbox"]/div[3]/div[2]/div[2]/div[2]/a[1]').click()   #使用QQ登录

browser.close()    #关闭斗鱼标签页

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

sleep(2)
browser.find_element_by_id("suggest-search").click()        #搜索主播
browser.find_element_by_id("suggest-search").clear()        #清除输入框
sleep(1)
browser.find_element_by_id("suggest-search").send_keys("英雄联盟官方赛事")      #输入搜索内容
sleep(1)
searchWindow = browser.current_window_handle
browser.find_element_by_xpath('//*[@id="header"]/div/div/div[2]/a/i').click()   #点击搜索按钮

browser.close()    #关闭搜索标签页
"""
窗口切换 window切换
"""
totalWindow = browser.window_handles
for romHandle in totalWindow:
    if romHandle != douyuWindow and romHandle != searchWindow:      #切换窗口
        browser.switch_to_window(romHandle)
        sleep(1)
        browser.find_element_by_xpath('//*[@id="mainbody"]/div/div[1]/div/a[2]/span').click()     #主播

        roomWindow = browser.current_window_handle

        browser.find_element_by_xpath('//*[@id="mainbody"]/div[1]/div[2]/ul/li[1]/a/div[1]/img').click()   #进入直播间
        sleep(1)
        Window4 = browser.window_handles

        browser.close()     #关闭主播标签页
        for Handle4 in Window4:
            if Handle4 != douyuWindow and Handle4 != searchWindow and Handle4 != roomWindow:  # 切换窗口
                browser.switch_to_window(Handle4)



                sleep(3)
                browser.find_element_by_xpath('//*[@id="js-send-msg"]/textarea').click()    #定位到弹幕输入框
                sleep(1)
                num = 10
                while num > 0:
                    browser.find_element_by_xpath('//*[@id="js-send-msg"]/textarea').send_keys("RNG加油")       #填写弹幕内容
                    sleep(5)
                    browser.find_element_by_xpath('//*[@id="js-send-msg"]/div[1]').click()    #发送

                    browser.find_element_by_xpath('//*[@id="js-send-msg"]/textarea').send_keys("LPL加油")  # 填写弹幕内容
                    sleep(5)
                    browser.find_element_by_xpath('//*[@id="js-send-msg"]/div[1]').click()  # 发送

                    browser.find_element_by_xpath('//*[@id="js-send-msg"]/textarea').send_keys("7777777")  # 填写弹幕内容
                    sleep(5)
                    browser.find_element_by_xpath('//*[@id="js-send-msg"]/div[1]').click()  # 发送
                    num = num - 1

sleep(20)
print ("退出浏览器")
#browser.quit()