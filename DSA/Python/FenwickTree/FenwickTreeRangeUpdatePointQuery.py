class FenwickTreeRangeUpdatePointQuery:
    def __init__(self, values = []):
        self.values = values
        self.LenOfFen = len(self.values)
        self.OriginalFen = self.__createFenwickTree()
        print(self.OriginalFen)
        if not self.OriginalFen:
            raise Exception("Invalid List")
        self.CurrentFen = self.OriginalFen[:]
    
    def __createFenwickTree(self):
        if self.values == [] or self.values == None:
            return False
        self.FenwickTree = self.values[:]

        for i in range(1,self.LenOfFen):
            parent = i + self.__lsb(i)
            if parent < self.LenOfFen:
                self.FenwickTree[parent] += self.FenwickTree[i]
        
        return self.FenwickTree

    def add(self, index, value):
        while index < self.LenOfFen:
            self.CurrentFen[index] += value
            index += self.__lsb(index)
            
    def updateRange(self, start, stop, value):
        # If Len of FT is 15, and the range update is from 10 to 12, then
        # update the value from 10 to 15 and then add negative of value from
        # 13 to 15
        self.add(start, value)
        self.add(stop + 1, -value)
        
    def get(self, index):
        return(self.__prefixSum(index, self.CurrentFen) - self.__prefixSum(index-1 , self.OriginalFen))

    def set(self, index, value):
        while(index < self.LenOfFen):
            self.CurrentFen[index] += value
            index &= self.__lsb(index)

    def sum(self, start, stop):
        if stop < start:
            raise Exception("Invalid Range")
        return(self.__prefixSum(stop, self.OriginalFen) - self.__prefixSum(start, self.OriginalFen))

    def __prefixSum(self, index, ft):
        sum = 0
        while index > 0:
            sum += ft[index]
            index &= ~self.__lsb(index) #index -= self.__lsb(index)
        return sum

    def __lsb(self, index):
        return(index & -index)

if __name__ == "__main__":
    myList = [0,1,-2,3,-4,5,-6]
    #myList = [0,1,2,2,4]
    fenwickObj = FenwickTreeRangeUpdatePointQuery(myList)
    fenwickObj.updateRange(1, 4, 10)
    print(fenwickObj.get(1))
    print(fenwickObj.get(4))
    print(fenwickObj.get(5))
    fenwickObj.updateRange(3, 6, -20)
    print(fenwickObj.get(3))
    print(fenwickObj.get(4))
    print(fenwickObj.get(5))