##find out Python version installed##
from platform import python_version
print("Current Python Version is:", python_version())

###find out Django version installed##
import django
django.VERSION
print("django version is:",django.VERSION)

#from subprocess import Popen
import subprocess
command = ["pip","list"]
subprocess.run(command)