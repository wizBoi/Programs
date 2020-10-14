import socket
import os
import json

os.system('title Know your IP')
info={}
info['host']=[]
info['host'].append({"Host Machine: " : socket.gethostname()})
print("\033[1;34;40mHost Machine: \033[0m", socket.gethostname())

print("\033[1;34;40mHost IP: \033[0m", socket.gethostbyname(socket.gethostname()))
info['host'].append({"Host IP: " : socket.gethostbyname(socket.gethostname())})
with open('info.txt', 'w') as outfile:
    json.dump(info, outfile)

print("\nDetails have been written to a JSON file.\n" )

os.system("PAUSE")