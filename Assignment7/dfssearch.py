from os import listdir
from os.path import isfile, join, isdir
def show_directories(wdList):

    while wdList:
        x = wdList[0]
        wdList = wdList[1:]
        xList = [join(x,f) for f in listdir(x) if isdir(join(x,f))]
        if xList:
            wdList = xList = wdList


wd = input("working directory: ")
wdList = [join(wd,f) for f in listdir(wd) if isdir(join(wd,f))]

show_directories(wdList)
