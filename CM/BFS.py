from graph_utiles import *
def BFS(graph,s,t):
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

def BFS_connex(graph,s):
    reached={}
    pile=[s]

    while len(pile)>0:

        #O(1)*V
        n=pile.pop(-1)
        
        #O(neighbours)*E
        for v in graph.neighbours(n):
            if not v in reached:
                reached[v]=True
                pile.append(v)
    
    return reached

if __name__=="__main__":
    graph=graph_test_BFS_DFS()
    print(BFS(graph,0,8))
    print(BFS_connex(graph,4).keys())