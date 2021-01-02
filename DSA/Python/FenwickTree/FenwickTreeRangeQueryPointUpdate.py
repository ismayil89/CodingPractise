__author__ = "Mohamed Ismayil"
__credits__ = ["William Fiset"]
__version__ = "1.0"
__maintainer__ = "Mohamed Ismayil"
__email__ = "ismayil.ece@gmail.com"
__status__ = "Prototype"
__date__ = "01-Jan-2021"

class FenwickTreeRangeQueryPointUpdate:
    def __init__(self, values = []):
        self.values = values
        self.LenOfFen = len(self.values)
        self.OriginalFen = self.__createFenwickTree()
        print(f'FT - {self.OriginalFen}')
        if not self.OriginalFen:
            raise Exception("Invalid List")
        
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
            self.OriginalFen[index] += value
            index += self.__lsb(index)
        
    def get(self, index):
        return(self.__prefixSum(index) - self.__prefixSum(index-1))

    def set(self, index, value):
        self.add(index ,value - self.sum(index, index))

    def sum(self, start, stop):
        if stop < start:
            raise Exception("Invalid Range")
        return(self.__prefixSum(stop) - self.__prefixSum(start-1))

    def __prefixSum(self, index):
        sum = 0
        while index > 0:
            sum += self.OriginalFen[index]
            index &= ~self.__lsb(index) #index -= self.__lsb(index)
        return sum

    def __lsb(self, index):
        return(index & -index)

if __name__ == "__main__":
    
    myList = [0,1,2,2,4]
    print(f'Original - {myList}')
    fenwickObj2 = FenwickTreeRangeQueryPointUpdate(myList)
    print(fenwickObj2.sum(1, 4))
    fenwickObj2.add(3, 1)
    print(fenwickObj2.sum(1, 4))
    fenwickObj2.set(4, 0)
    print(fenwickObj2.sum(1, 4))
    print(fenwickObj2.get(2))