# -*- coding: utf-8 -*-

import time
import os
import subprocess




try:
    check_pip3 = subprocess.check_output('dpkg -s python3-pip', shell=True)
    if str('install ok installed') in str(check_pip3):
        pass
except subprocess.CalledProcessError:
    print('[+] pip3 not installed')
    subprocess.check_output('sudo apt update',shell=True)
    subprocess.check_output('sudo apt install python3-pip -y', shell=True)
    print('[!] pip3 installed succesfully')



try:

    import requests
except Exception:
    print('[+] python3 requests is not installed')
    os.system('pip3 install requests')
    os.system('pip3 install requests[socks]')
    print('[!] python3 requests is installed ')
try:

    check_tor = subprocess.check_output('which tor', shell=True)
except subprocess.CalledProcessError:

    print('[+] tor is not installed !')
    subprocess.check_output('sudo apt update',shell=True)
    subprocess.check_output('sudo apt install tor -y',shell=True)
    print('[!] tor is installed succesfully ')

os.system("clear")
def ma_ip():
    url='https://www.myexternalip.com/raw'
    get_ip= requests.get(url,proxies=dict(http='socks5://127.0.0.1:9050',https='socks5://127.0.0.1:9050'))
    return get_ip.text

def change():
    os.system("service tor reload")
    print ('[+] Your IP has been Changed to : '+str(ma_ip()))

print('''\033[1;32;88888m \v
 __  __ ____    ________  ____   ___  
|  \/  |  _ \  |__  / _ \|  _ \ / _ \ 
| |\/| | |_) |   / / | | | |_) | | | |
| |  | |  _ <   / /| |_| |  _ <| |_| |
|_|  |_|_| \_\ /____\___/|_| \_\\___/ 
                              
''')
print("\033[1;40;31m https://www.facebook.com/afif.laswed.zorro/\n")
print ("MR ZORO/AFIF LASWED/☠A̷N̷O̷N̷Y̷M̷O̷U̷S̷☠")
print ("service tor start")

os.system("service tor start")




time.sleep(3)
print("\033[1;32;40m change your  SOCKES to 127.0.0.1:9050 \n")
os.system("service tor start")
x = input("[+] time to change Ip in Sec [type=60] >> ")
print ("☠A̷N̷O̷N̷Y̷M̷O̷U̷S̷☠")
lin = input("[+] how many time do you want to change your ip [type=1000]for infinte ip change type [0] >>")
print ("proxy***active :)")
if int(lin) ==int(0):

	while True:
		try:
			time.sleep(int(x))
			change()
		except KeyboardInterrupt:

		 	print('\nauto tor is closed ')
		 	quit()

else:
	for i in range(int(lin)):
		    time.sleep(int(x))
		    change()
