import math
import numpy as np

def BellmanFord(graph,t):
    ####### Inputs ##########
    n = len(graph)
    ####### Output ##########
    # init the table
    OPT = np.empty([n,n], dtype = object)

    OPT = [[1 for _ in range(n)]for _ in range(n)]
    OPT[0][t-1]=1

    # Dynamic table
    for i in range(1,n):
        for j in range(1,n-1):
            OPT[i][j] = OPT[i-1][j]
            for u in range(n):
                if u+1 in graph[j+1] and graph[j+1][u+1] != None and OPT[i][j]<OPT[i-1][u]*graph[j+1][u+1]:
                    OPT[i][j] = OPT[i-1][u]*graph[j+1][u+1]
 
    return OPT

if __name__ == "__main__":
    graph={
    1:{2:1,3:2},
    2:{3:1,4:4},
    3:{4:1,5:1},
    4:{5:1,6:2},
    5:{6:1,7:6},
    6:{7:1,8:2},
    7:{8:1,9:2},
    8:{9:1,10:4},
    9:{10:1,11:1},
    10:{11:1,12:4},
    11:{12:1},
    12:None
    }
    print(BellmanFord(graph,12))