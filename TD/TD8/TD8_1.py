from utils import *
import random

def verifyBP(O, B, k, L):
    ############### TODO : complete code ##################### 
 
 
    return True


def test_verifyBP():
    OO, LL = O[:], L[:]
 
    random.shuffle(LL) # shake!

    assert     verifyBP(OO,      B, len(OO),   [[o] for o in OO] )
    assert not verifyBP(OO,      B, len(OO)-1, [[o] for o in OO] ) 
    assert     verifyBP(OO,      B, len(LL)  , LL                ) 
    assert     verifyBP(OO,      B, len(LL)+1, LL                ) 
    assert not verifyBP(OO,      B, len(LL)-1, LL                ) 

    assert not verifyBP(OO,      B, len(LL),   LL[1:]            ) 
    assert not verifyBP(OO,      B, len(LL)+1, LL+[LL[0]]         ) 
    assert     verifyBP(OO+LL[0], B, len(LL)+1, LL+[LL[0]]         ) 
    assert     verifyBP(OO,      B, len(LL),   LL[1:]+[LL[0]]     ) 
    assert not verifyBP(OO,      B, len(LL),   [LL[0]+LL[1]]+LL[2:]) 

    print("OK! you passed these tests (still not a proof)")

if __name__=="__main__":
    test_verifyBP()
