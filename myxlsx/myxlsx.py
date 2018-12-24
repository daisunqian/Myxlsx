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
    print(cell_11, cell_21)

    # #读一行数据
    row_3 = booksheet.row_values(3)
    print row_3
    # 读取一列的数据
    col_3 = booksheet.col_values(3)
    print col_3

    print booksheet.row_values(3)[0].encode("utf-8")
    print booksheet.row(2)[2].ctype
    print booksheet.cell_value(3,0)


    #查看单元格内数据的数据类型
    # 说明：ctype: 0empty, 1string, 2number, 3date, 4boolean, 5error
    print booksheet.cell(0, 0).ctype
    #打印表格行数
    print booksheet.nrows
    #打印表格列数
    print booksheet.ncols


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


