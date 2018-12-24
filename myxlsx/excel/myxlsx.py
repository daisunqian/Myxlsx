#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@Author  :   sqdai
@Contact :   654251408@qq.com
@Software:   PyCharm
@File    :   myxlsx.py
@Time    :   2018/12/19 17:19

'''
import xlwt
import os
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import xlrd
import pandas as pd

L=[]
H=[]
for root, dirs, files in os.walk('C:\Users\daisq\Desktop\exexl'):
    for file in files:
        if os.path.splitext(file)[1] == '.xlsx':
            L.append(os.path.join(root, file))
print (L)
for i in range(len(L)):
    filename = L[i]
    #workbook = xlrd.open_workbook('C:\\Users\\daisq\\Desktop\\exexl\\111.xlsx')
    workbook = xlrd.open_workbook(filename=filename,encoding_override="utf-8")
    if workbook>0:
        print(workbook.sheet_names())                  #查看所有sheet
        # booksheet = workbook.sheet_by_index(0)         #用索引取第一个sheet
    booksheet = workbook.sheet_by_name('IO-LIST')  #或用名称取sheet
    # # #读单元格数据
    cell_11 = booksheet.cell_value(0,0)
    cell_21 = booksheet.cell_value(1,0)
    cell_33 = booksheet.cell_value(0,1)
    if booksheet.cell(0,0).ctype == 0:
        print 32323232
    # #读一行数据
    row_3 = booksheet.row(3)
    print booksheet.row_values(3)[0].encode("utf-8")
    print booksheet.row(2)[2].ctype
    print booksheet.cell_value(3,0)
    print(cell_11, cell_21, row_3)
    print row_3
    len = booksheet.row_len(3)
    print(len)

    # for i in range(booksheet.nrows):
    #     for j in range(booksheet.ncols):
    #         print(booksheet.cell_value(i,j))
    # for i in range(booksheet.nrows):
    #     for j in range(booksheet.ncols):
    #         if 1 == booksheet.cell(i,j).ctype or 2 == booksheet.cell(i,j).ctype :
    #             print(booksheet.cell_value(i, j))

    for i in range(booksheet.nrows):
        if 1 == booksheet.cell(i,0).ctype and 2 == booksheet.cell(i,1).ctype:

            H.append(booksheet.row(i))
            # print H
        print "+++++++",i,H

    row4 = booksheet.row_values(3)
    # row5 = booksheet.row(3)
    # # print(cell_33)
    print (row4)
    # # print(row5)
    # # data = pd.read_excel('C:\\Users\\daisq\\Desktop\\exexl\\222.xlsx',engine="xlrd")
    # # print data
    # print booksheet.nrows,booksheet.ncols
    # print booksheet.row_values(3)
    # print booksheet.cell(0,2).ctype


    # for e in range(len(row_3)):
    #    sunfile.write(8,e,row_3[e])
    #    f.save('sumfile.xlsx')


    # data = xlwt.Workbook(encoding="utf-8")
    # fristsheet = data.add_sheet("mySheer 1",cell_overwrite_ok=True)
    # ha=[u'\u6234\u5b59\u94b1', 90.0, 85.0, 85.0, 80.0, 80.0, 85.0, 90.0]
    # if fristsheet>0:
    #     print 2222222222
    # print "**********",ha
    # for h in range(ha):
    #     print 2222233333
    #     fristsheet.write(0,h,ha[h])
    #     print 33333
    # data.save("mytset.xls")
    # workbook = xlwt.Workbook(encoding='utf-8')
    # booksheet = workbook.add_sheet('Sheet 1', cell_overwrite_ok=True)
    # #存第一行cell(1,1)和cell(1,2)
    # booksheet.write(0,0,34)
    # booksheet.write(0,1,38)
    # #存第二行cell(2,1)和cell(2,2)
    # booksheet.write(1,0,36)
    # booksheet.write(1,1,39)
    # #存一行数据
    # rowdata = [43,56]
    # for i in range(len(rowdata)):
    #     booksheet.write(2,i,rowdata[i])
    # workbook.save('test_xlwt.xls')
    #
    #
