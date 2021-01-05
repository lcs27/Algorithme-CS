import math
####### Inputs example ##########
skis = {'s1':170, 's2':180, 's3':170, 's4':155, 's5':175, 's6':175, 's7':160, 's8':190} # available skis
customers = {'c1':186, 'c2':173, 'c3':150, 'c4':200} # skiers heights
 
def greedy_map(skis, customers):
    # better work on copies
    S = skis.copy()
    C = customers.copy()
 
    mapping = {}
    ############### TODO : complete code #####################

    while len(C)>0:
        # Find the min
        minimum = math.inf     
        min_i=0
        min_j=0
        for i in S.keys():
            for j in C.keys():
                if abs(S[i]-C[j])<minimum:
                    minimum,min_i,min_j=abs(S[i]-C[j]),i,j
        
        # Add the min
        mapping[min_j]=min_i
        C.pop(min_j)
        S.pop(min_i)
    return mapping
 
####### Testing #########
# to compute the cost of a mapping (i.e. the sum of size differences)
def mapping_cost(skis, customers, mapping):
    return sum([abs(customers[c] - skis[mapping[c]]) for c in customers])
 
greedy_mapping = greedy_map(skis, customers)
greedy_cost = mapping_cost(skis, customers, greedy_mapping)
 
print("GREEDY -- mapping:", greedy_mapping, "cost:", greedy_cost)
assert greedy_cost == 31