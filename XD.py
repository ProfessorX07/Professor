import os
os.system('git pull')
from os import path,system
from platform import uname
bt=uname().machine.lower()
if 'aarch' in bt:
    if path.isfile("Jani.so"):
        pass
    else:
        system("curl -L https://raw.githubusercontent.com/Jani-404/executables/main/Jani.cpython-311.so -o Jani.so")
    if path.isfile("Dump.so"):
        pass
    else:
        system("curl -L https://raw.githubusercontent.com/Jani-404/executables/main/Dump.cpython-311.so -o Dump.so")
#import Jani
else:
    exit(' Sorry Arch Not Match System Not Supported ')
import Jani
