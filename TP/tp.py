import tkinter as tk
import random
import math
from heapq import *
import matplotlib.pyplot as plt
from timeit import timeit

#################################################### Introduction ####################################################
# read the map file
def read_map(filename):
    f = open(file=filename, mode='r', encoding='utf-8')
 
    map = {}
    while True:  # reading list of cities from file
        ligne = f.readline().rstrip()
        if (ligne == '--'):
            break
        info = ligne.split(':')
        map[info[0]] = {'coords': (int(info[1]), int(info[2])), 'next':{}}
 
    while True:  # reading list of distances from file
        ligne = f.readline().rstrip()
        if (ligne == ''):
            break
        info = ligne.split(':')
        map[info[0]]['next'][info[1]] = int(info[2])
        map[info[1]]['next'][info[0]] = int(info[2])
 
    return map


toy_map = { 'A': {'coords': (100, 100), 'next': {'B': 140, 'E': 200, 'F': 200}}, 
            'B': {'coords': (200, 140), 'next': {'A': 140, 'C': 260, 'F': 140}}, 
            'C': {'coords': (360,  40), 'next': {'B': 260, 'D': 360}}, 
            'D': {'coords': (320, 360), 'next': {'C': 360, 'F': 280}}, 
            'E': {'coords': ( 80, 280), 'next': {'A': 200, 'F': 120}}, 
            'F': {'coords': (160, 240), 'next': {'A': 200, 'B': 140, 'D': 280, 'E': 120}} }

