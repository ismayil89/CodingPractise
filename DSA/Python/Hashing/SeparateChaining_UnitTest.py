import unittest
import SeparateChaining
from random import seed
from random import randint
import random

class SeparateChaining_UnitTest(unittest.TestCase):
    def setUp(self) -> None:
        self.scObj = SeparateChaining.SeparateChaining()
        seed(1)
        self.IntHeap = []
        self.floatHeap = []
        
        for _ in range(10):
            self.floatHeap.append(random.uniform(10.5, 10091.5))
        for _ in range(10):
	        self.IntHeap.append(randint(0, 10000))
            
        self.testDict = {}
        for key, value in zip(self.IntHeap, self.floatHeap):
            self.testDict[key] = value
            self.scObj.insert(key, value)

        self.Hashsize = self.scObj.sizeOf()
        self.Dictsize = len(self.testDict.keys())

    def test_sizeOf(self):
        self.assertEqual(self.Dictsize, self.scObj.sizeOf())
    
    def test_isEmpty(self):
        self.assertFalse(self.scObj.isEmpty())
    
    def test_clear(self):
        self.scObj.clear()
        self.assertTrue(self.scObj.isEmpty())

    def test_hasKey(self):
        self.assertFalse(self.scObj.hasKey("Hello"))
        self.assertTrue(self.scObj.hasKey(self.IntHeap[5]))

    def test_insert(self):
        self.assertRaises(Exception, self.scObj.insert, "", "")
        self.assertIsNone(self.scObj.insert("Hello", "World"))
        self.assertEqual(self.testDict[self.IntHeap[0]], self.scObj.insert(self.IntHeap[0], "Replaced"))
        self.assertEqual("World", self.scObj.insert("Hello", "Replaced"))
        self.scObj.printHashTable()

    def test_getValue(self):
        self.assertRaises(Exception, self.scObj.getValue, None)
        self.assertEqual(self.testDict[self.IntHeap[1]], self.scObj.getValue(self.IntHeap[1]))
        self.assertIsNone(self.scObj.getValue("Ism"))

    def test_remove(self):
        self.assertRaises(Exception, self.scObj.remove, None)
        self.assertEqual(self.testDict[self.IntHeap[1]], self.scObj.remove(self.IntHeap[1]))

if __name__ == "__main__":
    unittest.main()       