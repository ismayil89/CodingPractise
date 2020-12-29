import Queue #.Queue as Queue
class Node:
    def __init__(self, elem, left = None, right = None):
        self.data = elem
        self.left = left
        self.right = right

class BinarySearchTree:
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
            return self.__contains(node.left, elem)
        elif elem > node.data:
            return self.__contains(node.right, elem)
        else:
            return True
    
    def height(self):
        return self.__height(self.root)
    
    def __height(self, node):
        if node == None:
            return 0
        return max(self.__height(node.left), self.__height(node.right)) + 1

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

    def preOrder(self):
        node = self.root
        preOrderList = []
        return(self.__preOrder(node, preOrderList))
        
    def __preOrder(self, node, myLst):
        if node == None:
            return None
        myLst.append(node.data)
        self.__preOrder(node.left, myLst)
        self.__preOrder(node.right, myLst)
        return(myLst)
    
    def inOrder(self):
        node = self.root
        inOrderList = []
        return(self.__inOrder(node, inOrderList))

    def __inOrder(self, node, myLst):
        if node == None:
            return None
        self.__inOrder(node.left, myLst)
        myLst.append(node.data)
        self.__inOrder(node.right, myLst)
        return(myLst)

    def postOrder(self):
        node = self.root
        postOrderList = []
        return(self.__postOrder(node, postOrderList))

    def __postOrder(self, node, myLst):
        if node == None:
            return None
        self.__postOrder(node.left, myLst)
        self.__postOrder(node.right, myLst)
        myLst.append(node.data)
        return(myLst)

    def linearOrder(self):
        node = self.root
        linearOrderList = [node.data]
        queueObj = Queue.Queue()
        return(self.__linearOrder(node, linearOrderList, queueObj))

    def __linearOrder(self, node, myLst, queueObj):
        if node.left:
            queueObj.enqueue(node.left)
        if node.right:
            queueObj.enqueue(node.right)
        node = queueObj.dequeue()
        try:
            if node.data:
                myLst.append(node.data)
                self.__linearOrder(node, myLst, queueObj)
        except Exception:
            pass
        
        return(myLst)