import os
import shutil
import glob
import pprint


src_path = input('Please enter the source directory : ')
dst_path = input('Please enter the execution directory : ')

print('=== Input path found ===')
print('source directory => ' + src_path)
print('execution directory => ' + dst_path)
print('=== source directory file list ===')
src_dir = glob.glob(src_path + '/*')
src_dir.sort()
pprint.pprint(src_dir)
print('==============================')