from utils import *
from TD8_1 import *

def first_fit(O, B):
    L = []
    ############### TODO : complete code #####################     for o in O:
 
 
    return L
 
# Tests
def test_FF_petit():
    L_FF = first_fit(O, B)
    assert len(L_FF) == 13
    print(len(L_FF), "bins:", L_FF) # >>> 13 bins: ...

def test_FFD_petit():
    L_FFD = first_fit(sorted(O,reverse = True), B)
    print(len(L_FFD), "bins:", L_FFD) # >>> 11 bins: ... 
    if len(L_FFD) == round(sum(O)/B):
        print("OPTIMAL!!") # >>> OPTIMAL!!

def test_FFD_grand():
    OO, BB = big_instance() # OO is already sorted in descending order
    LL = first_fit(OO,BB)
    assert len(LL) == 89 # >>> 89 bins # NOT OPTIMAL!!

if __name__=="__main__":
   test_FF_petit()
   test_FFD_grand()
   test_FFD_grand()