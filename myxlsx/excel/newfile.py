#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@Author  :   sqdai
@Contact :   654251408@qq.com
@Software:   PyCharm
@File    :   newfile.py
@Time    :   2018/12/21 9:26

'''
import xlrd
import xlwt
import os
import sys
import pandas as pd



def getfilename():
    L = []
    for root, dirs, files in os.walk('C:\Users\daisq\Desktop\exexl'):
        for file in files:
            if os.path.splitext(file)[1] == '.xlsx':
                L.append(os.path.join(root, file))
    print (L)
def getdata():
    Listname = []
    data = []
    for root, dirs, files in os.walk('C:\Users\daisq\Desktop\exexl'):
        for file in files:
            if os.path.splitext(file)[1] == '.xlsx':
                Listname.append(os.path.join(root, file))
    print (Listname)
    for i in range(len(Listname)):
        filename = Listname[i]
        workbook = xlrd.open_workbook(filename=filename, encoding_override="utf-8")
        if workbook > 0:
            print(workbook.sheet_names())  # 查看所有sheet
        booksheet = workbook.sheet_by_name('IO-LIST')  # 或用名称取sheet
        for i in range(booksheet.nrows):
            if 1 == booksheet.cell(i, 0).ctype and 2 == booksheet.cell(i, 1).ctype:
                data.append(booksheet.row(i))
            print "+++++++", i, data
    print data[0][1]
    return data

def getnewxls(data):
    workbook = xlwt.Workbook(encoding='utf-8')
    booksheet = workbook.add_sheet('Sheet 1', cell_overwrite_ok=True)
    # # 存一行数据
    rowdata = [u'',u'廖颖',u'孟轲',u'彭俊华',u'陆志强',u'罗词威',u'贺礼云',u"周其林"]
    colsdata = [u'',u'廖颖',u'孟轲',u'戴孙钱',u'兰钧耀',u'黎宏',u'罗词威',u'陆志强',u'杨雨',u'刑定宇',u'贺礼云',u'彭俊华',u'袁冁鑫',u'惠明珠',u'徐洪浩',u'张承文',u'段世峰',u'张兆伟',u'赵敏',u'周其林',]
    data = data
    print data[0][1]
    for i in range(len(rowdata)):
        booksheet.write(0, i, rowdata[i])
    for i in range(len(colsdata)):
        booksheet.write(i, 0, colsdata[i])
    # for j in range(len(data)):
    for k in range(20):
        for a in range(8):
            print k+1,a,data[k][a]
            booksheet.write(k+1,a,data[k][a])
    workbook.save('test3_xlwt.xls')

if __name__ == "__main__":
    data = getdata()
    getnewxls(data)