#-------------------------------------------------------------------------------
# Name:        module7
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
print("名前を入力してください")
name=input("名前")
print("年齢を入力してください")
old=input("年齢")
print(name+"さんが100歳になる年は",(100-int(old))+2019)