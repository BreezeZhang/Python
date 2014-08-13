#!/usr/bin/python
#simulate D30GI server recv pack and send pack
import sys, socket, struct, time, ctypes

def	checksum(buff = None):
	if buff == None:
		return False
	res = 0
	buflen = len(buff)
	i = 0
	while i < buflen:
		temp = struct.unpack('!b', buff[i: i+1])[0]
		res = res^temp
		i = i+1
	return res
	
def init_task_content(size = 0):
	i = 0
	result = ''
	while i < size:
		if i%2 == 0:
			result += ' '
		if i%20 == 0:
			result += '\n'
		result += str(i)
		i += 1
	return result
#task
def task_init():
	task_id = 0x1050
	task_time = b'tttt'
#	task_action = 0x00    #预约任务0xc0
	task_action = 0xc0    #预约任务0xc0
	task_phone = b'13162477267'
	task_phonelen = len(task_phone)
	task_content = b'''plea senaa
	aaavb bbbb bbbb bbbb
	fdsaf asfd 
	asf af
	asffsas 
	fasf s a 
	fsa ffas 
	fsaaaa aas
	af fasd
	fm eff  daa
	aaaaa  aaa 
	aa aa aaa
	a aaaa aaaaaa
	aaaa aa 
	ff ffff ff
	ff fff fff
	ni hao ha heihei '''
#	task_content = init_task_content(80)
	task_contentlen = len(task_content)
	task_icount = 0
	format_task = ("<I4sBB%dsB%dsB" %(task_phonelen, task_contentlen))
	task_st = struct.pack(format_task, task_id, task_time, task_action, task_phonelen, task_phone, \
		task_contentlen, task_content, task_icount)
	return task_st
	
#package
def pkg_init():
	pkg_buf = task_init()
	pkg_ckm = checksum(pkg_buf)  #校验
	pkg_len =  len(pkg_buf) + 1
	pkg_cmd = 0x98
	format_pkg = ("<BB%dsb" %(pkg_len-1))
	pkg_st = struct.pack(format_pkg, pkg_cmd, pkg_len, pkg_buf, pkg_ckm)
	return pkg_st


host = ''
port = 3222
try:
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error:
	print ("socket init error:")
try:
	s.bind((host, port))
except socket.error:
	print ("socket bind error:")
try:
	s.listen(1)
except socket.error:
	print ("socket listen error: ")
	
conn, addr = s.accept()
request = conn.recv(1024)

print ("reques is ", request)
print ("Connect by ",  addr)
data = b'\x85\x00\xd0'
conn.send(data)
pkg_st = pkg_init()
time.sleep(3)
while(1):
	conn.send(pkg_st)
	tmp = input("whether or not continue send package(y/n): ")
	if(tmp == 'y'):
		continue
	else:
		break
conn.close()
