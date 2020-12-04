from utils import *
def coloring(V,E,s,t):
    color = { s:0 }
    
    def color_rec(E,n,t):
        for v in neighbours(n,E):
            if not v in color:
                color[v] = 1 - color[n]
                if not color_rec(E,v,t):
                    return False
            elif color[v] == color[n]:
                return False    
        
        return True
    
    return color, color_rec(E,s,t)