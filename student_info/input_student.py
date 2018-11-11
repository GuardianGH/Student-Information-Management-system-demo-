import write_file as WF


class Student:
	def __init__(self,name,age,score):
		self.name = name
		self.age = age
		self.score = score

def input_student():
	'''
	输入函数（追加）
	'''
	l = []		#空列表
	count = 0
#	path = os.getcwd()
	print('输入学生成绩，不需要输入时直接回车')
	def P_inf():
		nonlocal count
#		d = {}

		count +=1
		print('输入第 %d 个学生的信息：'%count)
		name = input("输入姓名：")
		if name =='':
#			return d
			return None
		else:
			age = input('输入年龄：')
			score = input('输入成绩：')
			stu = Student(name,age,score)
#			d = dict( 姓名 =name, 年龄 =age, 成绩 =score)
			print()
			return stu
#			return d

	while True:
#		D = P_inf()
		C_stu = P_inf()
#		if D=={}:
		if C_stu is None:
			break
		else:
#			if D['年龄'].isdigit() and 0<int(D['年龄'])<300 and D['成绩'].isdigit() and 0<=int(D['成绩'])<150:
			if C_stu.age.isdigit() and 0< int(C_stu.age) <300 and C_stu.score.isdigit() and 0<= int(C_stu.score) <150:
				l.append(dict(姓名=C_stu.name,年龄=int(C_stu.age),成绩=int(C_stu.score)))
#				l.append(D)
			else:
				print('不好意思，你好像输错啦^_^')


	WF.write_file(l,'a')
