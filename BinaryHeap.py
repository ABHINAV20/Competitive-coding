class HEAP:
    def __init__(self):
        self.heapList=[0]
        self.currentsize=0
        
    def insert(self,value):
        self.heapList.append(value)
        self.currentsize =self.currentsize + 1
        self.shiftUp(self.currentsize)
        
    def shiftUp(self,i):
        while(i // 2 > 0):
            if (self.heapList[i // 2] > self.heapList[i]):
                temp = self.heapList[i]
                self.heapList[i] = self.heapList[i // 2]
                self.heapList[i // 2] = temp
            i = i // 2
            
    def delMin(self):
        topNode = self.heapList[1]
        self.heapList[1] = self.heapList[self.currentsize]
        self.currentsize = self.currentsize - 1
        self.heapList.pop()
        self.shiftDown(1)
        return topNode
                
    def shiftDown(self,i):
        while (i*2) <= self.currentsize :
            mn=self.getmin(i)
            if (self.heapList[mn] < self.heapList[i]):
                temp = self.heapList[mn]
                self.heapList[mn] = self.heapList[i]
                self.heapList[i] = temp
            i = mn           
            
    def getmin(self,i):
        if (i*2+1 > self.currentsize):
            return i*2
        else:
            if (self.heapList[i*2] > self.heapList[i*2+1]):
                return i*2
            else:
                return i*2+1

    
        
        
             
            
        
            
        