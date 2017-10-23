# coding:utf-8
# coding:cp936
from selenium import webdriver
from PIL import Image

broswer = webdriver.Chrome()
broswer.get("http://www.baidu.com")
broswer.save_screenshot(r'E:\ph.png')
baidu = broswer.find_element_by_id('su')
left = baidu.location['x']
top = baidu.location['y']
elementWidth = baidu.location['x'] + baidu.size['width']
elementHeight = baidu.location['y'] + baidu.size['height']
picture = Image.open(r'E:\ph.png')
picture = picture.crop((left, top, elementWidth, elementHeight))
picture.save(r'E:\ph2.png')