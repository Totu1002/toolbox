import os
import glob
import shutil
import pprint #use...?
from PIL import Image

def resize():
	print('=== start resize process ===')
	os.chdir(to_path)
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


def rename():
	print('===== start rename process =====')
	new_name = input('Please enter a new file name : ')
	#files => src_files
	for i, f in enumerate(files, 1):
		re_name = new_name + '_' + '{0:03d}'.format(i) + '.jpg'
		
		copy_path = os.path.join(to_path + '/' + re_name)
		
		print(f + ' => ' + to_path + '/' + re_name)
		
		shutil.copy(f,copy_path)
		
#Test processing
#/private/var/mobile/Library/Mobile Documents/iCloud~com~omz-software~Pythonista3/Documents
print(os.getcwd())


#Enter path
while True:
	exe_path = input('Enter working directory : ')
	anser_exe = input('Is your working directory ? : ' + exe_path + ' : [y/n]')
	
	if anser_exe == 'y':
		#print('ok')
		print('working directory is : ' + exe_path)
		break
	else:
		print('enter it again')

#use patern mach process ?
#print list => check

os.chdir(exe_path)
now_path = os.getcwd()
print('===== working directory files =====')
print('Path now : ' + now_path) 
print('================================')
work_dir = glob.glob('./*')
work_dir.sort()
pprint.pprint(work_dir)
print('================================')

#Enter cource & execution directory
while True:
	from_path = input('Please enter the source directory : ')
	to_path = input('Please enter the execution directory : ')
	print('================================')
	print('source directory : ' + from_path)
	print('execution directory : ' + to_path)
	anser_parh = input('Are you sure ? : [y/n]')
	print('================================')
	
	
	#use patern mach process ?
	#path == '' ...
	
	if anser_parh == 'y':
		print('source directory : ' + from_path)
		print('execution directory : ' + to_path)
		files = glob.glob(os.path.join(from_path + '/*'))
		break
	else:
		print('Enter it again')
		
print('=== source directory file list ===')
src_dir = glob.glob(from_path + './*')
src_dir.sort()
pprint.pprint(src_dir)
print('================================')

#Enter process menu
while True:
	print('=== select menu ===')
	print('resize & rename : [1]')
	print('rename only : [2]')
	#print('resize only : [3]')
	print('===================')
	ans_menu = input('Enter the menu number to execute : ')
	
	if ans_menu == '1':
		#resize
		rename()
		print('=== completion of the rename process ===')
		resize()
		print('=== completion of the resize process ===')
		break
	elif ans_menu == '2':
		rename()
		break
	else:
		print('Enter it again')
		
print('=== All processing completed !! ===')
