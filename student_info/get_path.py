
import sys
import os

#import time
#from tishi import *


def get_path():
	"""获取本地保存的文件目录"""

	localf = os.getcwd()+"/file_path.txt"
	path_l = []
	with open(localf,'r') as read_path:
		lines = read_path.readlines()
		print('*******************lines: ', lines)
		if lines:
			for line in lines:
				li = line.split(' ')
				if '\n' in li:
					li.remove('\n')
					s = ''.join(li)
					path_l.append(s)
				else:
					s = ''.join(li)
					path_l.append(s)

			if '' in path_l:
				path_l.remove('')
				return path_l[-1]	#返回最后读取的文件
			return path_l[-1]
		else:
			print("file_path文件不存在或者为空")
			sys.exit(5)
