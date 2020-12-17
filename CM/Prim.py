from graph_utiles import *
def prim(graph,s):
    # Initialization O(1)
    frontiere=graph.vortex
    parent={}
    distance={}
    distance[s]=0

    while len(frontiere)>0:
        # Get the shortest point in frontiere O(extract_min)*E, O(extract_min)=O(n)
        x = extract_min_dist(frontiere,distance)
        frontiere.remove(x)
        for y in graph.neighbours(x):
            # Update distance O(update)*E, O(update)=O(1)
            new_dist = graph.get_distance(x,y)
            if y in frontiere and(y not in distance or distance[y] > new_dist):
                distance[y] = new_dist
                parent[y] = x
    
    return parent,distance

def extract_min_dist(frontiere,distance):
    # O(frontiere)=O(n)
    min_index = frontiere[0]
    for i in frontiere:
        if i in distance and min_index not in distance:
            min_index = i
        if i in distance and distance[i] <= distance[min_index]:
            min_index = i
    
    return min_index

if __name__=="__main__":
    graph=graph_test_krustal()
    print(prim(graph,1))