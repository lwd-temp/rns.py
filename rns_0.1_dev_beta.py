#! /usr/bin/env python3
# Random Name Selector
# Python 3,Cross platform.
# Author:Sunset Shimmer
# https://github.com/lwd-temp/rns.py
# Copyright © 2019 lwd-temp@Github.com. All rights reserved.
# RNS Open Source License:
# Please read the Chinese version of the License for more information.
# 随机姓名选择器
# 作者：余晖
# lwd-temp@Github.com 2019 版权所有 © 保留所有权利。
# RNS 开源许可证版本0.1
# 在符合下列条件的情况下，
# 特此免费向任何得到本授权作品的副本（包括源代码、文件和/或相关内容，以下统称为“授权作品”）的个人和法人实体授权：
# 被授权个人或法人实体有权以任何目的处置授权作品，包括但不限于使用、复制，修改，衍生利用、散布，发布和再许可：
# 1.个人或法人实体必须在许可作品的每个再散布或衍生副本上包含以上版权声明和本许可证，不得自行修改。
# 2.个人或法人实体必须严格遵守与个人实际所在地或个人出生地或归化地、或法人实体注册地或
#    经营地（以较严格者为准）的司法管辖区所有适用的与劳动和就业相关法律、法规、规则和
#    标准。如果该司法管辖区没有此类法律、法规、规章和标准或其法律、法规、规章和标准不可
#    执行，则个人或法人实体必须遵守国际劳工标准的核心公约。
# 3.个人或法人不得以任何方式诱导或强迫其全职或兼职员工或其独立承包人以口头或书面形式同
#    意直接或间接限制、削弱或放弃其所拥有的，受相关与劳动和就业有关的法律、法规、规则和
#    标准保护的权利或补救措施，无论该等书面或口头协议是否被该司法管辖区的法律所承认，该
#    等个人或法人实体也不得以任何方法限制其雇员或独立承包人向版权持有人或监督许可证合规
#    情况的有关当局报告或投诉上述违反许可证的行为的权利。
# 4.授权作品允许在遵守开源许可证的情况下用于商业用途，特此强调。
# 5.禁止在分发版本中删除或修改此许可证或表示（或暗示）虚假的授权作品原作者信息。
# 6.需在使用授权作品的相关源代码文件中附带作者信息、相关注释、彩蛋函数（即 zwt() ）完整代码、关注信息技术从业者公益广告、公益广告触发代码及相关变量。
# 7.若已明确知晓许可证要求会直接导致使用授权作品的应用程序的故障，可以注释相关代码但必须告知用户授权作品的使用并在应用程序说明中提供
#    授权作品的完整版本并向用户明示。
# 8.无论如何，使用授权作品的应用程序或其他作品需在明显位置向用户明示授权作品的完整（即此文件）源代码（含注释）。
# 9.被授权个人或法人实体有义务对部署授权作品的设备及时提供授权作品的最新更新。
# 该授权作品是"按原样"提供，不做任何明示或暗示的保证，包括但不限于对适销性、特定用途适用
# 性和非侵权性的保证。在任何情况下，无论是在合同诉讼、侵权诉讼或其他诉讼中，版权持有人均
# 不承担因本软件或本软件的使用或其他交易而产生、引起或与之相关的任何索赔、损害或其他责任。
# 使用说明：
# 姓名列表应位于工作目录下 namelist.txt 文件内，
# 每行一个姓名，不得空行，否则报错。
# 工作目录下会生成 RNSlog.txt 日志文件，
# 可用于调试。
# 此代码无保修且仅带有作者的最好祝愿，作者不为任何软件、硬件错误或损失及数据丢失负责。
# 请自行检查阁下的 Python 解释器发行版是否携带病毒或恶意软件，是否存在编译错误或对 Python 解释器源代码的不正当修改。
# 请自行检查此文件是否被篡改或传输不完整，目前最好的校验方法是前往 Github.com 获取程序的最新更新。
# Sunset Shimmer Education and Equestria Friendship Lessons Teaching and Technology Development Group Python Development Department,GitHub, Inc.,
# Hasbro.,Python Software Foundation 的雇员或组织成员以及 Sunset Shimmer 或 余晖、余晖烁烁、落日霞光、夕晖烁烁
# （或其他可能翻译）或 lwd-temp@Github.com 不为使用此软件带来的任何损失负责。
# Changelog 更新日志
# 0.1.4 Dev Beta 更新许可证
# 0.1.3 Dev Beta 增加 log 内容 优化彩蛋逻辑 增加公益广告
# 0.1.2 Dev Beta 修复 import 时多余输出和循环问题 补充注释 增加了完全不合理的开源许可用以劝退
# 0.1.1 Dev Beta 优化循环逻辑 彩蛋代码与主程序合并
# 0.1 Dev Beta 本地化完成
# 0.0.1 Dev Beta 首个版本 完成基本逻辑
readableversion='0.1.4开发者测试版'
version='0.1.4_dev_beta'
if __name__=='__main__':
    print('随机姓名选择器'+' '+readableversion)
    print('作者：余晖')
    print('-----------------------')
    print('[信息]导入库')
import random
import random
import datetime
if __name__=='__main__':
    print('[成功]库导入完成')
# [配置 config]
if __name__=='__main__':
    print('[信息]加载配置')
# Cheat:作弊设置，避免被抽取。1或0
cheat=1
# Yourname:与作弊配合使用，避免被抽取的内容。
yourname='余晖'
# Log:日志设置 1或0
log=1
# Egg:彩蛋设置 1或0
# 不推荐在生产环境开启彩蛋
egg=1
# Logegg:彩蛋日志输出 1或0
logegg=1
# Care:关注信息技术从业者公益广告 1或0
# https://996.icu
care=1
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
writelog('RNS '+'版本 '+version+' '+readableversion)
# HappyBirthdayZWT
# Author:LWD
# This code is used as an Easter Egg.
# You can get the code from my Github repo.
# You can NOT remove this function or edit its code.
# 致敬我的第一个实用项目——中考倒计时，代码内有相同功能但低技巧的代码段。
def zwt():
    # Adorable
    writelog("For the most adorable one.")
    date=datetime.datetime.today()
    if date.month==4:
        if int(date.day)>=20:
            if logegg==1:
                writelog("Happy birthday ZWT!")
            else:
                print("Happy birthday ZWT!")
    if date.month==5:
        if date.day==5:
            count=0
            while count!=4:
                if logegg==1:
                    writelog("Happy birthday ZWT!")
                else:
                    print("Happy birthday ZWT!")
                count=count+1
        if date.day<=15:
            if logegg==1:
                writelog("Happy birthday ZWT!")
            else:
                print("Happy birthday ZWT!")
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
    if care==1:
        print("关注信息技术从业者 反对不合理工作时制")
        writelog("关注信息技术从业者 反对不合理工作时制")
    if egg==1:
        writelog("彩蛋开启。")
        zwt()
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
