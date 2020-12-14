# Question 1
stock=[('leMonde',2),('leFigaro',1),('laLibération',4),('lesEchos',3),('lEquipe',5)]

# Question 2
def get(journal):
    #Compléxité en O(n)
    global stock
    for s in stock:
        if journal==s[0]:
            return s[1]
        return None


def set(journal,quantite):
    #Compléxité en O(n)
    global stock
    for s in stock:
        if journal==s[0]:
            s[1]=quantite
            return True
    return False

# Question 3
def add(journal,quantity):
    #Compléxité en O(1)
    global stock
    stock.append((journal,quantity))

# Question 4
def del(journal):
    #Compléxité en O(n)
    global stock
    
    for i=1:len(stock):
        #Compléxité en O(n)
        if stock[i][0]==journal:
            break
    for j=i:len(stock):
        #Compléxité en O(n)
        stock[j]=stock[j+1]

    