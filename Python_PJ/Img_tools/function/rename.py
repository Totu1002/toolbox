import os
import glob
import shutil
import pprint

#--- Rev.2.0 ---
#--- 2020/01/09 ---

def rename_main():
	print('=== rename_only.py ===')
	print('''
	This program is processed with,

	1.Select a directory to execute the process.

	2.copy & rename process
	source directory => execution directory
	''')
	print('======================')

	def rename():
		print('===== start rename process =====')
		new_name = input('Please enter a new file name : ')
		#files => src_dir
		for i, f in enumerate(src_dir, 1):
			re_name = new_name + '_' + '{0:03d}'.format(i) + '.jpg'		
			copy_path = os.path.join(dst_path + '/' + re_name)	
			print(f + ' => ' + dst_path + '/' + re_name)
			shutil.copy(f,copy_path)

	#Enter source & execution directory
	while True:
		src_path = input('Please enter the source directory : ')
		dst_path = input('Please enter the execution directory : ')
		
		if(os.path.exists(src_path)) and (os.path.exists(dst_path)):
			print('=== path found ===')
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
				rename()
				break
			else:
				print('=== Please enter again ===')
		else:
			print('=== ERROR : Path does not exist ===')
			print('=== Please enter again ===')
	
	print('=== completion of the rename process ===')

#test running to method
#rename_main()