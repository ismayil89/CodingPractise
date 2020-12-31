#import DoublyLinkedList as DLL

class Entry:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.hash = hash(key)
    
class SeparateChaining:
    def __init__(self):
        self.LoadFactor = 0.75
        self.Capacity = 3
        self.Threshold = self.LoadFactor * self.Capacity
        self.size = 0
        # Creating a List of Lists
        self.Table = self.Capacity * [None]

    def sizeOf(self):
        return self.size

    def isEmpty(self):
        return(self.size == 0)

    def __normalizeIndex(self, keyHash):
        return((keyHash & 0x7FFFFFFF) % self.Capacity)

    def clear(self):
        self.Capacity = 3
        self.Threshold = self.LoadFactor * self.Capacity
        self.size = 0
        # Creating a List of Lists
        self.Table = self.Capacity * [None]

    def hasKey(self, key):
        bucketIndex = self.__normalizeIndex(hash(key))
        return (self.__bucketSeekEntry(bucketIndex, key) != None)
    
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
        print("\n")
        for subList in self.Table:
            if subList:
                for Obj in subList:
                    print(f'Hash -> {Obj.hash} || Key -> {Obj.key} || Value -> {Obj.value}')
        
        print(f'Threshold -> {self.Threshold}')
        print(f'Capacity  -> {self.Capacity}')
        print(f'Size      -> {self.size}')

    def __bucketSeekEntry(self, bucketIndex, key):
        if key == None:
            raise Exception("Invalid Key")
        if self.Table[bucketIndex]:
            for obj in self.Table[bucketIndex]:
                if key == obj.key:
                    return obj
        return None

    def __bucketInsertEntry(self, bucketIndex, EntryObj):
        if self.Table[bucketIndex] == None:
            self.Table[bucketIndex] = []
        
        obj = self.__bucketSeekEntry(bucketIndex, EntryObj.key)
        if obj == None:
            self.Table[bucketIndex].append(EntryObj)
            self.size  += 1
            if self.size >= self.Threshold:
                self.__resizeTable()
            return None
        else:
            oldValue = obj.value
            obj.value = EntryObj.value
            return oldValue
        
    def __bucketRemoveEntry(self, bucketIndex, key):
        obj = self.__bucketSeekEntry(bucketIndex, key)
        if obj != None:
            value = obj.value
            self.Table[bucketIndex].remove(obj)
            self.size  -= 1
            return value
        return None
    
    def __resizeTable(self):
        self.Capacity *= 2
        self.Threshold = self.LoadFactor * self.Capacity
        newTable = self.Capacity * [None]

        for eachSubList in self.Table:
            if eachSubList != None:
                for eachObj in eachSubList:
                    bucketIndex = self.__normalizeIndex(eachObj.hash)
                    if newTable[bucketIndex] == None:
                        newTable[bucketIndex] = [eachObj]
                    else:
                        newTable[bucketIndex].append(eachObj)
        
        self.Table = newTable