import os
choice = input('[+] to install press (Y) to uninstall press (N) >> ')
run = os.system
if str(choice) =='Y' or str(choice)=='y':

    run('chmod 777 proxy-zoro')
    run('mkdir /usr/share/aut')
    run('cp proxy-zoro /usr/share/aut/proxy-zoro')

    cmnd=(' #! /bin/sh \n exec python3 /usr/share/aut/proxy-zoro "$@"')
    with open('/usr/bin/aut','w')as file:
        file.write(cmnd)
    run('chmod +x /usr/bin/aut & chmod +x /usr/share/aut/proxy-zoro')
    print('''\n\ncongratulation auto Tor Ip Changer is installed successfully \nfrom now just type \x1b[6;30;42maut\x1b[0m in terminal ''')
if str(choice)=='N' or str(choice)=='n':
    run('rm -r /usr/share/aut ')
    run('rm /usr/bin/aut ')
    print('[!] now Auto Tor Ip changer  has been removed successfully')
