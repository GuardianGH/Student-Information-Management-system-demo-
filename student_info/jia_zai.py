import tkinter
import tkinter.filedialog
import write_file as Wrf
import tishi as Tisi
import os
import output_info as opf
import safe_file_path as sfp
import read_file
import sys
def jia_zai():

	jia_zai_f= tkinter.filedialog.askopenfilename(title = '选择加载的文件',filetypes=[('TXT格式','.txt')])
	if jia_zai_f ==():
		print('已取消')
	else:
		fn = os.path.basename(jia_zai_f)	#截取文件名
		r_path = os.path.dirname(jia_zai_f)#截取文件所在文件夹名称
		local_path = os.getcwd()	#获取本地文件夹
		f_local = fn + local_path

		print(jia_zai_f)
		Tisi.tishi('读入中',1)
		sfp.safe_file_path(fn,r_path)

		from imp import reload
		reload(read_file)
		ld = read_file.read_file(jia_zai_f)
		if ld is None:
			return
		else:
			print('数据文件切换成功！即将退出系统，请重新进入系统查看和删改！')
			Tisi.tishi('正在关闭系统...',2)
			sys.exit()
#			opf.output_student()
