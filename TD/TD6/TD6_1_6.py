from utils import *
import matplotlib.pyplot as plt
from timeit import timeit
from random import randint
from TD6_1_3 import backtracking
def branchbound(O_dict, W) :    
    global bestSol, objs_list
 
    # initialization
    bestSol = {'selected': set() , 'index':0, 'weight': 0, 'score': 0}
    ################################################## CHANGED ##################################################
    objs_list = sorted(O_dict.keys(),key=lambda x:O_dict[x]['v']/O_dict[x]['w'],reverse=True) # separations
    ################################################ CHANGED END ################################################
    # computes the children of the current partial solution
    def children(curParSol):
        childrenSols = []

        if curParSol['index'] < len(objs_list):
            # First presence
            childSol1 = curParSol.copy()
            toadd = objs_list[curParSol['index']]
            childSol1['weight'] += O_dict[toadd]['w']
            if childSol1['weight'] <= W:
                childSol1['selected'] = curParSol['selected'].union({toadd})
                childSol1['score'] += O_dict[toadd]['v']
                childSol1['index'] += 1
                childrenSols.append(childSol1)
            
            # Second abscence
            childSol2 = curParSol.copy()
            childSol2['index'] += 1
            childrenSols.append(childSol2)


        return childrenSols
 
    # a partial solution is terminal when it has no children
    def terminal(curParSol):
        return len(children(curParSol)) == 0
    
    ################################################## CHANGED ##################################################
    def bound(curParSol):
        weight = curParSol['weight']
        score = curParSol['score']
        for i in range(curParSol['index'],len(objs_list)):
            weight += O_dict[objs_list[i]]['w']
            score += O_dict[objs_list[i]]['v']
            if weight > W:
                break
        return score

    ################################################ CHANGED END ################################################
    def backtracking_rec(curParSol) :
        global objs_list, bestSol

        if terminal(curParSol) :
            if curParSol['score'] > bestSol['score'] :
                bestSol = curParSol.copy()
        ################################################## CHANGED ##################################################
        elif bound(curParSol) > bestSol['score']:
        ################################################ CHANGED END ################################################
            for parSol in children(curParSol):
                backtracking_rec(parSol)
 
    # call backtracking on the root node
    rootSol = {'selected': set() , 'index': 0, 'weight': 0, 'score': 0}
    backtracking_rec(rootSol)
 
    # return the best found solution (the index entry is no more relevent)
    bestSol.pop('index')
    return bestSol


## Test Function
# generates some random instance of size N
def random_instance(N):
    W = N**2
    O = {f'o{i}': {'w': randint(1,N**2), 'v': randint(1,N**2)} for i in range(1,N+1)}
    return W, O
 
def benchmark():
    Time_basic = []
    Time_branching = []
 
    n_list = []
 
    for N in range(30, 50):
        print(N)
        n_list.append(N)
 
        # some random instance of size N
        W, O_dict = random_instance(N)
 
        Time_basic.append(timeit(lambda: backtracking(O_dict, W), number=1))
        Time_branching.append(timeit(lambda: branchbound(O_dict, W), number=1))
 
    plt.xlabel('N')
    plt.ylabel('T')
    plt.plot(n_list, Time_basic, 'r^', label='back tracking')
    plt.plot(n_list, Time_branching, 'b^', label='branch & bound')
 
    plt.legend()
    plt.show()

def test():
    bestSol4 = branchbound(O4, W4)
    print('--- simple case : 4 objects --- \n best found solution {} of value {}'.format(bestSol4['selected'], bestSol4['score']))
    assert bestSol4['score'] == 35
    assert bestSol4['selected'] == {'o2', 'o3'}
 
    bestSol15 = branchbound(O15, W15)
    print('--- bigger case : 15 objects --- \n best found solution {} of value {}'.format(bestSol15['selected'], bestSol15['score']))
    assert bestSol15['score'] == 1458
    assert bestSol15['selected'] == {'o1', 'o3', 'o5', 'o7', 'o8', 'o9', 'o14', 'o15'}
    print('Test finished')

if __name__=="__main__":
    print('--- BRANCH ET BOUND ---')
    test()
    #benchmark()