import math

pile=[]

def pile_add(element):
    #Compléxité en O(1)
    global pile
    pile.append(element)

def pile_get(element):
    #Compléxité en O(1)
    global pile
    pile.pop(element)

tas_min=[]

def tas_add(element):
    #Compléxité en O(log(n))
    global tas_min
    tas_min.append(element)
    i = len(tas_min)-1
    while i > 0:
        k = math.floor((i-1)/2)
        if tas_min[i] <= tas_min[k]:
            a = tas_min[k]
            tas_min[k] = tas_min[i]
            tas_min[i] = a
            i = k
        else:
            break

def tas_getmin():
    #Compléxité en O(1)
    global tas_min
    return tas_min[0]

def tas_popmin():
    #Compléxité en O(log(n))
    global tas_min
    minimum = tas_min[0]
    tas_min[0] = tas_min[-1]
    i = 0

    while i < math.floor((len(tas_min)-1)/2):

        #Get the min of the sons
        if tas_min[2*i+1] <= tas_min[2*i+2]:
            candidate = tas_min[2*i+1]
            index = 2*i+1
        else:
            candidate = tas_min[2*i+2]
            index = 2*i+2
        
        # Change with the min son
        if tas_min[i] >= candidate:
            tas_min[index] = tas_min[i]
            tas_min[i] = candidate
            i = index
        else:
            break

    tas_min.pop(-1)
    return minimum

if __name__ == "__main__":
    
    tas_min=[5,9,11,14,18,19,21,33,17,27]
    tas_add(7)
    print(tas_min)
    tas_min=[5,9,11,14,18,19,21,33,17,27]
    tas_popmin()
    print(tas_min)
    
    tas_min=[]
    tas_add(4)
    tas_add(7)
    tas_add(27)
    print(tas_min)
    tas_popmin()
    print(tas_min)
    tas_add(6)
    print(tas_min)
    