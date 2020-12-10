import os
import shutil
import glob
import pprint

#--- Rev.2.0 ---
#--- 2020/01/09 ---

def duplication():
	print('=== File replication program ===')

	#Enter source & execution directory
	while True:
		src_path = input('Please enter the source directory : ')
		dst_path = input('Please enter the execution directory : ')

		if(os.path.exists(src_path)) and (os.path.exists(dst_path)):
			print('=== Input path found ===')
			print('=== Input path found ===')
			print('source directory => ' + src_path)
			print('execution directory => ' + dst_path)
			print('=== source directory file list ===')
			src_dir = glob.glob(src_path + '/*')
			src_dir.sort()
			pprint.pprint(src_dir)
			print('==============================')
			anser_path = input('Are you sure ? : [y/n]')
			if anser_path == 'y':
				os.chdir(src_path)
				src_dir = glob.glob('./*')
				break
			else:
				print('=== Please enter again ===')
		else:
			print('=== ERROR : Input path not found ===')
			print('=== Please enter again ===')


	while True:
		src_file = input('Please enter the target file name : ')
		exe_num = input('Please specify the number of files to be created : ')
		exe_num = int(exe_num)
		count = 1
		if src_file in src_dir :
			print('=== Target file found ===')
			#src_file = os.path.join(src_path + src_file[1:])
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

#test running to method
#duplication()
