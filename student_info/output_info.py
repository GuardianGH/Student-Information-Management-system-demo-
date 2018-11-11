import read_file as Rf
from tishi import *
from imp import reload
def dict_key_sortS(d):
	'''
	用于排序的依据：成绩
	'''
	return d['成绩']

def dict_key_sortA(d):
	'''
	用于排序的依据：年龄
	'''
	return d['年龄']

def dict_key_sortX(d):
	'''
	用于排序的依据：姓名
	'''
	return d['姓名']

def output_student(ToF = False, key = '姓名'):
	'''
	输出函数
	'''
	ja = '+'
	jn = '-'
	su = '|'

	ld = Rf.read_file()
#	print(ld)
	if ld is None:
		return
	else:
		if key =='姓名':
			l_ss = sorted(ld,key = dict_key_sortX,reverse = ToF)

		elif key =='成绩':
			l_ss = sorted(ld,key = dict_key_sortS,reverse = ToF)

		else:
			l_ss = sorted(ld,key = dict_key_sortA,reverse = ToF)

		print('\n以下输出表格：\n')

		def changdu(s):		#调用一次就返回姓名或年龄或成绩的最长的长度
			cdl = []		#存放姓名年龄成绩的长度
			for i in l_ss:
				cd = len(i[s])+2
				cdl.append(cd)
			cd = max(cdl)	#找到最长的
			return cd
		c_n = changdu('姓名')
		c_a = changdu('年龄')
		c_s = changdu('成绩')

		def kuang():
			print(ja, jn*(c_n+2), ja, jn*(c_a+2), ja, jn*(c_s+2), ja, sep = '')
		def hang(name,age,score):
			print(su, name.center(c_n+2),su, age.center(c_a+2),su, score.center(c_s+2),su , sep = '')

		kuang()
		hang('name','age','score')
		kuang()

		for i in l_ss:
	#		print(i)
			name = i['姓名']
			age = i['年龄']
			score = i['成绩']
			hang(name,age,score)
		kuang()
		print()
		input('返回目录请按任意键')
		tishi('即将返回目录',2)
		print()
