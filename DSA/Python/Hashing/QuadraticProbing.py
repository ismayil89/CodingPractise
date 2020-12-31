class TombStone:
    def __init__(self):
        self.key = None
        pass

class Entry:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.hash = hash(key)

class QuadraticProbing:
    def __init__(self):
        self.LoadFactor = 0.5
        self.PowerofTwo = 2
        self.Capacity = 4
        self.Threshold = self.LoadFactor * self.Capacity
        self.size = 0 # Hold the number of keys
        self.slotsUsed = 0 # Holds the number of keys + Tombstones
        self.Table = self.Capacity * [None]

    def __capacity(self):
        self.PowerofTwo += 1
        return(2**self.PowerofTwo)

    def sizeOf(self):
        return self.size

    def isEmpty(self):
        return(self.size == 0)

    def clear(self):
        self.PowerofTwo = 2
        self.Capacity = 4
        self.Threshold = self.LoadFactor * self.Capacity
        self.size = 0
        self.slotsUsed = 0
        self.Table = self.Capacity * [None]

    def hasKey(self, key):
        bucketIndex = self.__normalizeIndex(hash(key))
        return (self.__bucketSeekEntry(bucketIndex, key) != None)

    def __probing(self, x):
        return(int((x*(x + 1))/2))

    def __normalizeIndex(self, keyHash):
        return ((keyHash & 0x7FFFFFFF) % self.Capacity)
        
    def insert(self, key, value):
        if key == None or key == "":
            raise Exception("Invalid Key")

        EntryObj = Entry(key, value)
        bucketIndex = self.__normalizeIndex(EntryObj.hash)
        return(self.__bucketInsertEntry(bucketIndex, EntryObj))

    def getValue(self, key):
        if key == None or key == "":
            raise Exception("Invalid Key")
        bucketIndex = self.__normalizeIndex(hash(key))
        EntryObj = self.__bucketSeekEntry(bucketIndex, key)
        if EntryObj:
            return EntryObj.value
        return None

    def remove(self, key):
        if key == None or key == "":
            raise Exception("Invalid Key")
        bucketIndex = self.__normalizeIndex(hash(key))
        return(self.__bucketRemoveEntry(bucketIndex, key))
    
    def printHashTable(self):
        if self.size == 0:
            return None
        for i in range(len(self.Table)):
        #for Obj in self.Table:
            #if hasattr(self.Table[i], 'hash'):
            Obj = self.Table[i]
            if hasattr(Obj, 'hash'):
                print(f'Index -> {i} || Hash -> {Obj.hash} || Key -> {Obj.key} || Value -> {Obj.value}')
        
        print(f'Threshold -> {self.Threshold}')
        print(f'Capacity  -> {self.Capacity}')
        print(f'Size      -> {self.size}')

    def __bucketSeekEntry(self, bucketIndex, key):
        if key == None:
            raise Exception("Invalid Key")
        if self.Table[bucketIndex]:
            if self.Table[bucketIndex].key == key:
                return self.Table[bucketIndex]
                
            elif self.Table[bucketIndex]:
                newHash = hash(self.Table[bucketIndex].key)
                bucketIndex = self.__normalizeIndex(newHash)
                x = 0
                while self.Table[bucketIndex]:
                    if self.Table[bucketIndex].key == key:
                        return self.Table[bucketIndex]

                    # Finding the next Free hop
                    x = x + 1
                    self.Table[bucketIndex].hash += self.__probing(x)
                    bucketIndex = self.__normalizeIndex(self.Table[bucketIndex].hash)
                    
        return None

    def __bucketInsertEntry(self, bucketIndex, EntryObj):
        oldValue = None
        x = 0 
        while True:
            if self.Table[bucketIndex] == None:
                self.Table[bucketIndex] = EntryObj
                self.size += 1
                break
            elif self.Table[bucketIndex].key == EntryObj.key:
                oldValue = self.Table[bucketIndex].value
                self.Table[bucketIndex].value = EntryObj.value
                break
            elif type(self.Table[bucketIndex]).__name__ == 'Tombstone':
                self.Table[bucketIndex] = EntryObj
                #Flag = False
                self.size += 1
                break
            else:
                # Finding the next hop
                x = x + 1
                EntryObj.hash += self.__probing(x)
                bucketIndex = self.__normalizeIndex(EntryObj.hash)
                
        if self.size >= self.Threshold:
            self.__resizeTable()

        if oldValue:
            return oldValue
        else:
            return None
            
    def __bucketRemoveEntry(self, bucketIndex, key):
        obj = self.__bucketSeekEntry(bucketIndex, key)
        if obj != None:
            value = obj.value
            self.Table[bucketIndex] = TombStone()
            self.size  -= 1
            return value
        return None
    
    def __resizeTable(self):
        self.Capacity = self.__capacity()
        self.Threshold = self.LoadFactor * self.Capacity
        newTable = self.Capacity * [None]
        
        for eachObj in self.Table:
            if hasattr(eachObj, 'hash'):
                eachObj.hash = hash(eachObj.key)
                bucketIndex = self.__normalizeIndex(eachObj.hash)
                x = 0
                while True:
                    if newTable[bucketIndex] == None:
                        newTable[bucketIndex] = eachObj
                        break
                
                    # Finding the next Free hop
                    x = x + 1
                    eachObj.hash += self.__probing(x)
                    bucketIndex = self.__normalizeIndex(eachObj.hash)

        self.Table = newTable
        self.slotsUsed = self.size