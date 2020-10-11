#Bored of shutting down through the GUI?
#Powershell too much for you?
#Then this is the perfect script to shutdown or reboot your PC!

import os
import time

os.system('title SHUT ME DOWN       but with Python')

print(
    '\n\033[1;34;40m[1]\033[0m Shutdown Your PC \n\033[1;34;40m[2]\033[0m Restart Your PC'
)
userin = input('\n\033[1;32;40m>>\033[0m What would you like to do\033[1;32;40m?\033[0m')
if str(userin)=="1":
    os.system('title Systems going offline in 5 seconds')
    print('\033[1;35;40m Shutdown \033[0m Initiated.')
    time.sleep(5)
    os.system('shutdown.exe /s /t 00')
elif str(userin)=="2":
    os.system('title Commencing Reboot in 5 seconds')
    print('\033[1;35;40m Reboot \033[0m Initiated.')
    time.sleep(5)
    os.system('shutdown.exe /r /t 00')    
else:
    print('\n \033[1;31;40m Invalid Selection! \033[0m')
    os.system('PAUSE')
    os._exit(0)  


