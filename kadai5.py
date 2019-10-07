#-------------------------------------------------------------------------------
# Name:        module5
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
print("数字を入力してください")
x=input("x=")
print("x+25000=",int(x)+25000)
print("num=",int(x)+25000)
if int(x)+25000 == 3500*9:
    print("numは3500*9と等しい")
else:
    print("numは3500*9と等しくない")