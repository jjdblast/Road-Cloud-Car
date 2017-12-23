#coding=utf8

import os

import itchat

HELP_MSG = u'''\

欢迎使用微信物联网

帮助： 显示帮助

开始： 运行脚本

'''

def run_bash():
    os.system('./run.sh')

@itchat.msg_register(itchat.content.TEXT)
def bash_runner(msg):
    if msg['ToUserName'] != 'filehelper': return
    if msg['Text'] == u'开始':
        run_bash()
        itchat.send(u'脚本已运行', 'filehelper')
    if msg['Text'] == u'帮助':
        itchat.send(HELP_MSG, 'filehelper')
    else:
        itchat.send(u'等待指令', 'filehelper')

if __name__ == "__main__":
    itchat.auto_login(True)
    itchat.send(HELP_MSG, 'filehelper')
    itchat.run()
