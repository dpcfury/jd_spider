# -*- coding:utf-8 -*-
import xlrd
# 打开excel 文件
data = xlrd.open_workbook('jd.xlsx')
# 通过名称获取工作表
table = data.sheet_by_name(u'product')
# 获取表格的行数和列数
nrows = table.nrows
ncols = table.ncols

print "total row :%d" % nrows
print "total col :%d" % ncols

count = 1
for i in range(1, nrows):
    if count == 10:
        break
    # 获取一行的数据，返回数组
    row_values = table.row_values(i)
    for i in range(ncols):
        print row_values[i]

    count += 1

