#標準ライブラリ
import shutil
import os
import glob

print('===== Current directory =====')
#カレントデイレクトリの一覧を表示
print(glob.glob('./*'))
print('===================')


#input()を使用して選択式に変更可能
from_path = './Img/Img_befor'
to_path = './Img/Img_after'
print('***** selected path ! *****')


print('===== in files =====')
files = glob.glob(os.path.join(from_path + '/*'))
print(files)
print('===================')
new_name = input('File name : ')

print('===== rename method =====')
for i, f in enumerate(files, 1):
	#os.rename(f, os.path.join(path, '{0:03d}'.format(i) +'_' + os.path.basename(f)))
	
	re_name = new_name + '_' + '{0:03d}'.format(i) + '.jpg'
	copy_path = os.path.join(to_path + '/' + re_name)

	#os.rename(f,os.path.join(to_path,re_name)
	#os.rename(f,os.path.join(to_path,'{0:03d}'.format(i) + '.jpg'))
	
	shutil.copy(f,copy_path)
	#shutil.copy('c:\\pg\\file1.txt','c:\\pg\\python\\test_file.txt')

	print(f + ' => ' + to_path + '/' + re_name)
	#print(f + '=>' + to_path + '/' + '{0:03d}'.format(i) + '.jpg')
	
print('===== rename ok !! =====')
