import os
from time import sleep
import subprocess
cmd = "taskkill /IM PanGPA.exe /F"
cmd2 = 'tasklist |find "PanGPA.exe"'
while True:
  try:
    x = subprocess.check_output(cmd2, shell =True)
    os.system(cmd)
  except:
    pass
  sleep(2)

#while True:
# os.system(cmd)
# sleep(4)
