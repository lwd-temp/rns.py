#! /usr/bin/env python3
# 随机姓名选择器
# 作者：李一一
# 此代码仅用于汉东省青少年科技创新大赛，不得用于其他用途。
# 使用说明：
# 姓名列表应位于工作目录下 namelist.txt 文件内，
# 每行一个姓名，不得空行，否则报错。
# 工作目录下会生成 RNSlog.txt 日志文件，
# 可用于调试。
readableversion='0.1稳定版，仅用于汉东省青少年科技创新大赛'
version='0.1_stable_competition'
if __name__=='__main__':
    print('随机姓名选择器'+' '+readableversion)
    print('作者：李一一')
    print('-----------------------')
    print('[信息]导入库')
import datetime
import random

if __name__=='__main__':
    print('[成功]库导入完成')
# [配置 config]
if __name__=='__main__':
    print('[信息]加载配置')
# Cheat:作弊设置，避免被抽取。1或0
cheat=0
# Yourname:与作弊配合使用，避免被抽取的内容。
yourname='避免抽取'
# Log:日志设置 1或0
log=1
# Refresh 是否在重新抽取时重读列表 1或0
refresh=0
# [配置结束 End of config]
if __name__=='__main__':
    print('[成功]配置加载完成')
    print('[信息]定义函数')
global count
count=0
global names
names=[]
# 日志函数，参数为日志内容，自动添加时间。
def writelog(text):
    if log==1:
        with open('RNSlog.txt','a') as logfile:
            currtime=str(datetime.datetime.now())
            logfile.write(currtime+" 日志："+str(text)+'\n')
writelog('日志函数定义完成，开始记录。')
writelog('随机姓名选择器 '+'版本 '+version+' '+readableversion)

# 读取列表，使用 global 变量，无参数。
def getname():
    writelog('获取姓名列表：') 
    print("读取列表")
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
    print("读取完成")
    writelog("读取完成。")
# 获取总数，调试用途。
def getcount():
    print(count)
# 获取随机数，使用 global 变量，无参数。
def getrand():
    number=random.randint(1,count)
    writelog('获取随机数：'+str(number))
    return number
# 抽取，使用 global 变量，无参数。
def getaname():
    number=getrand()
    aname=names[number-1:number]
    writelog('获取姓名：'+str(aname))
    for theone in aname:
        therightone=theone
    return therightone
if __name__=='__main__':
    print('[成功]定义函数完成')
if __name__=='__main__':
    print('-----------------------')
# 开始运行
if __name__=='__main__':
    print('开始抽取')
    getname()
    input("就绪，按Enter抽取")
    if cheat==1:
        writelog('作弊模式开启！')
        nname=getaname()
        while nname==yourname:
            writelog("获取作弊者姓名，重试。")
            nname=getaname()
    else:
        nname=getaname()
    print('抽取结果：')
    print(nname)
    writelog('输出完成。')
    print('完成')
    input("按Enter继续")
    while True:
        print('开始抽取')
        if refresh==1:
            writelog("刷新姓名列表。")
            getname()
        if cheat==1:
            writelog('作弊模式开启！')
            nname=getaname()
            while nname==yourname:
                writelog("获取作弊者姓名，重试。")
                nname=getaname()
        else:
            nname=getaname()
        print('抽取结果：')
        print(nname)
        writelog('输出完成。')
        print('完成')
        input("按Enter继续")
