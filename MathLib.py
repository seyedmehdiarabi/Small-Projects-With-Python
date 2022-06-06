import math
from typing import Concatenate
list1= [1,2,3,4,5,6,7,8,9,10,11]
if (a:=len(list1)) > 10:
    print(f"list1 ={a}")

print("---------------------------------------------")

def myF(*kids):
    print(kids[-1])
    for i in kids:
        print(i)

myF('ali','mahdi','fatemeh')

print("---------------------------------------------")

def concatenate(**kids):
    print(kids)
concatenate(ali='real',b="python",c="Is",d="Great",e="!")

print("---------------------------------------------")

Adam = 12
def xx(Adam):
    Adam +=1
    print(Adam)

xx(Adam)
print(Adam)


print("Hello World!")
