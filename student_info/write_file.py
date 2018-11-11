import os
from tishi import *
import time

import get_path
from imp import reload
reload(get_path)
f_p = get_path.get_path()
def write_file(l,mod,f_path = f_p):
	'''
	写入文件
	'''
#	print('写入文件：',f_path)
#	f_path = str(os.getcwd())+'/student_info.txt'

	with open(f_path,mod) as fw:
		for d in l:
			fw.write('%s,%s,%s\n'%(d['姓名'],d['年龄'],d['成绩']))
	tishi('正在保存文件',1)
	print('文件已保存到：%s'%f_path)
	time.sleep(1)
