from utils import *
import numpy as np
import matplotlib.pyplot as plt
from timeit import timeit
from random import randint
from TD6_1_3 import backtracking
from TD6_1_6 import branchbound
def Knapsack_DP(O_dict, W):
 
    n = len(O_dict)
    objs_list = sorted(O_dict.keys())
 
    # FILLING THE TABLE ITERATIVELY
    V = np.zeros((n+1, W+1), dtype='int32')
 
    ############### TODO : complete code ####################
    for i in range(1,n+1):
        vi=O_dict[objs_list[i-1]]['v']
        wi=O_dict[objs_list[i-1]]['w']
        for j in range(1,W+1):
            if j >= wi:
                V[i,j]=max(V[i-1,j],V[i-1,j-wi]+vi)
            else:
                V[i,j]=V[i-1,j]

    # RETRIEVE THE SOLUTION
    selected = set()
    ############### TODO : complete code ####################        
    j=W
    i=n
    while j>0:
        while i>0:
            vi=O_dict[objs_list[i-1]]['v']
            wi=O_dict[objs_list[i-1]]['w']
            
            if V[i,j] != V[i-1,j] and V[i,j] == V[i-1,j-wi]+vi:
                selected = selected.union({objs_list[i-1]})
                j -= wi
                i -= 1
                break
            else:
                i -= 1
        else:
            j -= 1

    return {'selected': selected, 'score': V[n,W]}
def random_instance(N):
    W = N**2
    O = {f'o{i}': {'w': randint(1,N**2), 'v': randint(1,N**2)} for i in range(1,N+1)}
    return W, O

def benchmark():
    Time_basic = []
    Time_branching = []
    Time_DP = []
 
    n_list = []
 
    for N in range(30, 50):
        print(N)
        n_list.append(N)
 
        # some random instance of size N
        W, O_dict = random_instance(N)
 
        Time_basic.append(timeit(lambda : backtracking(O_dict, W), number=1))
        Time_branching.append(timeit(lambda : branchbound(O_dict, W), number=1))
        Time_DP.append(timeit(lambda :Knapsack_DP(O_dict, W), number=1))
        a=branchbound(O_dict, W)
        assert backtracking(O_dict, W)['score']==a['score']
        assert a['score']==Knapsack_DP(O_dict, W)['score']
 
    plt.xlabel('N')
    plt.ylabel('T')
    plt.plot(n_list, Time_basic, 'r^', label='back tracking')
    plt.plot(n_list, Time_branching, 'b^', label='branch & bound')
    plt.plot(n_list, Time_DP, 'y^', label='Dynamic Programming')
 
    plt.legend()
    plt.show()

def test():
    print("--- DYNAMIC PROGRAMMING ---")
    bestSol4 = Knapsack_DP(O4, W4)
    print('--- simple case : 4 objects --- best found solution {} of value {}'.format(bestSol4['selected'], bestSol4['score']))
    assert bestSol4['score'] == 35
    assert bestSol4['selected'] == {'o2', 'o3'}
 
    bestSol15 = Knapsack_DP(O15, W15)
    print('--- bigger case : 15 objects --- best found solution {} of value {}'.format(bestSol15['selected'], bestSol15['score']))
    assert bestSol15['score'] == 1458
    assert bestSol15['selected'] == {'o1', 'o3', 'o5', 'o7', 'o8', 'o9', 'o14', 'o15'}
    print('Test finished')

if __name__=="__main__":
    #test()
    #benchmark()
    