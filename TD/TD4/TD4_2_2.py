from TD4_2_1 import *
import time
A=[4,6,10,25,34,46]
B=[7,11,23,36,55]
C=[27,45,56,67]

a=A.pop(0)
b=B.pop(0)
c=C.pop(0)
tas_add(c)
tas_add(b)
tas_add(a)

total=[]

while a is not None or b is not None or c is not None and len(tas_min)>0: # n
    x=tas_popmin() # O(log(p))
    total.append(x) # O(1)
    if x == a: # O(1)
        try:
            a = A.pop(0) # O(1)
            tas_add(a) # O(log(p))
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