import os
import glob
import shutil
import pprint

def rename_main():
	print('=== rename_only.py ===')
	print('''
	This program is processed with,

	1.Select the current directory for processing

	2.copy & rename process
	source directory => execution directory
	''')
	print('======================')

	#test path
	#/private/var/mobile/Library/Mobile Documents/iCloud~com~omz-software~Pythonista3/Documents

	#exe_path = '/private/var/mobile/Library/Mobile Documents/iCloud~com~omz-software~Pythonista3/Documents'

	#Enter path
	while True:
		exe_path = input('Enter working directory : ')
		anser_exe = input('Is your working directory ? : ' + exe_path + ' : [y/n]')
		
		if anser_exe == 'y':
			#print('ok')
			print('working directory is : ' + exe_path)
			break
		else:
			print('=== enter it again ===')

	os.chdir(exe_path)
	now_path = os.getcwd()
	print('===== working directory files =====')
	print('Path now : ' + now_path) 
	print('================================')
	work_dir = glob.glob('./*')
	work_dir.sort()
	pprint.pprint(work_dir)
	print('================================')

	#test 
	#from_path = './Img_original'
	#to_path = './Img_rename'


	#Enter source & execution directory
	while True:
		
		
		from_path = input('Please enter the source directory : ')
		to_path = input('Please enter the execution directory : ')
		
		
		if from_path in work_dir and to_path in work_dir:
			print('=== path found ===')
			anser_path = input('Are you sure ? : [y/n]')
			if anser_path == 'y':
				print('==============================')
				print('source directory => ' + from_path)
				print('execution directory => ' + to_path)
				print('=== source directory file list ===')
				src_files = glob.glob(os.path.join(from_path + '/*'))
				src_files.sort()
				pprint.pprint(src_files)
				print('==============================')
				break
			else:
				print('=== ERROR : Path does not exist ===')
				print('=== Please re-enter ===')


	def rename():
		print('===== start rename process =====')
		new_name = input('Please enter a new file name : ')
		#files => src_files
		for i, f in enumerate(src_files, 1):
			re_name = new_name + '_' + '{0:03d}'.format(i) + '.jpg'
			
			copy_path = os.path.join(to_path + '/' + re_name)
			
			print(f + ' => ' + to_path + '/' + re_name)
			
			shutil.copy(f,copy_path)

	rename()

	print('=== completion of the rename process ===')
