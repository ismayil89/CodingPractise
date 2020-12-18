import unittest
import SinglyLinkedList as SLL
class Test_DynamicArray(unittest.TestCase):
    def setUp(self):
        self.testObj = SLL.MyLinkedList()
        self.myListElements = [5,15,25]
        self.mylistLen = len(self.myListElements)
        for element in self.myListElements:
            self.testObj.addAtHead(element)
    
    def test_get(self):
        self.assertEqual(25, self.testObj.get(0))

if __name__ == '__main__':
    unittest.main()