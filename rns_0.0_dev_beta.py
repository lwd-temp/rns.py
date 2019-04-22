#! /usr/bin/env python3
# Random Name Selector
# Python 3,Cross platform.
# Author:Sunset Shimmer
# You can use this script freely with the author's name in the script file.
# 随机姓名选择器
# 作者：余晖
# 请在代码文件中附带作者信息及相关注释即可自由使用。
# 姓名列表应位于工作目录下 namelist.txt 文件内，
# 每行一个姓名，不得空行，否则报错。
# 工作目录下会生成 RNSlog.txt 日志文件，
# 可用于调试。
# 此代码无保修且仅带有作者的最好祝愿，作者不为任何软件、硬件错误或损失及数据丢失负责。
# 请自行检查 Python 解释器是否携带病毒或恶意代码。
# 请自行检查此文件是否被篡改或传输不完整。
# 在发布之前把版本号改掉（下面）
version='Developer Beta Version'
print('Random Name Selector'+' '+version)
print('Author:LWD')
print('-----------------------')
print('[Info]Importing Modules')
import random
#import happybirthdayzwt
# Easter egg ;-)
#happybirthdayzwt.main()
import random
import datetime
print('[Success]Modules Imported')
# [配置 config]
print('[Info]Loading Config')
# Cheat:作弊设置，避免被抽取。1或0
cheat=1
# Yourname:与作弊配合使用，避免被抽取的内容。
yourname='余晖'
# Log:日志设置 1或0
log=1
# [配置结束 End of config]
print('[Success]Config Loaded')
print('[Info]Define Functions')
global count
count=0
global names
names=[]
def writelog(text):
    if log==1:
        with open('RNSlog.txt','a') as logfile:
            currtime=str(datetime.datetime.now())
            logfile.write(currtime+" LOG:"+str(text)+'\n')
writelog('Log Function Inited and the log starts')
writelog('RNS '+'Version '+version)
def getname():
    writelog('Get names')
    with open('namelist.txt','r') as list:
        global count
        global names
        names=[]
        count=0
        for name in list:
            namer=name.rstrip()
            count=count+1
            if namer=='':
                raise Exception('Empty line in the namelist.txt file.Line '+str(count))
            names.append(namer)
            writelog(namer+' '+str(count))
def getcount():
    print(count)
def getrand():
    number=random.randint(1,count)
    writelog('Get random number:'+str(number))
    return number
def getaname():
    number=getrand()
    aname=names[number-1:number]
    writelog('Get a name:'+str(aname))
    for theone in aname:
        therightone=theone
    return therightone
print('[Success]Functions defined')
print('-----------------------')
# 开始运行
print('开始抽取')
getname()
if cheat==1:
    writelog('Cheat Mode On!')
    nname=getaname()
    while nname==yourname:
        writelog("Got the Cheater's name.Try again.")
        nname=getaname()
else:
    nname=getaname()
print('结果：')
print(nname)
writelog('Output Finished')
print('完成')
writelog('Script Exit without any Error')
writelog('-----------------------------')
