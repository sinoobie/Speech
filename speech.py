#!usr/bin/python3.7
#author: kang-newbie
#github: https://github.com/kang-newbie
#contact: https://t.me/kang_nuubi

import os,sys,time

try:
	os.mkdir('audio')
except: pass

def os_detek():
    if os.name in ['nt', 'win32']:
        os.system('cls')
    else:
        os.system('clear')

banner="""
;;;;;;;;;;;;;;;;;
;     KARIN	;	Author: KANG-NEWBIE
; SPEECH - TEXT ;	Contact: t.me/kang_nuubi
;;;;;;;;;;;;;;;;;
"""

def sarg():
	exit("""
Usage:
	python %s --lang (language)
Example:
	python %s --lang id
		or
	python %s --lang en"""%(sys.argv[0],sys.argv[0],sys.argv[0]))
	
if __name__=='__main__':
	os_detek()
	print(banner)
	a=sys.version.split('.')
	if a[0] != '3':
		exit('use python version 3.x.x')
	if len(sys.argv) != 3:
		sarg()
	if 'id' in sys.argv[2]:
		os.system('python3 src/karin_id.py')
	elif 'en' in sys.argv[2]:
		os.system('python3 src/karin_en.py')
	else: sarg()
