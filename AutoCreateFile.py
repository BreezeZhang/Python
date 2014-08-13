#!/usr/bin/python
# -*- coding:utf-8 -*-
import sys
import os

def create_file(path, size):
	file = open(path, 'w')
	file.seek(size)
	file.write('\x00')
	file.close()
	print (path, ": 创建成功")

def show_help():
	print ("-----------------------------------------------------------------")
	print ("Version: 2.0")
	print ("Author: buju.hh@alibaba-inc.com")
	print ("-----------------------------------------------------------------")	
	print ("用法: AutoCreateFile.py [-h] [-KB size] [-MB size] [-GB size]")
	print ("")
	print ("-h 		显示本帮助内容")
	print ("-KB size	在当前目录，以KB为单位，创建指定大小的文件")
	print ("-MB size	在当前目录，以MB为单位，创建指定大小的文件")
	print ("-GB size	在当前目录，以GB为单位，创建指定大小的文件")
	print ("")	

def cur_file_dir():
    path = sys.path[0]
    if os.path.isdir(path):
        return path
    elif os.path.isfile(path):
        return os.path.dirname(path)

def covert_string_to_float(str):
	size = float(str)

	if(size < 0):
		print ("输入的文件大小有误")
		print ("-h 参考帮助文档")
		os._exit()

	return size

def main():
	argv = sys.argv
	c_path = cur_file_dir()

	if(len(argv) < 2):
		show_help()
	elif(argv[1] == "-h"):
		show_help()
	elif(argv[1] == "-KB"):	
		try:
			size = covert_string_to_float(argv[2])
			name = "\\" + argv[2] + "KB.data"
			create_file(c_path + name, 1024*size)		
		except:
			show_help()
	elif(argv[1] == "-MB"):
		try:
			size = covert_string_to_float(argv[2])
			name = "\\" + argv[2] + "MB.data"
			create_file(c_path + name, 1024*1024*size)		
		except:
			show_help()
	elif(argv[1] == "-GB"):
		try:
			size = covert_string_to_float(argv[2])
			if(size > 10):
				userInput = raw_input("你将要创建一个10GB大小的文件，确定吗？(y/n)")
				if(userInput != "y"):
					return
			name = "\\" + argv[2] + "GB.data"
			create_file(c_path + name, 1024*1024*1024*size)
		except:
			show_help()

if __name__ == '__main__':
	main()