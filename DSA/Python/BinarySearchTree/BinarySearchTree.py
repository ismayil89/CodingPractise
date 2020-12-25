class Node:
    def __init__(self, elem, left = None, right = None):
        self.data = elem
        self.left = left
        self.right = right

class BST:
    def __init__(self):
        self.root = None
        self.nodeCount = 0

    def isEmpty(self):
        return(self.nodeCount == 0)

    def sizeOf(self):
        return(self.nodeCount)

    def contains(self, elem):
        return self.__contains(self.root, elem)

    def __contains(self, node, elem):
        if node == None:
            return False

        if elem < node.data:
            return self.__contains(self.left, elem)
        elif elem > node.data:
            return self.__contains(self.right, elem)
        else:
            return True
    
    def height(self):
        return self.__height(self.root)
    
    def __height(self, node):
        if node == None:
            return 0
        return max(self.__height(self.left), self.__height(self.right)) + 1

    def add(self, elem):
        if self.contains(elem):
            return False
        else:
            self.root = self.__add(self.root, elem)
            self.nodeCount += 1
            return True

    def __add(self, node, elem):
        if node == None:
            node = Node(elem)
        else:
            if elem < node.data:
                node.left = self.__add(node.left, elem)
            else:
                node.right = self.__add(node.right, elem)
        
        return node

    def remove(self, elem):
        if self.contains(elem):
            self.root = self.__remove(self.root , elem)
            return(True)
        else:
            return(False)

    def __remove(self, node, elem):
        if node == None:
            return None
        
        if elem < node.data:
            node.left = self.__remove(node.left, elem)
        elif elem > node.data:
            node.right = self.__remove(node.right, elem)
        else:
            if node.left == None:
                rightChild = node.right
                node.data = None
                node = None
                return rightChild
            elif node.right == None:
                leftChild = node.left
                node.data = None
                node = None
                return leftChild
            else:
                tmp = self.__digLeft(node.right)
                node.data = tmp.data
                node.right = self.__remove(node.right, tmp.data)
                 
        return node

    def __digLeft(self, curNode):
        while(curNode.left != None):
            curNode = curNode.left
        return curNode
