from TD4_2_1 import *
import time
A=[4,6,10,25,34,46]
B=[7,11,23,36,55]
C=[27,45,56,67]

a=A.pop(0)
b=B.pop(0)
c=C.pop(0)
tas_add(a)
tas_add(b)
tas_add(c)

total=[]

while a is not None or b is not None or C is not None and len(tas_min)>0:
    x=tas_popmin()
    total.append(x)
    if x == a:
        try:
            a = A.pop(0)
            tas_add(a)
        except:
            a = None
    elif x == b:
        try:
            b = B.pop(0)
            tas_add(b)
        except:
            b = None
    elif x == c:
        try:
            c = C.pop(0)
            tas_add(c)
        except:
            c = None
        
print(total)