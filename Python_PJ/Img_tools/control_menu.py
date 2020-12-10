import os
import shutil
import glob
import pprint
import sys
from function import duplication
from function import rename
from function import resize

#Enter process menu
while True:
    print('==== select menu ====')
    print('Fire Rename      : [1]')
    print('Fire Resize      : [2]')
    print('Fire Duplication : [3]')
    print('Exit             : [99]')
    print('=====================')
    ans_menu = input('Enter the menu number to execute : ')
    if ans_menu == '1':
        #rename
	    print('selcted menu [1]')
	    continue
    elif ans_menu == '2':
	    #resize
        print('selcted menu [2]')
        continue
    elif ans_menu == '3':
        #duplication
        print('selcted menu [3]')
        continue
    elif ans_menu == '99':
        #exit process
        print('selcted menu [99]')
        print('=== Exited processing ===')
        break
    else:
        print('Enter it again')
        continue


print('=== All processing completed !! ===')


