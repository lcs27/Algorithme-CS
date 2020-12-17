from graph_utiles import *
from tas import Tas
def PCC_liste(graph,s):
    return NotImplementedError
    '''
    # Initialization O(1)
    tas=Tas(compare_distance)
    tas.add([s,0,None])
    parent={}
    parent[s]=None
    distance={}
    distance[s]=0

    while tas.len()>0:
        # Get the shortest point in frontiere O(extract_min)*E
        shortest,tas = extract_min_dist(tas)#O(extract_min)=O(n)
        x=shortest[0]
        parent[x]=shortest[1]
        distance[x]=shortest[2]
        

        for y in graph.neighbours(x):

            # Add neighborhood O(E)
            if y not in parent:
                tas.add([y,distance[y],parent[y]])
            
            # Update distance O(update)*E O(update)=O(1)
            new_dist = distance[x]+graph.getdistance(x,y)
            if y not in distance or distance[y] > new_dist:
                distance[y] = new_dist
                parent[y] = x
    return parent,distance



def compare_distance(vortex1,vortex2):
    # O(1)
    if vortex1[1] < vortex2[1]:
        return True
    return False

def extract_min_dist(tas):
    return tas.popmin(),tas
    
    

if __name__=="__main__":
    graph=graph_test_PCC()
    print(PCC_liste(graph,3))