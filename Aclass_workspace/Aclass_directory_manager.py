# coding:utf-8
# coding:cp936
from time import sleep
from Aclass_mouse import mouse
class directory_manager():
    def mkdir_directory(self, broswer, dirname , dirNum):
        mouse().mouse_move_xpath(broswer, '//*[@id="gx"]/a')                                # 文件共享
        mouse().mouse_xpath_click(broswer, '/html/body/table[1]/tbody/tr/td[5]/ul/li[1]/a')             # 目录管理
        # mouse().mouse_id_click(broswer, 'btnCreate')                                        # 新建
        dirnameList = []
        for dirnameA in range(11, dirNum):
            dir = dirname + str(dirnameA)
            dirnameList.append(dir)
        for dirnameL in dirnameList:
            mouse().mouse_id_click(broswer, 'btnCreate')
            mouse().mouse_id_write(broswer, 'name', dirnameL)
            mouse().mouse_id_click(broswer, 'confirm')
            sleep(1)




