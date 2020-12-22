import unittest
import PQBinaryHeap
from random import seed
from random import randint
import random

class PQueue_UnitTest(unittest.TestCase):
    def setUp(self) -> None:
        self.pqueueObj = PQBinaryHeap.PQBinaryHeap(ascendig=False)
        seed(1)
        self.IntHeap = []
        for _ in range(10):
	        self.IntHeap.append(randint(0, 10000))

        self.IntHeapLen = len(self.IntHeap)
        for element in self.IntHeap:
            self.pqueueObj.addNode(element)

    def test_sizeOf(self):
        self.assertEqual(self.IntHeapLen, self.pqueueObj.sizeOf())

    def test_isEmpty(self):
        self.assertFalse(self.pqueueObj.isEmpty())
        self.assertEqual(0,self.pqueueObj.clear())
        self.assertTrue(self.pqueueObj.isEmpty())

    def test_contains(self):
        self.assertFalse(self.pqueueObj.contains(10001))
        self.assertTrue(self.pqueueObj.contains(self.IntHeap[-1]))
        
    def test_addNode(self):
        # Testing of Node addition to existing Priority Queue
        self.assertRaises(Exception, self.pqueueObj.addNode, 3)
        sortedData = []
        data = self.pqueueObj.poll()
        while data:
            sortedData.append(data)
            data = self.pqueueObj.poll()

        self.assertEqual(sortedData, sorted(self.IntHeap, reverse=True))

        #self.assertTrue(self.pqueueObj.clear())
        self.IntHeapLen = 0
        self.assertEqual(self.IntHeapLen + 1, self.pqueueObj.addNode(3))
        self.assertRaises(Exception, self.pqueueObj.addNode, "3")

    def test_peek(self):
        self.assertEqual(max(self.IntHeap), self.pqueueObj.peek())
        self.assertEqual(0,self.pqueueObj.clear())
        self.assertIsNone(self.pqueueObj.peek())

    def test_poll(self):
        self.assertEqual(max(self.IntHeap), self.pqueueObj.poll())
        self.assertEqual(self.IntHeapLen - 1, self.pqueueObj.sizeOf())
        self.assertEqual(0,self.pqueueObj.clear())
        self.assertIsNone(self.pqueueObj.poll())

    def test_clear(self):
        self.assertEqual(0,self.pqueueObj.clear())
        self.assertEqual(0,self.pqueueObj.clear())

if __name__ == "__main__":
    unittest.main()
