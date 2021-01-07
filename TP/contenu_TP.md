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
- Exo8&9&10: Get combinations with think of graph intensive and voisin, voir code pour comprendre
