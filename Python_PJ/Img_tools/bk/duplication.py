import os
import shutil
import glob
import pprint

def duplication():
	print('=== File replication program ===')
	exe_num = input('Please specify the number of files to be created : ')
	exe_num = int(exe_num)
	count = 1

	#test method
	'''
	work_dir = glob.glob('./*')
	work_dir.sort()
	pprint.pprint(work_dir)

	#test work path
	#/private/var/mobile/Library/Mobile Documents/iCloud~com~omz-software~Pythonista3/Documents
	'''

	#Enter path
	while True:
		exe_path = input('Enter working directory : ')
		anser_exe = input('Is your working directory ? : ' + exe_path + ' : [y/n]')
		
		if anser_exe == 'y':
			#print('ok')
			#print('working directory is : ' + exe_path)
			os.chdir(exe_path)
			now_path = os.getcwd()
			print('===== working directory files =====')
			print('Path now : ' + now_path) 
			print('================================')
			work_dir = glob.glob('./*')
			work_dir.sort()
			pprint.pprint(work_dir)
			print('================================')
			break
		else:
			print('=== enter it again ===')


	#Enter source & execution directory
	while True:
		src_path = input('Please enter the source directory : ')
		dst_path = input('Please enter the execution directory : ')
		
		if src_path in work_dir and dst_path in work_dir:
			print('=== path found ===')
			anser_path = input('Are you sure ? : [y/n]')
			if anser_path == 'y':
				print('==============================')
				print('source directory => ' + src_path)
				print('execution directory => ' + dst_path)
				print('=== source directory file list ===')
				#os.chdir(src_path)
				src_dir = glob.glob(src_path + '/*')
				src_dir.sort()
				pprint.pprint(src_dir)
				print('==============================')
				break
			else:
				print('=== Please re-enter ===')	
		else:
			print('=== ERROR : Path does not exist ===')
			print('=== Please re-enter ===')

	'''
	src_path = './Img_original'
	dst_path = './Img_rename'
	count = 1

	#os.chdir(src_path)
	src_dir = glob.glob(src_path + '/*')
	src_dir.sort()
	pprint.pprint(src_dir)
	'''

	while True:
		src_file = input('Please enter the target file name : ')
		if src_file in src_dir :
			print('=== Target file found ===')
			break
		else:
			print('=== ERROR : Target file not found ===')
			print('=== Please re-enter ===')

	for count in range(exe_num):
		dst_name = str(count) + '_' + os.path.basename(src_file)
		
		dst_file = os.path.join(dst_path + '/' + dst_name)
		shutil.copy(src_file,dst_file)
		print(src_file + ' => ' + dst_file)
		count += 1
		
	print('=== completion of the Duplication process ===')

#duplication()
