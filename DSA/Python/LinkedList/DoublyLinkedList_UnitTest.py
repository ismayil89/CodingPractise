import unittest
from typing import Generator, Iterable
import DoublyLinkedList as DLL

class Test_DoublyLinkedList(unittest.TestCase):
    def setUp(self):
        self.testObj = DLL.DoublyLinkedList()
        self.myListElements = ["Hello!!", "Welcome", "To", "Doubly Linked List", "Implementation", "In", "Python", 666]
        self.mylistLen = len(self.myListElements)
        for element in self.myListElements:
            self.testObj.addLast(element)
        
    def test_clear(self):
        self.testObj.clear()
        self.assertEqual(0,self.testObj.getSize())
        self.testObj.clear()
        
    def test_getSize(self):
        self.assertEqual(self.mylistLen, self.testObj.getSize())
        
    def test_isEmpty(self):
        self.assertFalse(self.testObj.isEmpty())

    def test_addLast(self):
        self.assertIsNone(self.testObj.addLast("Testing"))
        self.assertEqual(self.mylistLen+1,self.testObj.getSize())
        self.testObj.clear()
        self.assertIsNone(self.testObj.addLast("Testing"))
        self.assertEqual(1,self.testObj.getSize())
    
    def test_addFirst(self):
        self.assertIsNone(self.testObj.addFirst("Testing"))
        self.assertEqual(self.mylistLen+1,self.testObj.getSize())
        self.testObj.clear()
        self.assertIsNone(self.testObj.addFirst("Testing"))
        self.assertEqual(1,self.testObj.getSize())

    def test_addAt(self):
        self.assertRaises(Exception, self.testObj.addAt, -1, "Test")
        self.assertRaises(Exception, self.testObj.addAt, self.mylistLen, "Test")
        self.assertTrue(self.testObj.addAt(0,"Unit"))
        self.assertTrue(self.testObj.addAt(2, "Test"))
        self.assertEqual(self.mylistLen+2,self.testObj.getSize())

    def test_peekFirst(self):
        self.assertNotEqual("Hello!", self.testObj.peekFirst())
        self.assertEqual("Hello!!", self.testObj.peekFirst())
        self.testObj.clear()
        self.assertRaises(Exception, self.testObj.peekFirst)

    def test_peekLast(self):
        self.assertNotEqual("bound", self.testObj.peekLast())
        self.assertEqual(666, self.testObj.peekLast())
        self.testObj.clear()
        self.assertRaises(Exception, self.testObj.peekLast)

    def test_removeFirst(self):
        self.assertEqual("Hello!!", self.testObj.removeFirst())
        self.testObj.clear()
        self.assertRaises(Exception, self.testObj.removeFirst)
        self.testObj.addFirst("Testing")
        self.assertTrue("Testing", self.testObj.removeFirst())
    
    def test_removeLast(self):
        self.assertTrue(666, self.testObj.removeLast())
        self.testObj.clear()
        self.assertRaises(Exception, self.testObj.removeLast)
        self.testObj.addLast("Testing")
        self.assertTrue("Testing", self.testObj.removeLast())

    def test_removeAt(self):
        self.assertEqual("To", self.testObj.removeAt(2))
        self.assertEqual("In", self.testObj.removeAt(4))
        self.assertRaises(Exception, self.testObj.removeAt, -1)
        self.assertRaises(Exception, self.testObj.removeAt, self.mylistLen)
        self.assertTrue("Hello!!", self.testObj.removeAt(0))
        self.assertTrue(666, self.testObj.removeAt(self.mylistLen - 4))
        self.assertEqual("Doubly Linked List", self.testObj.removeAt(1))
        
    def test_valueAt(self):
        self.assertRaises(Exception, self.testObj.valueAt, -1)
        self.assertRaises(Exception, self.testObj.valueAt, self.mylistLen)
        self.assertEqual("Hello!!", self.testObj.valueAt(0))
        self.assertEqual(666, self.testObj.valueAt(self.mylistLen - 1))
        self.assertEqual("To", self.testObj.valueAt(2))
        self.assertEqual("Implementation", self.testObj.valueAt(4))
        
    def test_indexOf(self):
        self.assertFalse(self.testObj.indexOf("To00"))
        self.assertEqual(2,self.testObj.indexOf("To"))

    def test_contains(self):
        self.assertEqual(2, self.testObj.contains("To"))
        self.assertFalse(self.testObj.contains("Testing"))

    def test_iterator(self):
        self.assertIsInstance(self.testObj.iterator(), Iterable)
        self.assertIsInstance(self.testObj.iterator(), Generator)
        
if __name__ == '__main__':
    unittest.main()