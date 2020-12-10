import os
import glob
import shutil
import pprint #use...?
from PIL import Image

def resize_main():
	print('=== Infomation ===')
	print('''
	This program is processed with,

	1.Select a directory to execute the process.

	2.Select the width of the size to change.
	  Resize without changing the aspect ratio.
	''')
	print('======================')

	def resize():
		print('=== start resize process ===')
		os.chdir(src_path)
		#print(os.getcwd())
		#pprint.pprint(glob.glob('./*'))
		
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


	#Enter source & execution directory
	while True:
		
		src_path = input('Please enter the source directory : ')
		#dst_path = input('Please enter the execution directory : ')
		
		if(os.path.exists(src_path)):
			print('=== path found ===')
			print('source directory => ' + src_path)
			#print('execution directory => ' + dst_path)
			print('=== source directory file list ===')
			src_dir = glob.glob(src_path + '/*')
			src_dir.sort()
			pprint.pprint(src_dir)
			print('==============================')
			anser_path = input('Are you sure ? : [y/n]')
			if anser_path == 'y':
				resize()
				break
			else:
				print('=== ERROR : Path does not exist ===')
				print('=== Please re-enter ===')
	
	print('=== completion of the resize process ===')

#test run
#resize_main()
