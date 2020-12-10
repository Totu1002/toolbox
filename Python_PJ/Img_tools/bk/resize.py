import os
import glob
import shutil
import pprint #use...?
from PIL import Image

def resize_main():
	print('=== rename_only.py ===')
	print('''
	This program is processed with,

	1.Select the current directory for processing

	2.Change directry & resize process
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
	#from_path = './Img_rename'
	#from_path = './Img_original'
	#to_path = './Img_rename'

	#Enter source & execution directory
	while True:
		
		from_path = input('Please enter the source directory : ')
		#to_path = input('Please enter the execution directory : ')
		
		if from_path in work_dir:
			print('=== path found ===')
			print('source directory => ' + from_path)
			anser_path = input('Are you sure ? : [y/n]')
			if anser_path == 'y':
				print('=== source directory file list ===')
				src_files = glob.glob(os.path.join(from_path + '/*'))
				src_files.sort()
				pprint.pprint(src_files)
				print('==============================')
				break
			else:
				print('=== ERROR : Path does not exist ===')
				print('=== Please re-enter ===')
				
	def resize():
		print('=== start resize process ===')
		os.chdir(from_path)
		print(os.getcwd())
		pprint.pprint(glob.glob('./*'))
		
		files = glob.glob('./*')
		wsize = input('Please enter the width of the image: ')
		
		if wsize=='':
			wsize=700 
		else:
			wsize = int(wsize)
		
		for f in files:
			img = Image.open(f)
			if wsize >= img.width:
				
				continue
			rate = wsize / img.width
			hsize = int(img.height * rate)
			img_resize = img.resize((wsize, hsize))
		
			resize_name = os.path.basename(f)
			img_resize.save(resize_name,quality = 100)
			print(resize_name + ' => resize')

	'''
	def resize():
		print('=== start resize process ===')
		os.chdir(from_path)
		print(os.getcwd())
		pprint.pprint(glob.glob('./*'))
		
		files = glob.glob('./*')
		wsize = input('Please enter the width of the image: ')
		
		if wsize=='':
			wsize=700 
		else:
			wsize = int(wsize)
		
		while True:
			print('*** If a file with the same name exists, it will be overwritten ! ***')
			ans_name = input('Change file name? : [y/n]')
			
			if ans_name == 'y':
				resize_name = input('Please enter a new file name : ')
				for f in files:
					img = Image.open(f)
					if wsize >= img.width:
						continue
					rate = wsize / img.width
					hsize = int(img.height * rate)
					img_resize = img.resize((wsize, hsize))
					
					#!
					#resize_name = os.path.basename(f)
					resize_name = resize_name + '.jpg'
					img_resize.save(resize_name,quality = 100)
					print(resize_name + ' => resize')
					break
				
			elif ans_name =='n':
				for f in files:
					img = Image.open(f)
					if wsize >= img.width:
						continue 
					rate = wsize / img.width
					hsize = int(img.height * rate)
					img_resize = img.resize((wsize, hsize))
					
					#!!!!!
					resize_name = os.path.basename(f)
					img_resize.save(resize_name,quality = 100)
					print(resize_name + ' => resize')
					break
					
			else:
				print('=== Please select [y] or [n] ===')
	'''
	resize()
	print('=== completion of the resize process ===')
#test run
#resize_main()
