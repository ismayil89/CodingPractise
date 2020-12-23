import unittest
import PQBinaryHeap
from random import seed
from random import randint
import random

class PQueue_UnitTest(unittest.TestCase):
    def setUp(self) -> None:
        self.pqueueObj = PQBinaryHeap.PQBinaryHeap()
        self.floatHeap = []
        for _ in range(10):
            self.floatHeap.append(random.uniform(10.5, 10091.5))

        self.floatHeapLen = len(self.floatHeap)
        for element in self.floatHeap:
            self.pqueueObj.addNode(element)

    def test_sizeOf(self):
        self.assertEqual(self.floatHeapLen, self.pqueueObj.sizeOf())

    def test_isEmpty(self):
        self.assertFalse(self.pqueueObj.isEmpty())
        self.assertEqual(0,self.pqueueObj.clear())
        self.assertTrue(self.pqueueObj.isEmpty())

    def test_contains(self):
        self.assertFalse(self.pqueueObj.contains(10091.6))
        self.assertTrue(self.pqueueObj.contains(self.floatHeap[-1]))
        
    def test_addNode(self):
        # Testing of Node addition to existing Priority Queue
        self.assertRaises(Exception, self.pqueueObj.addNode,56.543)
        sortedData = []
        data = self.pqueueObj.poll()
        while data:
            sortedData.append(data)
            data = self.pqueueObj.poll()

        self.assertEqual(sortedData, sorted(self.floatHeap))
        self.floatHeapLen = 0
        self.assertEqual(self.floatHeapLen + 1, self.pqueueObj.addNode(3.0))
        self.assertRaises(Exception, self.pqueueObj.addNode, 3)

    def test_peek(self):
        self.assertEqual(min(self.floatHeap), self.pqueueObj.peek())
        self.assertEqual(0,self.pqueueObj.clear())
        self.assertIsNone(self.pqueueObj.peek())

    def test_poll(self):
        self.assertEqual(min(self.floatHeap), self.pqueueObj.poll())
        self.assertEqual(self.floatHeapLen - 1, self.pqueueObj.sizeOf())
        self.assertEqual(0,self.pqueueObj.clear())
        self.assertIsNone(self.pqueueObj.poll())

    def test_clear(self):
        self.assertEqual(0,self.pqueueObj.clear())
        self.assertEqual(0,self.pqueueObj.clear())

if __name__ == "__main__":
    unittest.main()
