from time import sleep

#カウントダウンタイマープログラム

set_time = input('set time :')
print('timer on!')

def down_timer(secs):
	for i in range(secs,0,-1):
		print(i)
		sleep(1)
	print('＊＊＊time is now!＊＊＊')

down_timer(int(set_time))

