# Question 6
l1=['leMonde',2,None]
l2=['leFigaro',1,l1]
l3=['laLibération',4,l2]
l4=['lesEchos',3,l3]
stock=['lEquipe',5,l4]

# On peut faire autrement par objet

# Question 7
def get(journal):
    #Compléxité en O(n)
    global stock
    current = stock
    while current != None:
        if current[0] == journal:
            return current[1]
        current=current[2]
    
    return None

def set(journal,quantity):
    #Compléxité en O(n)
    global stock
    current = stock
    while current != None:
        if current[0] == journal:
            current[1] = quantity
            return True
        current=current[2]
    return False

def add(journal,quantity):
    #Compléxité en O(1)
    global stock
    old=stock
    stock=[journal,quantity,old]

def delete(journal):
    #Compléxité en O(n)
    global stock
    current = stock
    while current != None:
        if current[0] == journal:
            current[2] = current[2][2]
            return True
        current=current[2]
    return False