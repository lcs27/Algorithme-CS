from utils import *
from TD1_1_1 import *
def has_odd_cycle(V,E):
    s=V[0]
    depth=depth_compute(V,E,s)
    for e in E:
        if depth[e[0]]==depth[e[1]]:
            return True
    return False