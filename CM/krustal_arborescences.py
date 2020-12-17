from tas import Tas
from graph_utiles import *

def krustal_arborescences(graph):

    #### Initialisation O(|V|)
    max = len(graph.vortex)-1 # O(1)
    MST=[] # O(1)
    forest=[] # Represent by arborescences, see https://fr.wikipedia.org/wiki/Union-find
    for v in graph.vortex: # O(1)*|V|
        forest.append(v)
    
    #### Sort of edges O(Elog(E))
    cpt = 0
    sort = sort_by_weight(graph.edges) # O(Elog(E))

    for edge in sort: 
        u=edge[0]
        v=edge[1]
        #### Determination of indices: O(log(V))*E=O(Elog(V))
        if find_tree(u,forest) != find_tree(v,forest): 


            #### Fusion of tree O(log(V))*(V-1)=O(Vlog(V))
            MST.append((u,v)) # O(1)
            forest = merge_trees(u,v,forest) # O(log(V))

            # O(1)
            cpt += 1
            if cpt == max:
                break
    
    return MST

def find_tree(u,forest):
    # O(1) for each, with depth O(log(V))
    if forest[u] == u:
        return u
    else:
        forest[u] = find_tree(forest[u],forest)
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
    #O(log(V))
    fu = find_tree(u,forest) #O(log(V))
    fv = find_tree(v,forest) #O(log(V))
    if fu != fv:
        forest[fu]=fv #O(1)
    return forest

def compare_edge(edge1,edge2):
    # O(1)
    if edge1[2] < edge2[2]:
        return True
    return False


if __name__ == '__main__':
    graph = graph_test_krustal()
    print(krustal_arborescences(graph))