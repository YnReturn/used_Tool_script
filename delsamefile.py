#这个不具有普遍性,针对于特殊性,由于特殊性需要进行递归形式的判断,可能速度比较慢,所以为了方便针对于特殊
#情况进行处理
import os
# import re

def getfile():
    return os.listdir('./')

def checkSame(file):
    # re.search()
    flag = file[-6:-3]
    if flag == " 2.":
        print("if!!!    delete ... " + file)
        os.remove(file)
    else:
        print("else!!!     pass ... " + file)
        pass
def main():
    fileList = getfile()
    for i in fileList:
        checkSame(i)

main()


