from graph_utiles import *
visited={}
def DFS_rec(graph,n,t):
    global visited
    visited[n]=True
    
    if n == t:
        return True
    for v in graph.neighbours(n):
        if not v in visited:
            if DFS_rec(graph,v,t):
                return True
    return False

def DFS_ite(graph,s,t):
    reached={}
    pile=[s]

    while len(pile)>0:
        #O(1)*V
        n=pile.pop(-1)  
        if n == t:
            return True
        
        #O(neighbours)*E
        for v in graph.neighbours(n): 
            if not v in reached:
                reached[v]=True
                pile.append(v)
    
    return False


if __name__=="__main__":
    graph=graph_test_BFS_DFS()
    visited={}
    print(DFS_rec(graph,0,8))
    print(DFS_ite(graph,0,8))
