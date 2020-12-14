__author__ = 'Mohamed Ismayil'
__credits__ = ['William Fiset']
__version__ = '1.0'
__maintainer__ = 'Mohamed Ismayil'
__email__ = 'ismayil.ece@gmail.com'
__status__ = 'Prototype'

class DynamicArray:
    '''
    Dynamic Array Implementation using Python
    '''
    def __init__(self) -> None:
        '''
        Initialises the Standard Size of Array as 16
        '''
        self.len = 0
        self.capacity = 0
        self.Array = 16 * [None]

    def size(self):
        '''
        Returns the Size of Array
        '''
        return(self.len)

    def isEmpty(self):
        '''
        Returns True/False based on Array Content
        '''
        return(self.len == 0)

    def get(self,index):
        '''
        Returns the value at specific index of an Array
        '''
        if(index < 0 or index > self.len):
            return("Index out of bound")
        return(self.Array[index])
    
    def set(self, index, data):
        '''
        Sets the value at a specific index of Array.
        '''
        if(index < 0 or index > self.len):
            return("Index out of bound")
        self.Array[index] = data
        
    def clear(self):
        '''
        Empties the Array
        '''
        for index in range(self.len):
            self.Array[index] = None
        self.len = 0

    def add(self,data):
        '''
        Adds or Appends the value to the Array
        '''
        if (self.len + 1 >= self.capacity):
            if (self.capacity == 0):
                self.capacity = 1
            else:
                self.capacity = 2 * self.capacity
            self.TmpArray = self.capacity * [None]
            for index in range(self.len):
                self.TmpArray[index] = self.Array[index]
            self.Array = self.TmpArray
        
        self.Array[self.len] = data
        #print("Added '" + str(data) + "' to Array")
        self.len += 1
        
    def indexof(self, data):
        '''
        Returns the index of value in the Array.
        This is the index of first found value in Array
        '''
        for idx in range(self.len):
            if data == None:
                if self.Array[idx] == None:
                    return(idx)
            else:
                if self.Array[idx] == data:
                    return(idx)
        return(-1)

    def removeAt(self, rm_index):
        '''
        Removes the value at a specific index of Array
        '''
        if rm_index < 0 or rm_index > self.len:
            return("Index out of bound")
        data = self.Array[rm_index]
        self.TmpArray = (self.len -1) * [None]
        tmp_ptr = 0
        #print(self.len)
        #print(rm_index)
        #print(len(self.TmpArray))
        for i in range(self.len):
            #print("idx - " + str(i))
            if i != rm_index:
                #print("Temp - " + str(tmp_ptr))
                self.TmpArray[tmp_ptr] = self.Array[i]
                tmp_ptr += 1

        self.Array = self.TmpArray    
        self.capacity = self.len - 1
        self.len = self.len - 1
        return(data)

    def remove(self, data):
        '''
        Removes the first found value from the Array
        '''
        idx = self.indexof(data)
        #print("Index is " + str(idx))
        if idx >= 0:
            self.removeAt(idx)
            return(True)
        else:
            return(False)

    def contains(self,data):
        '''
        Returns True/False based on the value availability in Array
        '''
        return(self.indexof(data) != -1)
    
    def arrayIter(self):
        '''
        Returns the Iterator of the Array
        '''
        if self.len < 1:
            return(False)
        iterLen = 0
        while(iterLen < self.len):
            yield self.Array[iterLen]
            iterLen += 1
    
    def reverse(self):
        if self.len < 1:
            return None
        return(self.Array[self.len-1::-1])

    def array(self):
        if self.len < 1:
            return([])
        return(self.Array[:self.len])
    
#if __name__ == '__main__':
#
#    myobj = DynamicArray()
#    print("Original Array -> " + str(myobj.array()))
#    print("Is Array Empty? -> " + str(myobj.isEmpty()))
#    print("Find Value at Index 2 -> " + str(myobj.get(2)))
#    print("Size of Array -> " + str(myobj.size()))
#    myobj.add("Hello!!")
#    myobj.add("Welcome")
#    myobj.add("To")
#    myobj.add("Array")
#    myobj.add("Implementation")
#    myobj.add("Using")
#    myobj.add("Python")
#    print("Is Array Empty? -> " + str(myobj.isEmpty()))
#    print("Size of Array -> " + str(myobj.size()))
#    print("Usage of Iterator")
#    for val in myobj.arrayIter():
#        print(val)
#    print("Reverse Array -> " + str(myobj.reverse()))
#    print("Original Array -> " + str(myobj.array()))
#    print("Is the value 'Welcome' available in Array -> " + str(myobj.contains('Welcome')))
#    print("Size of Array -> " + str(myobj.size()))
#    print("Removing the value 'Welcome' from the Array -> " + str(myobj.remove('Welcome')))
#    print("Size of Array -> " + str(myobj.size()))
#    print("Original Array -> " + str(myobj.array()))
#    print("Removing the value at Index '0' from the Array -> " + str(myobj.removeAt(0)))
#    print("Size of Array -> " + str(myobj.size()))
#    print("Original Array -> " + str(myobj.array()))
#    myobj.add("Completed")
#    print("Changing the value at Index '0' in the Array to 'Done!' -> " + str(myobj.set(0, "Done!")))
#    print("Size of Array -> " + str(myobj.size()))
#    print("Original Array -> " + str(myobj.array()))
#    myobj.clear()
#    print("Array after clearing -> " + str(myobj.array()))
#    print("Size of Array -> " + str(myobj.size()))