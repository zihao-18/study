#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-10-20 17:38:16
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import xlwt 

wb = xlwt.Workbook()


sh1 = wb.add_sheet('成绩')
sh2 = wb.add_sheet('汇总')


sh1.write(0,0,'姓名')
sh1.write(0,1,'专业')
sh1.write(0,2,'科目')
sh1.write(0,3,'成绩')

sh1.write(1,0,'张三')
sh1.write(1,1,'信息与通信工程')
sh1.write(1,2,'数值分析')
sh1.write(1,3,88)

sh1.write(2,0,'李四')
sh1.write(2,1,'计算机应用技术')
sh1.write(2,2,'java程序设计')
sh1.write(2,3,62)

sh1.write(3,0,'王五')
sh1.write(3,1,'计算机信息管理')
sh1.write(3,2,'C语言')
sh1.write(3,3,90)

sh2.write(0,0,'总分')
sh2.write(1,0,240)

wb.save('Score.xls')