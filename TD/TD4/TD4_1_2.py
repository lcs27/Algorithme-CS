from utils import *

# Question 5
stock=[['lesEchos',3],['lEquipe',5],['leFigaro',1],['laLibération',4],['leMonde',2]]

def get(journal):
    #Compléxité en O(log(n))
    global stock
    candidate=stock
    while True:
        i=int(len(candidate)/2)
        if i<1:
            return None
        if journal == candidate[i-1] :
            return candidate[i-1][1]
        elif compare(journal,candidate[i-1]) > 0:
            candidate=candidate[0:i-1]
        else:
            candidate=candidate[i:]
    
def set(journal,quantity):
    #Compléxité en O(log(n))
    global stock
    candidate=stock
    while True:
        i=int(len(candidate)/2)
        if i<1:
            return False
        if journal == candidate[i-1] :
            candidate[i-1][1]=quantity
        elif compare(journal,candidate[i-1]) > 0:
            candidate=candidate[0:i-1]
        else:
            candidate=candidate[i:]

def add():
    #Compléxité en O(n)
    raise NotImplementedError

def delete():
    #Compléxité en O(n)
    raise NotImplementedError

