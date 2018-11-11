import time

def tishi(info,n):
	for i in '/－\\|'*n:
		print('%s'%info,'%s\r'%i,end = '')
		time.sleep(1/10)

