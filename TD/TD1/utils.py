def pop_begin( lnext ):
    return lnext.pop(0)

def neighbours (n , E ):
    neigh=[]
    for (x,y) in E:
        if x == n:
            neigh.append(y)
        if y == n:
            neigh.append(x)
    return neigh

def add_end (v , lnext):
    lnext.append(v)

