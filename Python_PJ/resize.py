import os
import glob
from PIL import Image


wsize = input('Image Size: ')
if wsize=='':
	wsize=700 #デフォルトは幅700px
else:
	wsize = int(wsize)

dir = glob.glob('./*')
print('=== dil all ===')
print(dir)
print('=== in files ===')

to_path = input('select to path : ')
#指定フォルダのjpegファイル一覧を取得
files = glob.glob(os.path.join(to_path + '/*jpg'))
print(files)

for f in files:
	img = Image.open(f)
	if wsize >= img.width:
		continue
	#指定幅からリサイズレートを算出
	rate = wsize / img.width
	#リサイズレートから高さを算出
	hsize = int(img.height * rate)
	#リサイズ実行
	img_resize = img.resize((wsize, hsize))
	
	#新しいファイル名を作成
	imgdir = os.path.dirname(f)
	imgname = os.path.basename(f)
	newfname = imgdir + "/out_" + imgname
	print(newfname)
	
	#リサイズ画像を指定ファイル名で保存
	img_resize.save(newfname)
