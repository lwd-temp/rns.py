#! /usr/bin/env python3
# Random Name Selector
# Python 3,Cross platform.
# Author:LWD(Sunset Shimmer)
# You can use this script freely with the author's name in the script file.
# 随机姓名选择器
# 作者：LWD（余晖）
# 请在代码文件中附带作者信息及相关注释即可自由使用。
# 姓名列表应位于工作目录下 namelist.txt 文件内，
# 每行一个姓名，不得空行，否则报错。
# 工作目录下会生成 RNSlog.txt 日志文件，
# 可用于调试。
# 此代码无保修且仅带有作者的最好祝愿，作者不为任何软件、硬件错误或损失及数据丢失负责。
# 请自行检查 Python 解释器是否携带病毒或恶意代码。
# 请自行检查此文件是否被篡改或传输不完整。
# Changelog 更新日志
# 0.1 本地化完成
# 0.0 首个版本 完成基本逻辑
version='0.1开发者测试版'
print('随机姓名选择器'+' '+version)
print('作者：余晖')
print('-----------------------')
print('[信息]导入库')
import random
import random
import datetime
print('[成功]库导入完成')
# [配置 config]
print('[信息]加载配置')
# Cheat:作弊设置，避免被抽取。1或0
cheat=1
# Yourname:与作弊配合使用，避免被抽取的内容。
yourname='余晖'
# Log:日志设置 1或0
log=1
# Egg:彩蛋设置
egg=0
# [配置结束 End of config]
print('[成功]配置加载完成')
print('[信息]定义函数')
global count
count=0
global names
names=[]
def writelog(text):
    if log==1:
        with open('RNSlog.txt','a') as logfile:
            currtime=str(datetime.datetime.now())
            logfile.write(currtime+" 日志："+str(text)+'\n')
writelog('日志函数定义，开始记录。')
writelog('RNS '+'版本 '+version)
# HappyBirthdayZWT
# Author:LWD
# This code is used as an Easter Egg.
def zwt():
    date=datetime.datetime.today()
    if str(date.month)=="4":
        if int(date.day)>=20:
            print("Happy birthday ZWT!")
    if str(date.month)=="5":
        if str(date.day)=="5":
            count=0
            while count!=4:
                print("Happy birthday ZWT!")
                count=count+1
        if int(date.day)<=15:
            print("Happy birthday ZWT!")
def getname():
    writelog('获取姓名列表')
    with open('namelist.txt','r') as list:
        global count
        global names
        names=[]
        count=0
        for name in list:
            namer=name.rstrip()
            count=count+1
            if namer=='':
                writelog('在 namelist.txt 文件中出现空行。行 '+str(count))
                raise Exception('Empty line in the namelist.txt file.Line '+str(count))
            names.append(namer)
            writelog(namer+' '+str(count))
def getcount():
    print(count)
def getrand():
    number=random.randint(1,count)
    writelog('获取随机数：'+str(number))
    return number
def getaname():
    number=getrand()
    aname=names[number-1:number]
    writelog('获取姓名：'+str(aname))
    for theone in aname:
        therightone=theone
    return therightone
print('[成功]定义函数完成')
if egg==1:
    writelog("彩蛋开启。")
    zwt()
print('-----------------------')
# 开始运行
while True:
    print('开始抽取')
    getname()
    if cheat==1:
        writelog('作弊已启动！')
        nname=getaname()
        while nname==yourname:
            writelog("获取作弊者姓名，重试。")
            nname=getaname()
    else:
        nname=getaname()
    print('结果：')
    print(nname)
    writelog('输出完成。')
    print('完成')
    input("按Enter继续")
    