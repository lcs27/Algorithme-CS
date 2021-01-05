import numpy as np
import math
from TD5_2_2 import *

def dyn_sol(skis, customers):
 
    ####### Inputs ##########
    n = len(skis) # n pairs of ski
    m = len(customers) # m customers
 
    # sort and index the skis and customers depending on their size
    # the trick "['_'] +" is to start indexing from 1 (not 0)
    # S[i] gives the key of the i-th ski in the ascending order of their sizes
    # C[j] gives the key of the j-th customer in the ascending order of their sizes
    S = ['_'] + sorted(list(skis.keys()), key = lambda s: skis[s])
    C = ['_'] + sorted(list(customers.keys()), key = lambda c: customers[c])

    print(S)
    ####### Output ##########
    # init the table
    Sol = np.empty([n+1,m+1], dtype = object)
 
    ############### TODO : complete code #####################    

    #Init the base case
    for i in range(n+1):
        Sol[i][0]=0
    for j in range(1,m+1):
        Sol[0][j]=math.inf

    # Dynamic table
    for j in range(1,m+1):
        for i in range(1,n+1):
            Sol[i][j]=min(Sol[i-1][j],Sol[i-1][j-1]+abs(skis[S[i]]-customers[C[j]]))
 
    return Sol, S, C
 
####### Testing #########

dyn_table, _ ,  _ = dyn_sol(skis, customers)
print(dyn_table)
dyn_cost = dyn_table[-1][-1]                    # the cost is the last cell of the table
assert dyn_cost == 23                  
print("Dynamic programming -- cost:", dyn_cost) 
 
# greedy is far from optimal
skis2 = {'s1':170, 's2':140}
customers2 = {'c1':160, 'c2':200}
greedy_cost2 = mapping_cost(skis2, customers2, greedy_map(skis2, customers2))
dyn_cost2 = dyn_sol(skis2, customers2)[0][-1][-1]
assert greedy_cost2 == 70
assert dyn_cost2 == 50

def dyn_map(dyn_solution):
    Sol, S, C = dyn_solution

    n = len(S) # n pairs of ski
    m = len(C) # m customers
    mapping = {}
    ############### TODO : complete code #####################
    for j in range(1,m+1):
        for i in range(1,n+1):
            if Sol[i][j] != Sol[i-1][j]:
                mapping[C[i]]=S[j]
            print(mapping)
    return mapping
 
####### Testing #########
dyn_mapping = dyn_map(dyn_sol(skis, customers))
print("Dynamic programming -- mapping:", dyn_mapping)
assert mapping_cost(skis, customers, dyn_mapping) == dyn_cost
 
dyn_mapping2 = dyn_map(dyn_sol(skis2, customers2))
assert dyn_mapping2 ==  {'c2': 's1', 'c1': 's2'}