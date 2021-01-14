Le contenu de TP et les listes des attentions
- Exo1: Create a random map with dict
- Exo2: Write PCC algo with list
- Exo3: Write PCC algo with tas_min   
    **Attention 1** PCC need to update the distance dictionnary,which is impossible for tas, so we add previous times in the tas and we create a new set to detect the multiple visit of one point   
    **Attention 2** Here we use set or dictionary to have a research on O(1). If we use list, the research of element is on O(|V|)!
- Exo4: Get the dictionary of all distance
- Exo5: Complexity   
    **Attention 1**
    Conclusion sur la complexité:  
    En cas peu dense, naive n'explose pas?    
        la frontiere n'est rarement trop occupé, la taille moyenne de frontiere est petite.   
        Conseil: Conteur pour taille de frontiere   
    En cas dense, pourquoi pas V^2logV?   
        update n'est presque pas executé E fois, difficile de toujours améliorer chaque fois, pas mettre à toujours autant que ça  
        Conseil: Conteur pour update  
- Exo6: Get all combination by naive approach
- Exo7: Get all combination of size k by naive approach
    **Attention**  
    Usage of ```yield```
- Exo8: Get voisins of a graph
- Exo9: Get all of the combination possible with DFS
- Exo10: Get all of the combination of length k with DFS
    **Attention**  
    Why do we use DFS?
    How to stop once we find a combination of length k?  
    Are pop(0) and pop(-1) of same complexity?  
- Exo11: Get the min of the hospitals near here
    **Attention**   
    Usage of  ```min(hospitals, key=lambda i: distance_dict[(city,i)])``` can help to improve our code
- Exo12: Get the max of exo11, which is the kcentre_value
- Exo13: Write the brute force algo which tests all of the possible combinations
- Exo14: Complexity of brute force
- Exo15: Write greedy(glouton) algorithm which takes each time 1 best (combien with the old city) city to add in the combination
- Exo16: Write heuristic algorithm which takes each time l best (combien with the old city) city to add in the combination
- Exo17: Write random algorithm which takes 
    **Attention**   
    Usage of ```random.shuffle(candidates_copy)``` and ```random_combination = candidates_copy[0:k]``` to randomly generate a combination
- Exo18: Complexity of france lite map
- Exo19: Complexity of france map