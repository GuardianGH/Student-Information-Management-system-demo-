# coding:utf-8
#import time
import os
#import tkinter.filedialog
import sys
import gai_path as Gp
import input_student as iput
import output_info as oput
#from read_file import *
import shan_chu as Sc
#from write_file import *
import xiu_gai as Xg
import tishi as Ts
import jia_zai as Jz
#path = '/home/tarena/aid1803/fc/code'
path = os.getcwd()
sys.path.append(path)


def ml():
	while True:
		print('''
+---------------------------------------+
| 1) 添加学生信息			|
| 2) 显示所有学生的信息			|
| 3) 删除学生信息			|
| 4) 修改学生信息			|
| 5) 按学生成绩高-低显示学生信息	|
| 6) 按学生成绩低-高显示学生信息	|
| 7) 按学生年龄高-低显示学生信息	|
| 8) 按学生年龄低-高显示学生信息	|
| 9) 复制信息到新的目录			|
| 0) 选择学生信息文件			|
| q) 退出				|
+---------------------------------------+
		''')
		xz = input('请选择需要操作的条目：')
		if xz =='q':
			print('退出系统！')
			break
		elif xz == '1':
#			global l
			iput.input_student()
		elif xz == '2':
			oput.output_student(False,'姓名')

		elif xz == '3':
			Sc.shan_chu()
			
		elif xz == '4':
			Xg.xiu_gai()
			
		elif xz == '5':
			oput.output_student(True,'成绩')			
		elif xz == '6':
			oput.output_student(False,'成绩')			
		elif xz == '7':
			oput.output_student(True,'年龄')			
		elif xz == '8':
			oput.output_student(False,'年龄')
		elif xz == '9':
			Gp.gai_path()
		elif xz == '0':
			Jz.jia_zai()

		else:
			print('输入错误!')
			Ts.tishi('返回目录',3)
	return
