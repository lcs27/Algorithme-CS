from heapq import *
 
tas = [(1,'a'), (2,'b')]            
heapify(tas)                        ### création d'un tas min à partir d'une liste quelconque en O(n)
heappush(tas, (0,'c'))               ### insertion en O(log n) 
print(heappop(tas))                 ### extraction de (0, 'c') en O(log n)
print(heappop(tas)[0])              ### extraction >>> '1'
print(len(tas))                     ### mesure en O(1) >>> 1 
print(heappop(tas)[1])              ### extraction >>> 'b'