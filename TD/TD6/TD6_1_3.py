from utils import *

def backtracking(O_dict, W) :    
    global bestSol, objs_list
 
    # initialization
    bestSol = {'selected': set() , 'index':0, 'weight': 0, 'score': 0}
    objs_list = sorted(O_dict.keys()) # lexicographical order on objects
 
    # computes the children of the current partial solution
    def children(curParSol):
        childrenSols = []
        ############### TODO : complete code ####################
        if curParSol['index'] < len(objs_list):
            # First presence
            childSol1 = curParSol.copy()
            toadd = objs_list[curParSol['index']]
            childSol1['weight'] += O_dict[toadd]['w']
            if childSol1['weight'] <= W:
                childSol1['selected'] = curParSol['selected'].union({toadd})
                childSol1['score'] += O_dict[toadd]['v']
                childSol1['index'] += 1
                childrenSols.append(childSol1)
            
            # Second abscence
            childSol2 = curParSol.copy()
            childSol2['index'] += 1
            childrenSols.append(childSol2)


        return childrenSols
 
    # a partial solution is terminal when it has no children
    def terminal(curParSol):
        return len(children(curParSol)) == 0
 
    def backtracking_rec(curParSol) :
        global objs_list, bestSol
 
        if terminal(curParSol) :
            if curParSol['score'] > bestSol['score'] :
                bestSol = curParSol.copy()
        else :
            for parSol in children(curParSol):
                backtracking_rec(parSol)
 
    # call backtracking on the root node
    rootSol = {'selected': set() , 'index': 0, 'weight': 0, 'score': 0}
    backtracking_rec(rootSol)
 
    # return the best found solution (the index entry is no more relevent)
    bestSol.pop('index')
    return bestSol

if __name__=="__main__":
    print('--- BACKTRACKING ---')
 
    bestSol4 = backtracking(O4, W4)
    print('--- simple case : 4 objects --- \n best found solution {} of value {}'.format(bestSol4['selected'], bestSol4['score']))
    assert bestSol4['score'] == 35
    assert bestSol4['selected'] == {'o2', 'o3'}
 
    bestSol15 = backtracking(O15, W15)
    print('--- bigger case : 15 objects --- \n best found solution {} of value {}'.format(bestSol15['selected'], bestSol15['score']))
    assert bestSol15['score'] == 1458
    assert bestSol15['selected'] == {'o1', 'o3', 'o5', 'o7', 'o8', 'o9', 'o14', 'o15'}
    print('Test finished')