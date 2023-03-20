import os
Dirlist = os.listdir("./")

for file in Dirlist:
    tmp = file.replace("exe", "rar")
    os.rename(file, tmp)
