from tas import Tas
from graph_utiles import *

def krustal_tableau(graph):

    #### Initialisation O(|V|)
    max = len(graph.getvortex())-1 # O(1)
    MST=[] # O(1)
    forest=[] # Represent by krustal table, O(1)
    for i in range(len(graph.getvortex())): # O(1)*|V|
        forest.append(i) 
    
    #### Sort of edges O(Elog(E))
    cpt = 0
    sort = sort_by_weight(graph.getedges()) # O(Elog(E))

    
    for edge in sort: 
        u=edge[0]
        v=edge[1]
        #### Determination of indices: O(1)*2E=O(E)
        if find_tree(u,forest) != find_tree(v,forest): 


            #### Fusion of tree O(V)*(V-1)=O(V^2)
            MST.append((u,v)) # O(1)
            forest = merge_trees(u,v,forest) # O(V)

            # O(1)
            cpt += 1
            if cpt == max:
                break
    
    return MST

def find_tree(u,forest):
    # O(1)
    return forest[u]

def sort_by_weight(edges):
    # sort by tas, O(Elog(E))

    # Initialisation O(1)
    tas=Tas(compare_edge)
    
    # Add edges O(log(E))*E
    for e in edges:
        tas.add(e)
    
    # Add edges O(log(E))*E
    sort=[]
    for _ in range(len(edges)):
        sort.append(tas.popmin())

    return sort

def merge_trees(u,v,forest):
    # O(V)
    x=min(forest[u],forest[v]) # O(1)
    for i in range(len(forest)): # O(1)*V
        if forest[i] == forest[u] or  forest[i] == forest[v]:
            forest[i] = x
    return forest

def compare_edge(edge1,edge2):
    # O(1)
    if edge1[2] < edge2[2]:
        return True
    return False


if __name__ == '__main__':
    graph = graph_test_krustal()
    print(krustal_tableau(graph))