class UnionFind:
    '''
    Constructor of Union Find Class
    Takes the size of UnionFind Set as Input
    '''
    def __init__(self, size):
        # Size of Union Find
        self.size = size 
        if self.size <= 0:
            raise Exception(f'Invalid Size. Minimum size should be 1')
        # Initially no. of components will be equal to the size of Union Find
        self.numOfComp = size 
        self.sizeOfComp = self.size * [None]
        self.compArray = self.size * [None]
        for i in range(self.size):
            # Initially size of each component will be 1
            self.sizeOfComp[i] = 1
            # Initially each node of a component will point to itself
            self.compArray[i] = i 

    def find(self, node):
        '''
        Find the root to which the node belongs to
        '''
        if self.isValid(node):
            root = node
            while(root != self.compArray[root]):
                root = self.compArray[root]

            while(node != root):
                nextNode = self.compArray[node]
                self.compArray[node] = root
                node = nextNode

            return(root)

    def isValid(self, node):
        if (node < 0) or (node > self.size):
            raise Exception(f'Invalid Node - {node}')
        return(True)

    def connected(self, node_1, node_2):
        '''
        Verifies if two nodes belong to same component
        '''
        if (self.isValid(node_1) and self.isValid(node_2)):
            return(self.find(node_1) == self.find(node_2))

    def componentSize(self, node):
        '''
        Returns the size of the Component/set, the node belongs to
        '''
        if self.isValid(node):
            return(self.sizeOfComp[self.find(node)])

    def sizeOf(self):
        return(self.size)

    def components(self):
        '''
        Returns the total number of components
        '''
        return(self.numOfComp)

    def unify(self, node_1, node_2):
        '''
        Unifies two nodes within a single component
        '''
        if (self.isValid(node_1) and self.isValid(node_2)):
            if(self.connected(node_1, node_2)):
                return None

            root_1 = self.find(node_1)
            root_2 = self.find(node_2)

            if self.sizeOfComp[root_1] >= self.sizeOfComp[root_2]:
                self.compArray[root_2] = root_1
                self.sizeOfComp[root_1] += self.sizeOfComp[root_2]
            else:
                self.compArray[root_1] = root_2
                self.sizeOfComp[root_2] += self.sizeOfComp[root_1]

            self.numOfComp -= 1