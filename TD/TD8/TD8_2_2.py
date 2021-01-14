from utils import *
from TD8_1 import *

def best_fit(O, B):
    L = []
    ############### TODO : complete code ##################### 
 
 
    return L
 
# Tests
def test_BF_petit():
    L_BF = best_fit(O, B)
    print(len(L_BF), "bins:", L_BF) # >>> 12 bins: ...
    assert len(L_BF) == 12
 
# what if we sort objects in descending order?
def test_BFD_petit():
    L_BFD = best_fit(sorted(O,reverse = True), B)
    print(len(L_BFD), "bins:", L_BFD) # >>> 11 bins: ... # OPTIMAL!!
    assert len(L_BFD) == sum(O)//B

def test_BFD_grand():
    LL = best_fit(OO,BB)
    assert len(LL) == round(sum(OO)/BB) # >>> OPTIMAL!!

if __name__=="__main__":
   test_BF_petit()
   test_BFD_grand()
   test_BFD_grand()