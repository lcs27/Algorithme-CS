import math
class Graph:
    vortex=[]
    edges=[] #[u,v]
    def __init__(self,vortex,edges):
        self.vortex=vortex
        self.edges=edges

    def getvortex(self):
        return self.vortex
    
    def getedges(self):
        return self.edges

    def neighbours(self,n):
        neighbours=[]
        for i in self.vortex:
            for edge in self.edges:
                if (edge[0] == n and edge[1] == i) or (edge[0] == i and edge[1] == n):
                    neighbours.append(i)
        return neighbours

    def get_distance(self,x,y):
        for edge in self.edges:
                if (edge[0] == x and edge[1] == y) or (edge[0] == y and edge[1] == x):
                    return edge[2]
        return math.inf

    def get_direction_distance(self,x,y):
        for edge in self.edges:
                if edge[0] == x and edge[1] == y:
                    return edge[2]
        return math.inf