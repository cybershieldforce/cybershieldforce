###__IMPORT__###

import os , time
from time import sleep

###__COLOURS__###

GREEN ='\x1b[38;5;46m'
RED = '\x1b[38;5;196m' 
WHITE = '\033[1;97m'
YELLOW = '\033[1;33m'
BLUE = '\033[1;34m'
ORANGE = '\033[1;35m'
BLACK="\033[1;30m"

logo = (f'''{GREEN}
     _____   ______   ________  
 .' ___  |.' ____ \ |_   __  | 
/ .'   \_|| (___ \_|  | |_ \_| 
| |        _.____`.   |  _|    
\ `.___.'\| \____) | _| |_     
 `.____ .' \______.'|_____|    

----------------------------------------------------------------
----------------------------------------------------------------
MADE BY CYBER SHIELD FORCE
TELEGRAM : https://t.me/CSFTEAM143
GITHUB       : cybershieldforce
FACEBOOK  : CYBERSHIELDFORCE
----------------------------------------------------------------
---------------------------------------------------------------- ''')

menu = ('''
[1] TERMUX BASIC SETUP
[2] FACEBOOK BRUTE FORCE ATTACK
[3] FACEBOOK RANDOM ID CLONE
[4] FACEBOOK ID INFORMER
[5] FACEBOOK PHISHING LINK MAKER
[6] BD FAST SMS BOOMBER
[7] TERMUX STYLE LIKE PRO
[8] FACEBOOK PASSWORD LIST MAKER
[9] JOIN OUR TELEGRAM CHANNEL
[10] EXIT
''')

def setup ():
	os.system("pkg update && pkg upgrade && pkg install curl && pkg install wget && pkg install git && pkg install python && pkg install python2 && pkg install ruby && pkg install php && pkg install nano && pkg install vim && pkg install figlet && pkg install cowsay && pkg install toilet && pkg install unzip && pkg install tar && pkg install zip && pkg install tor && pkg install w3m && pkg install proot && pkg install openssl && pkg install wget && pip install requests && pip install mechanize && pip install bs4 && termux-setup-storage")
	exit()
def fbbrute():
	os.system("rm -rf FB-Brute && git clone https://github.com/STLP-TEAM/FB-Brute && cd FB-Brute && python brute.py")
def zphisher ():
	os.system("rm -rf zphisher && git clone --depth=1 https://github.com/htr-tech/zphisher.git && cd zphisher && bash zphisher.sh")
def ranclone ():
	os.system("rm -rf R4NDOM && pip install bs4 && pip install requests && git clone https://github.com/wasimmoulik008/R4NDOM && cd R4NDOM && python OR4NDOM.py")
def fbinform ():
	os.system("rm -rf Facebook && pkg install ruby && pkg install git && git clone https://github.com/MR-X-Junior/Facebook && cd Facebook && ruby main.rb")
def smsboomtoxic ():
	os.system("rm -rf ToxicBomber && git clone https://github.com/Toxic-Noob/ToxicBomber && cd ToxicBomber && python Tbomb.py")
def termuxstyle():
	os.system("rm -rf T-LOAD && pip install lolcat && git clone https://github.com/noob-hackers/T-LOAD && cd T-LOAD && bash t-load.sh")
def passlist():
	os.system("rm -rf cupp && git clone https://github.com/Mebus/cupp && cd cupp && python cupp.py -i")
def join():
	os.system("xdg-open https://t.me/CSFTEAM143")
def main():
	os.system('clear')
	print(logo)
	print('')
	print(menu)
	option = input(f'{RED}Choose Option : ')
	if option == '1':
		setup()
		main()
	elif option == '2':
		fbbrute()
	elif option == '3':
		ranclone()
	elif option =='10':
		exit()
	elif option =='5':
	  zphisher()
	elif option =='4':
		fbinform()
	elif option =='6':
		smsboomtoxic()
	elif option =='7':
		termuxstyle()
	elif option =='8':
		passlist()
	elif option =='9':
		join()
	else:
		print('\n')
		print("OPTION NOT FOUND")
		print("OPTION NOT FOUND")
		print("OPTION NOT FOUND")
		print("OPTION NOT FOUND")
		print("OPTION NOT FOUND")
		print("OPTION NOT FOUND")
		print("OPTION NOT FOUND")
		print("OPTION NOT FOUND")
		print("OPTION NOT FOUND")
		print("OPTION NOT FOUND")
		print("OPTION NOT FOUND")
		print("OPTION NOT FOUND")
		print("OPTION NOT FOUND")
		print("DEVELOPED BY CYBER SHIELD FORCE")
		time.sleep(3)
		main()

main()





#os.system('apt install git')
