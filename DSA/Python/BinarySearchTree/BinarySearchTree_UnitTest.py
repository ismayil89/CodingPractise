import unittest
import BinarySearchTree as BST
from random import seed
from random import randint

class BinarySearchTree_UnitTest(unittest.TestCase):
    def setUp(self):
        self.bstObj = BST.BinarySearchTree()
        seed(1)
        self.bsTree = []
        for _ in range(10):
	        self.bsTree.append(randint(0, 100))

        self.bsTreeLen = len(self.bsTree)
        for element in self.bsTree:
            self.bstObj.add(element)

    def test_preOrder(self):
        print(self.bsTree)
        print(self.bstObj.preOrder())
        print(self.bstObj.inOrder())
        print(self.bstObj.postOrder())
        print(self.bstObj.linearOrder())

if __name__ == "__main__":
    unittest.main() 
