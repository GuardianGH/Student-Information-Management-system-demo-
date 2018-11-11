import os
#localpath = os.getcwd()
def safe_file_path(fn,fp = None):
	if not fp:
		fp = os.getcwd()
		
	s = fp	+ '/' + fn+ ' \n'
	localf = os.getcwd() + '/file_path.txt'
	with open(localf,'a') as fpath:
		fpath.write(s)
	fpath.close()
	return
