from utils import *
def depth_compute (V ,E ,s):
    lnext = [ s ] # la file
    depth={ s: 0}
    while len( lnext ) >0:
        n = pop_begin( lnext )
        for v in neighbours (n , E ):
            if not v in depth :
                depth[v]=depth[n]+1
                add_end (v , lnext)
    return depth