import os
os.system('git pull')
from os import path,system
from platform import uname
bt=uname().machine.lower()
if 'aarch' in bt:
    print('\033[1;34m\n Congratulations! Your Device Support This Tools\033[1;37m')
    if path.isfile("Jani.so"):
        pass
    else:
        system("curl -L https://raw.githubusercontent.com/Jani-404/executables/main/Jani.cpython-311.so -o Jani.so")
    if path.isfile("Dump.so"):
        pass
    else:
        system("curl -L https://raw.githubusercontent.com/Jani-404/executables/main/Dump.cpython-311.so -o Dump.so")
else:
    exit(' Sorry Arch Not Match System Not Supported ')
