#-------------------------------------------------------------------------------
# Name:        module4
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
print("借金の総額を入力してください")
a=int(input("借金の総額="))
print("ひと月に返済する金額を入力してください")
b=int(input("返済金額="))
print("返済にかかる年数は{}年".format((a/b)/12))
print("ボーナスから返済する金額を入力してください")
c=int(input("ボーナス返済金額="))
print("返済完了が{}年早まります".format((c*(a/b)/12)/b/12))
print("返済を完了したい年数を入力してください")
d=int(input("返済完了年数="))
print("ボーナスから{}円返せばよい".format((a-(b*12*d))/12))
