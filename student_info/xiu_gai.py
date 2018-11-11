import read_file as r_f
import write_file as w_f
import tishi as ts
#import get_path
def xiu_gai():
	'''
	修改学生条目
	'''
	xg = input('输入需要修改的学生的姓名：')
	l = r_f.read_file()
	count = 0
	for i in l:
		if i['姓名'] ==xg:
			count+=1
			print('您要修改的是：','姓名：%s，年龄：%s，成绩：%s'%(i['姓名'],i['年龄'],i['成绩']))
			print('\n 要修改：\n 姓名 输入1 \n 年龄 输入2　\n 成绩 输入3　\n 可自由修改需要的信息，修改全部输入123')
			qr = input()
		
			if '1' in qr:
				Nname = input('输入新的名字：')
				i['姓名'] = Nname
			
			if '2' in qr:
				Nage = input('输入新的年龄：')
				i['年龄'] = Nage

			if '3' in qr:
				Nscore = input('输入新的成绩：')
				i['成绩'] = Nscore
				break
	if count == 0:
		print('没有这个人哦')
		print('重新输入吗？（y/n）')
		s0 = input('	')
		if s0 == 'y':
			xiu_gai()
			return
		else:
			return
			
	else:
#		from imp import reload	
#		reload(get_path)
		
		w_f.write_file(l,'w')
		return

