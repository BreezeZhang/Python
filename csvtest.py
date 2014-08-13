#!/usr/bin/python
#Filename: TelBook.py

import sys
import os
import time
import csv

def addPerson(filename):
	'''Add a new Person\'s Tel'''
	#print ("addPerson fun start")
	person = input('Enter the persons\' name?(y/n)')
	tel = input('Enter the persons tel: ')
	update=time.strftime('%Y-%m-%d %H:%m:%S')
	
	f = open(filename, 'a+')
	writer1=csv.writer(f ,dialect='excel')
	writer1.writerow([person,tel,update])
	f.close()
	
	print ('New Person\'s tel has been added!')
	
if (os.path.isfile('TelBook.csv'))==False:
		title=['NAME','TEL','TIME']
		f = open('TelBook.csv', 'w')
		writer1=csv.writer(f ,dialect='excel')
		#writer1.writerow([person,tel,update])
		writer1.writerow(title)
		f.close()
		
swag = input("Do you wanna Enter a new Person\' tel?(y/n)")
if swag=='y':
	flag=True
else:
	flag=False
	print ('Thanks, Bye!')
while flag:		
	addPerson('TelBook.csv')
	t = input("Do you wanna Enter another?(y/n)")
	if t != 'y':
		break
	
