#-------------------------------------------------------------------------------
# Name:        module9
# Purpose:
#
# Author:      kousuke saeki
#
# Created:     02/10/2019
# Copyright:   (c) kousuke saeki 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()
print("回文を入力して下さい")
kaibun = input("")
def first(kaibun):
    return kaibun[0]
def last(kaibun):
    return kaibun[-1]
def middle(kaibun):
    return kaibun[1:-1]
def palindromic(kaibun):
    return kaibun == kaibun[::-1]
palindromic(kaibun)