# Draw the map by tkinter
def draw_map(map, hospitals = [], l = 800, h = 800):
    w = tk.Tk()
    c = tk.Canvas(w, width=l, height=h)
 
    for city in map:
        for vname in map[city]['next']:
            if city < vname:
                x1 , y1 = map[city]['coords']
                x2 , y2 = map[vname]['coords']
                c.create_line(x1, y1, x2, y2, dash=True)
                c.create_text((x1+x2)//2, (y1+y2)//2, text=map[city]['next'][vname])
 
    for city in map:
        x , y =  map[city]['coords']
        color = 'red' if city in hospitals else 'black' 
        c.create_rectangle(x-5, y-5, x+5, y+5, fill=color)
        c.create_text(x+12, y+12, text=city)
 
    c.pack()
    w.mainloop()
 
# Generate a random grid map no dense
def random_grid_map (n, step):
    map = {f'{i}_{j}': {'coords':(j*step,i*step), 'next':{}} for i in range(1, n+1) for j in range(1, n+1)}
 
    for i in range(1, n+1):
        for j in range(1, n):
            d = random.randint(step+1, 2*step)
            map[f'{i}_{j}']['next'][f'{i}_{j+1}'] = d
            map[f'{i}_{j+1}']['next'][f'{i}_{j}'] = d
 
    for i in range(1, n):
        for j in range(1, n+1):
            d = random.randint(step+1, 2*step)
            map[f'{i}_{j}']['next'][f'{i+1}_{j}'] = d
            map[f'{i+1}_{j}']['next'][f'{i}_{j}'] = d
 
    return map


#################################################### Question 1 ####################################################
def random_dense_map(n, d_max):
    map = {f'{i}': {'coords':(random.randint(0, d_max),random.randint(0, d_max)), 'next':{}} for i in range(1, n+1)}
 
    for i in range(1, n+1):
        for j in range(i+1, n+1):
            d = random.randint(0, d_max)
            map[f'{i}']['next'][f'{j}'] = d
            map[f'{j}']['next'][f'{i}'] = d
 
    return map

#################################################### Question 2 ####################################################

# Main function
def PCCs_naive(graph,s):
    frontier = [s]
    dist = {s: 0}
 
    while len(frontier)>0:
 
        ### extraction du noeud de la frontière ayant la distance minimal    ###
        x = extract_min_dist(frontier,dist)
        frontier.remove(x)
        ### pour chaque voisin mise à jour de la frontière et de sa distance ###
        for y in neighbors(graph, x):
            if y not in dist.keys():
                frontier.append(y)
 
            new_dist = dist[x] + distance(graph,x,y)
            if y not in dist.keys() or dist[y] > new_dist:
                dist[y] = new_dist
    return dist

# Support function
def extract_min_dist(frontier,dist):
    min_noeud=None
    min_dist=math.inf
    for i in frontier:
        if dist[i]<min_dist:
            min_noeud=i
            min_dist=dist[i]
    return min_noeud

def neighbors(graph, x):
    return list(graph[x]['next'].keys())

def distance(graph,x,y):
    if y in graph[x]['next'].keys():
        return graph[x]['next'][y]
    else:
        return math.inf

#################################################### Question 3 ####################################################
def PCCs_heap(map, s):
    dist = {s: 0}
    frontier = [(0,s)]
    heapify(frontier)
    visited=set()
 
    while len(frontier)>0:
        ### extraction du noeud de la frontière ayant la distance minimal    ###
        x = heappop(frontier)[1]
        if x not in visited:
            visited.add(x)
            ### pour chaque voisin mise à jour de la frontière et de sa distance ###
            for y in neighbors(map, x): 
                new_dist = dist[x] + distance(map,x,y)
                if y not in dist.keys() or dist[y] > new_dist:
                    dist[y] = new_dist
                    heappush(frontier, (new_dist,y))
    return dist
# Remarque: Pour savoir si un noeud a déjà été extrait, utilisez un ensemble ou un dictionnaire Python pour avoir une recherche en O(1). Si vous utilisez une simple liste la recherche coûtera O(|V|)!
#################################################### Question 4 ####################################################
def all_distances(map, PCCs = PCCs_heap):
    all_distance_dict={}
    for i in map.keys():
        dist=PCCs(map,i)
        for j in map.keys():
            all_distance_dict[(i,j)]=dist[j]
    return all_distance_dict

#################################################### Question 5 ####################################################
# This function is given by the professor.
def benchmark():
    Time_heap_grid = []
    Time_naive_grid = []
    Time_heap_dense = []
    Time_naive_dense = []
 
    n_list = []
 
    for N in range(10,30):
        print(N) # pour voir que ça avance!
 
        n = N*N
        n_list.append(n)
 
        # on compare sur des cartes non-denses: grille de côté N contient N*N villes
        map_grid = random_grid_map(n = N, step = 100)
 
        # on calcule une moyenne sur N lancements en tirant aléatoirement une ville de départ à chaque fois
        Time_naive_grid.append(timeit(lambda: PCCs_naive(map_grid, random.choice(list(map_grid))), number=N) / N)
        Time_heap_grid.append(timeit(lambda: PCCs_heap(map_grid, random.choice(list(map_grid))), number=N) / N)
 
        # on compare sur des cartes denses
        map_dense = random_dense_map(n = N*N, d_max = 10000)
 
        Time_naive_dense.append(timeit(lambda: PCCs_naive(map_dense, random.choice(list(map_dense))), number=N) / N)
        Time_heap_dense.append(timeit(lambda: PCCs_heap(map_dense, random.choice(list(map_dense))), number=N) / N)
 
    plt.subplot(2, 1, 1)
    plt.xlabel('N')
    plt.ylabel('T')
    plt.plot(n_list, Time_naive_grid, 'r^', label='naive grid')
    plt.plot(n_list, Time_heap_grid, 'b^', label='heap grid')
    plt.legend()
 
    plt.subplot(2, 1, 2)
    plt.xlabel('N')
    plt.ylabel('T')
    plt.plot(n_list, Time_naive_dense, 'r*', label='naive dense')
    plt.plot(n_list, Time_heap_dense, 'b*', label='heap dense')
    plt.legend()
 
    plt.show()

# Conclusion sur la complexité:
#   En cas peu dense, naive n'explose pas? 
#       la frontiere n'est rarement trop occupé, la taille moyenne de frontiere est petite.
#       Conseil: Conteur pour taille de frontiere
#   En cas dense, pourquoi pas V^2logV?
#       update n'est presque pas executé E fois, difficile de toujours améliorer chaque fois, pas mettre à toujours autant que ça
#       Conseil: Conteur pour update
#################################################### Question 6 ####################################################

def all_combis(candidates):
    n=len(candidates)
    for i in range(0,pow(2, n)):
        answer=[]
        k = i
        for j in range(0,n):
            if k % 2 == 1:
                answer.append(candidates[j])
            k = k // 2
        print(i,answer)

#################################################### Question 7 ####################################################
def all_combis_k(candidates,k):
    n=len(candidates)
    for i in range(0,pow(2, n)):
        answer=[]
        q = i
        for j in range(0,n):
            if q % 2 == 1:
                answer.append(candidates[j])
            q = q // 2
        if len(answer) == k:
            yield answer
#################################################### Question 8 ####################################################
def voisins(node_combi):
    choisi=node_combi[0]
    candidat=node_combi[1]
    while len(candidat)>0:
        i=candidat.pop()
        choisi.append(i)
        yield choisi,candidat
        choisi.pop()

#################################################### Question 9 ####################################################

def combi_gen(candidates):
    frontier=[([],candidates)]
    while len(frontier)>0:
        a=frontier.pop(0)
        for i,j in voisins(a):
            frontier.append((i.copy(),j.copy()))
            yield i

#################################################### Question 10 ###################################################
def combi_gen_k(candidates,k=1):
    frontier=[([],candidates)]
    while len(frontier)>0:
        a=frontier.pop(0)
        for i,j in voisins(a):
            frontier.append((i.copy(),j.copy()))
            if len(i) == k:
                yield i
            elif len(i) > k:
                break
################################################# Check Functions ##################################################
# This part is given by the professor.

def check_map(map, complete=False):
    for city in map:
        for voisin in map[city]['next']:
            if voisin not in map:
                print('Error : Le voisin', voisin, 'de la ville', city, 'n existe pas')
                return False
            if city not in map[voisin]['next']:
                print('Error : La ville', city, 'et la ville', voisin, 'ne sont pas voisines reciproquement')
                return False
            if map[city]['next'][voisin] != map[voisin]['next'][city]:
                print('Error : La ville', city, 'et la ville', voisin, 'ne sont pas a la meme distance reciproquement')
                return False
        if complete:
            if len(map[city]['next']) < len(map) - 1:
                print('Error : Le graphe n est pas complet, il manque des voisins au noeud :', city)
                return False
    return True
 
def Q_1():
    complete_map = random_dense_map(10,500)
    assert len(complete_map) == 10 and check_map(complete_map, complete=True) 
    draw_map(complete_map)
    print('Question 1 Passed')

def Q_2():
    assert PCCs_naive(toy_map, 'A') == {'A': 0, 'B': 140, 'E': 200, 'F': 200, 'C': 400, 'D': 480}
    print('Question 2 Passed')

def Q_3():
    assert PCCs_heap(toy_map, 'A') == {'A': 0, 'B': 140, 'E': 200, 'F': 200, 'C': 400, 'D': 480}
    print('Question 3 Passed')

def Q_4():
    assert all_distances(toy_map) == {('A', 'A'):   0, ('A', 'B'): 140, ('A', 'C'): 400, ('A', 'D'): 480, ('A', 'E'): 200, ('A', 'F'): 200, 
                                  ('B', 'A'): 140, ('B', 'B'):   0, ('B', 'C'): 260, ('B', 'D'): 420, ('B', 'E'): 260, ('B', 'F'): 140, 
                                  ('C', 'A'): 400, ('C', 'B'): 260, ('C', 'C'):   0, ('C', 'D'): 360, ('C', 'E'): 520, ('C', 'F'): 400,
                                  ('D', 'A'): 480, ('D', 'B'): 420, ('D', 'C'): 360, ('D', 'D'):   0, ('D', 'E'): 400, ('D', 'F'): 280,
                                  ('E', 'A'): 200, ('E', 'B'): 260, ('E', 'C'): 520, ('E', 'D'): 400, ('E', 'E'):   0, ('E', 'F'): 120, 
                                  ('F', 'A'): 200, ('F', 'B'): 140, ('F', 'C'): 400, ('F', 'D'): 280, ('F', 'E'): 120, ('F', 'F'):   0}
 
    map_grid = random_grid_map(10,100)
    assert all_distances(map_grid, PCCs_heap) == all_distances(map_grid, PCCs_naive)
 
    map_dense = random_dense_map(100,1000)
    assert all_distances(map_dense, PCCs_heap) == all_distances(map_dense, PCCs_naive)
    print('Question 4 Passed')

def Q_5():
    benchmark()
    print('Question 5 Finished')

def Q_6():
    all_combis(['A','B','C'])
    print('Question 6 Finished')

def Q_7():
    for combi in all_combis_k(['A','B','C','D'], k=2):
        print(combi)
 
    fake_candidates = [f'city{i}' for i in range(50)]
    for combi in all_combis_k(fake_candidates, k=1):
        print(combi)
    print('Question 7 Finished')

def Q_8():
    for v in voisins((['A','C'], ['B','D','E'])):
        print(v)
    print('Question 8 Finished')

def Q_9():
    for combi in combi_gen(['A','B','C','D']):
        print(combi)
    print('Question 9 Finished')

def Q_10():
    for combi in combi_gen_k(['A','B','C','D'], k=2):
        print(combi)
 
    fake_candidates = [f'city{i}' for i in range(50)]
    for combi in combi_gen_k(fake_candidates, k=1):
        print(combi)
    print('Question 10 Finished')

####################################################### Main ########################################################
if __name__=="__main__":

    ## Introduction Part
    '''
    assert read_map('territoire_jouet.map') == toy_map
    draw_map(toy_map, ['A', 'C']) # pensez à commenter cette ligne après le test
    draw_map(random_grid_map(5,100))
    print('Introduction Test Passed')
    '''

    ## Questions
    #Q_1()
    #Q_2()
    #Q_3()
    #Q_4()
    #Q_5()
    #Q_6()
    #Q_7()
    #Q_8()
    #Q_9()
    Q_10()
