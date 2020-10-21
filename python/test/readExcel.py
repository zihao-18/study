import xlrd

wb = xlrd.open_workbook('Score.xls')
print("sheet 数量：",wb.nsheets)
print("sheet 名称：",wb.sheet_names())

sh1 = wb.sheet_by_index(0)

print(u"sheet %s 共 %d 行 %d 列"%(sh1.name,sh1.nrows,sh1.ncols))

#获取并打印某个单元格的值
print("第一行第二列的值为：",sh1.cell_value(0,1))

rows = sh1.row_values(0) #获取第一行内容
cols = sh1.col_values(1) #获取第二列内容


#打印获取的行列值
print("第一行的值为：",rows)
print("第二列的值为：",cols)


#获取单元格内容的数据类型
print("第二行第一列的值类型为：",sh1.cell(1,0).ctype)


#遍历所有表单内容
for sh in wb.sheets():
	for r in range(sh.nrows):
	#输出指定行
		print(sh.row(r))