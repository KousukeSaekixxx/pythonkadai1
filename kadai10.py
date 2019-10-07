#-------------------------------------------------------------------------------
# Name:        module10
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
a=[1,4,9,16,25,36,49,64,81,100]
b=filter(lambda x: x%2==0,a)
print(list(b))