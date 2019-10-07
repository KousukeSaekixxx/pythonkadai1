#-------------------------------------------------------------------------------
# Name:        module6
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
num=input("num=")
if int(num)%7==0:
    print("numは7の倍数である")
else:
    print("numは7の倍数ではない")
if int(num)%3==0:
    print("numは3の倍数である")
else:
    print("numは3の倍数ではない")
if int(num)<0:
    print("numは負の数である")
else:
    print("numは負の数ではない")
