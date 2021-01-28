import defss
import time as tm
import os
import sys
import DB

while True:
	p = '9828'
	t = input('what u wanna do?\n\nadd something on DB <add>, acess something in DB <acss>, clear the terminal <cls>, <rmv> to remove, or get out of the progam? <q>\n: ').lower()
	if t == 'add':
		pin = input('PIN: ')
		if pin != p:
			while pin != p  :
				pin = input('PIN: ')
				if pin == p:
					a = input('what do you wanna add ?\n: ')
					defss.add(a)
		elif pin == p:
			a = input('what do you wanna add?\n')
			defss.add(a)
	elif t == 'acss':
		pin = input('PIN: ')
		if pin != p:
			while pin != p:
				pin = input('PIN: ')
				if pin == p:
					defss.acss()
		elif pin == p:
			defss.acss()
	elif t == 'cls':
		os.system('clear')
	elif t == 'q':
		defss.rpp()
	elif t == 'rmv':
		pin = input('PIN: ')
		if pin != p:
			while pin != p  :
				pin = input('PIN: ')
				if pin == p:
					defss.remove()
	else:
		print('please type again')
		tm.sleep(1)
		os.system('clear')
