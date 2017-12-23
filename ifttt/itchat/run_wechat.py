#coding=utf8

import os
import itchat

HELP_MSG = u'''\
欢迎使用微信物联网controller

帮助： 显示帮助

开始运动： 车辆开始运行

开始扫描: lidar开始扫描建图

开始取货: 开发中…
'''

## 开始运动
from lib.test_velo_ctl import run as run_velo_ctl
def run_rcc():
    run_velo_ctl()
    return u'脚本已运行'

## 开始扫描
def run_rviz_lidar():
    os.system('./bash/run_rviz_lidar.sh')
    return u'脚本已运行'

## 开始取货
def run_fetching():
    os.system('./bash/run_fetching.sh')
    return u'脚本已运行'


@itchat.msg_register(itchat.content.TEXT)
def bash_runner(msg):
    if msg['ToUserName'] != 'filehelper': return

    if msg['Text'] == u'开始运动':
        return_msg = run_rcc()
        itchat.send(return_msg, 'filehelper')

    if msg['Text'] == u'开始扫描':
        return_msg = run_rviz_lidar()
        itchat.send(return_msg, 'filehelper')

    if msg['Text'] == u'开始取货':
        return_msg = run_fetching()
        itchat.send(u'开发中…', 'filehelper')
        itchat.send(return_msg, 'filehelper')

    if msg['Text'] == u'帮助':
        itchat.send(HELP_MSG, 'filehelper')
    else:
        itchat.send(u'等待指令', 'filehelper')

if __name__ == "__main__":
    itchat.auto_login(True)
    itchat.send(HELP_MSG, 'filehelper')
    itchat.run()
