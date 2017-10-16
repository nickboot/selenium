# coding:utf-8
# coding:cp936
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
class mouse():
    def mouse_id_click(self, broswer, element):
        broswer.find_element_by_id(element).click()

    #鼠标单击

    def mouse_xpath_click(self, broswer, element):
        broswer.find_element_by_xpath(element).click()

    # 鼠标悬浮
    def mouse_move_xpath(self, broswer, moveElement):
        move_element = broswer.find_element_by_xpath(moveElement)
        ActionChains(broswer).move_to_element(move_element).perform()

    # 输入内容
    def mouse_id_write(self, broswer, element, dirname):
        broswer.find_element_by_id(element).send_keys(dirname)