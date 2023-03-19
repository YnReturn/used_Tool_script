import os
import shutil
import math

dir = os.listdir('./')

def moveDir(dir : list):
    for i in range(0,round((len(dir)/500))):
        for j in range(0,500):
            if(os.path.exists("./No" + str(i))):
                shutil.move(dir[j + i*500], "./No" + str(i))
            else:
                os.mkdir("./No" + str(i))
                shutil.move(dir[j + i*500], "./No" + str(i))
moveDir(dir)
