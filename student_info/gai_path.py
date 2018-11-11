import read_file as Rf
import write_file as Wf
import tkinter
import tkinter.filedialog
import tishi as Ts
def gai_path():
	'''
	更改学生信息文件保存目录
	'''
	lf_old = Rf.read_file()
	xuan_ze = tkinter.filedialog.askdirectory(title = '选择途径文件保存目录')		#返回目录元组

	if xuan_ze ==():
		print('已取消')
		return
	else:
		path = '%s' % xuan_ze
		f_path = '%s/student_info.txt'%path

		Ts.tishi('正在保存文件',3)
		with open(f_path,'w') as fw:
			for d in lf_old:
				fw.write('%s,%s,%s\n'%(d['姓名'],d['年龄'],d['成绩']))
		print('文件已复制到%s'%f_path)
		Ts.tishi('文件保存成功',3)
