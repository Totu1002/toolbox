import subprocess

#[tor_setting_config.bat] for Linux version

user = ""
group = ""

# Source path set valiable
src_path = "config/"

# Destinationpath set valiable
#windows用path
#dst_path = "..¥Browser¥TorBrowser¥Data¥Tor¥"
#Mac用path
#dst_path =  " Tor Browser.app/Contents/Resources/TorBrowser/Tor/torrc-defaults"

#Linux用path
#dst_path = "/etc/tor/"
dst_path = "/home/pr0wler/.local/share/torbrowser/tbb/x86_64/tor-browser_en-US/Browser/TorBrowser/Data/Tor/"
dst_file = "torrc"

def setting_torrc(src_file):
  del_cmd = "rm -rf " + dst_path + dst_file
  set_cmd = "cp " + src_path + src_file + " " + dst_path + dst_file
  subprocess.run(del_cmd,shell=True)
  subprocess.run(set_cmd,shell=True)

def chenge_owner():
  cmd = "chown " + user + ":" + group + " " + dst_path + dst_file
  subprocess.run(cmd,shell=True)

def show_torrc():
  cmd = "cat " + dst_path + dst_file
  subprocess.run(cmd,shell=True)


menutext = """=============== MENU ===============
Please select a batch file to execute
=======================================
[0]torrc_level0
setting[entry:{jp}only,include:{jp}only,exit:{jp}only]

[1]torrc_level1
setting[entry:{jp}only,include:1hop country,exit:{jp}only]

[2]torrc_level2
setting[entry:{jp}only,include:1hop country,exit:1hop country]

[3]torrc_level3
setting[entry:1hop country,include:1hop country,exit:1hop country]

[4]torrc_level4
setting[entry:tor default,include:tor default,exit:tor default]

[5]torrc_5eyes
setting[exclude:5eyes]

[6]torrc_9eyes
setting[exclude:9eyes]

[7]torrc_14eyes
setting[exclude:14eyes]

[8]torrc_41eyes
setting[exclude:41eyes]

[9]torrc_levelMAX
setting[exclude:41eyes + dangerous country]

[10]torrc_levelCustom
setting[exclude:14eyes + mycountry + EntryGuargs 15]

[s]:Show running config
Check the current settings .

[d]:Return to default config

[q]:Cancel selection
======================================="""
print(menutext)

while True:
  num = input('Please enter the menu number : ')
  print("Selected menu number : " + num)
  if num == "0":
    src_file = "torrc_level0.txt"
    setting_torrc(src_file)
    chenge_owner()
    break
  elif num == "1":
    src_file = "torrc_level1.txt"
    setting_torrc(src_file)
    chenge_owner()
    break
  elif num == "2":
    src_file = "torrc_level2.txt"
    setting_torrc(src_file)
    chenge_owner()
    break
  elif num == "3":
    src_file = "torrc_level3.txt"
    setting_torrc(src_file)
    chenge_owner()
    break
  elif num == "4":
    src_file = "torrc_level4.txt"
    setting_torrc(src_file)
    chenge_owner()
    break
  elif num == "5":
    src_file = "torrc_5eyes.txt"
    setting_torrc(src_file)
    chenge_owner()
    break
  elif num == "6":
    src_file = "torrc_9eyes.txt"
    setting_torrc(src_file)
    chenge_owner()
    break
  elif num == "7":
    src_file = "torrc_14eyes.txt"
    setting_torrc(src_file)
    chenge_owner()
    break
  elif num == "8":
    src_file = "torrc_41eyes.txt"
    setting_torrc(src_file)
    chenge_owner()
    break
  elif num == "9":
    src_file = "torrc_levelMax.txt"
    setting_torrc(src_file)
    chenge_owner()
    break
  elif num == "10":
    src_file = "torrc_levelCustom.txt"
    setting_torrc(src_file)
    chenge_owner()
    break
  elif num == "d":
    src_file = "torrc_.txt"
    setting_torrc(src_file)
    chenge_owner()
    break
  elif num == "s":
    show_torrc()
    break
  elif num == "q": 
    print("--- Quit ---")
    break
  else:
    print("--- INPUT ERROR ---")

print("--- Running configuration ---")
show_torrc()
