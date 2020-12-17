import math
class Tas:
    def __init__(self,compare):
        self.tas=[]
        self.compare = compare

    def add(self,element):
    #O(log(n))
        self.tas.append(element)
        i = len(self.tas)-1
        while i > 0:
            k = math.floor((i-1)/2)
            if self.compare(self.tas[i],self.tas[k]):
                a = self.tas[k]
                self.tas[k] = self.tas[i]
                self.tas[i] = a
                i = k
            else:
                break

    def getmin(self):
        #O(1)
        return self.tas[0]

    def popmin(self):
        #O(log(n))
        minimum = self.tas[0]
        self.tas[0] = self.tas[-1]
        i = 0

        while i < math.floor((len(self.tas)-1)/2):

            #Get the min of the sons
            if self.compare(self.tas[2*i+1],self.tas[2*i+2]):
                candidate = self.tas[2*i+1]
                index = 2*i+1
            else:
                candidate = self.tas[2*i+2]
                index = 2*i+2
        
            # Change with the min son
            if not self.compare(self.tas[i],candidate):
                self.tas[index] = self.tas[i]
                self.tas[i] = candidate
                i = index
            else:
                break

        self.tas.pop(-1)
        return minimum
    
    def len(self):
        return len(self.tas)