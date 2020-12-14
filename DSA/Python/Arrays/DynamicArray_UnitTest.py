from typing import Generator, Iterable
import unittest
import DynamicArray as DynArr
class Test_DynamicArray(unittest.TestCase):
    def setUp(self):
        self.testObj = DynArr.DynamicArray()
        self.myListElements = ["Hello!!","Welcome","To","Array","Implementation","In","Python",666]
        self.mylistLen = len(self.myListElements)
        for element in self.myListElements:
            self.testObj.add(element)
        
    def test_size(self):
        self.assertEqual(self.mylistLen, self.testObj.size())
        
    def test_isEmpty(self):
        self.assertFalse(self.testObj.isEmpty())

    def test_get(self):
        self.assertNotEqual("Index out of bound", self.testObj.get(3))

    def test_set(self):
        self.assertTrue(5,"Added")

    def test_clear(self):
        self.testObj.clear()
        self.assertEqual(0,self.testObj.size())

    def test_add(self):
        self.assertIsNone(self.testObj.add("Testing"))
        self.assertEqual(self.mylistLen+1,self.testObj.size())

    def test_indexof(self):
        self.assertFalse(0,self.testObj.indexof("To"))

    def test_remove(self):
        self.assertTrue(self.testObj.remove("To"))
        self.assertFalse(self.testObj.remove("Testing"))
        
    def test_removeAt(self):
        self.assertEqual("Index out of bound", self.testObj.removeAt(-4))
        self.assertEqual("Index out of bound", self.testObj.removeAt(self.mylistLen+1))
        self.assertEqual("Welcome", self.testObj.removeAt(1))

    def test_contains(self):
        self.assertTrue(self.testObj.contains("To"))
        self.assertFalse(self.testObj.contains("Testing"))

    def test_arrayIter(self):
        self.assertIsInstance(self.testObj.arrayIter(), Iterable)
        self.assertIsInstance(self.testObj.arrayIter(), Generator)
        
    def test_reverse(self):
        self.assertEqual(self.myListElements[self.mylistLen-1::-1],self.testObj.reverse())
        self.testObj.clear()
        self.assertIsNone(self.testObj.reverse())

    def test_array(self):
        self.assertEqual(self.myListElements,self.testObj.array())
        self.testObj.clear()
        self.assertEqual([],self.testObj.array())
        
if __name__ == '__main__':
    unittest.main()