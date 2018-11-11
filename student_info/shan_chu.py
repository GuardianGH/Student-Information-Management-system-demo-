import read_file as Rf
import write_file as Wf
import tishi as ts
#import get_path
def shan_chu():
	'''
	删除学生条目
	'''
	l = Rf.read_file()
#	print(l)
	sc = input('输入需要删除的学生的姓名：')

	for i in l:
		if i['姓名'] ==sc:
			print('您要删除的是：',i['姓名'],'请确认(y/n)')
			qr = input()
			if qr =='y':
				shan_chu = l.pop(l.index(i))
				print('删除了：',shan_chu)
#				from imp import reload	
#				reload(get_path)
				Wf.write_file(l,'w')
				return
			else:
				print('已放弃操作')
				ts.tishi('即将返回目录',4)
				return
	print('没有此人')
	ts.tishi('返回目录',5)
				
	


