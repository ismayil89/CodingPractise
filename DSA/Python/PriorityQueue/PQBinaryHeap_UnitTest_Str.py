import unittest
import PQBinaryHeap
from random import seed
from random import randint
import random, string

class PQueue_UnitTest(unittest.TestCase):
    def setUp(self) -> None:
        self.pqueueObj = PQBinaryHeap.PQBinaryHeap(ascendig=False)
        #self.strHeap = []
        #for _ in range(10):
        #    self.strHeap.append(''.join(random.choice(string) for i in range(10)))

        self.strHeap = [
            "Hello!!",
            "Welcome",
            "To",
            "Doubly",
            "Linked List",
            "Implementation",
            "In",
            "Python",
            "3",
            ".8"
        ]

        self.strHeapLen = len(self.strHeap)
        for element in self.strHeap:
            self.pqueueObj.addNode(element)

    def test_sizeOf(self):
        self.assertEqual(self.strHeapLen, self.pqueueObj.sizeOf())

    def test_isEmpty(self):
        self.assertFalse(self.pqueueObj.isEmpty())
        self.assertEqual(0,self.pqueueObj.clear())
        self.assertTrue(self.pqueueObj.isEmpty())

    def test_contains(self):
        self.assertFalse(self.pqueueObj.contains('Ismayil'))
        self.assertTrue(self.pqueueObj.contains(self.strHeap[-1]))
        
    def test_addNode(self):
        # Testing of Node addition to existing Priority Queue
        self.assertRaises(Exception, self.pqueueObj.addNode, 'Mohamed')
        sortedData = []
        data = self.pqueueObj.poll()
        while data:
            sortedData.append(data)
            data = self.pqueueObj.poll()

        self.assertEqual(sortedData, sorted(self.strHeap, reverse=True))

        #self.assertTrue(self.pqueueObj.clear())
        self.strHeapLen = 0
        self.assertEqual(self.strHeapLen + 1, self.pqueueObj.addNode('GitHub'))
        self.assertRaises(Exception, self.pqueueObj.addNode, 4.3)

    def test_peek(self):
        self.assertEqual(max(self.strHeap), self.pqueueObj.peek())
        self.assertEqual(0,self.pqueueObj.clear())
        self.assertIsNone(self.pqueueObj.peek())

    def test_poll(self):
        self.assertEqual(max(self.strHeap), self.pqueueObj.poll())
        self.assertEqual(self.strHeapLen - 1, self.pqueueObj.sizeOf())
        self.assertEqual(0,self.pqueueObj.clear())
        self.assertIsNone(self.pqueueObj.poll())

    def test_clear(self):
        self.assertEqual(0,self.pqueueObj.clear())
        self.assertEqual(0,self.pqueueObj.clear())


if __name__ == "__main__":
    unittest.main()
