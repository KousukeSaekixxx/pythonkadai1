#-------------------------------------------------------------------------------
# Name:        module8
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
x=int(input("あなたの番号を入力してください"))
if x%2==0:
    if x%4==0:
        print("4の倍数です")
    else:
        print("偶数です")
else:
    print("奇数です")