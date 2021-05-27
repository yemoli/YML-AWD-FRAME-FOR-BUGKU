# -*- coding:utf-8 -*-#
class bcolor(object):
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

# green
def printGreen(mess):
    print(bcolor.OKGREEN + mess + bcolor.ENDC)


# red
def printRed(mess):
    print(bcolor.FAIL + mess + bcolor.ENDC)


# yellow
def printYellow(mess):
    print(bcolor.WARNING + mess + bcolor.ENDC)
