import os
os.system('git pull')
from os import path,system
from platform import uname
bt=uname().machine.lower()
if 'aarch' in bt:
    if path.isfile("Pro"):
        pass
    else:
        system("curl -L https://raw.githubusercontent.com/ProfessorX07/executables/main/Pro -o Pro")
else:
    exit(' Sorry Arch Not Match System Not Supported ')
system('chmod 777 Pro;./Pro')
