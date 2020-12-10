import shutil
import os
import glob
from PIL import Image

print("■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■")
print("Welcome to [resize_and_rename.py]")
print("このプログラムは[実行元フォルダ]より[実行先のフォルダ]へ")
print("[対象ファイル]をコピーすることでリサイズ・リネームを行います。")
print("■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■")

#Execution directory
exe_path = input('Enter working directory : ')
print(exe_path)
#anser_exe = input("Are you sure in this directory? [yes/no]: ")

now_path = os.getcwd()
print(now_path) 
print('===== 実行ディレクトリ =====')
print("選択された実行ディレクトリ：" + exe_path)
print("ディレクトリ配下一覧")
print(glob.glob("./*"))
print('=========================')


if anser_exe == "yes":
    os.chdir(exe_path)
    now_path = os.getcwd()
    print(now_path) 
    print('===== 実行ディレクトリ =====')
    print("選択された実行ディレクトリ：" + exe_path)
    print("ディレクトリ配下一覧")
    print(glob.glob("./*"))
    print('=========================')
    
    else:
        #print("")
        continue


#for_path = input("[実行元フォルダ]を入力してください：")
#to_path = input("[実行先のフォルダ]を入力してください：")
from_path = input('Please enter the source directory : ')
to_path = input('Please enter the execution directory : ')

print('source directory : ' + from_path)
print('execution directory : ' + to_path)

