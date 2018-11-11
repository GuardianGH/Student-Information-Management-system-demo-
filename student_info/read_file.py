import sys
import os
import time
from tishi import *
import get_path
#from imp import reload
#reload(get_path)
#import jia_zai as JZ

def read_file(f = get_path.get_path()):		#默认读取最后一次加载的文件
	'''
	读取文件
	'''
	ld = []
	try:
		with open(f,'r') as fr:
			lines = fr.readlines()
			for s in lines:
#				print(type(s))
				if str(s) !='':
					l = list(s)
					l.remove('\n')
					s = ''.join(l)
					ls = s.split(',')
					ds = dict(姓名=ls[0], 年龄=ls[1], 成绩=ls[2])
					ld.append(ds)
				else:
					print('文件为空！')
					sys.exit()
	#				return ml()
		if ld == []:
			print('没有读取到信息！')
			print('请先添加信息')
			input_student()
			print('请重载系统')
			sys.exit()
		else:
			print('已加载文件：%s'%f)
			return ld
	except FileNotFoundError:
		print('没有学生信息文件，请先输入')
		tishi('即将返回目录',7)
		print()
		return
