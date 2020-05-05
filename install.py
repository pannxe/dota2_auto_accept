import os
import sys

if os.name == "nt":
    os.system("install/install.bat")
else :
    os.system("sudo chmod +x ./install/install.bash")
    os.system("sudo ./install/install.bash")