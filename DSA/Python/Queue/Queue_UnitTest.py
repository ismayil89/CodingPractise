from typing import Generator, Iterable
import unittest
import Queue


class Queue_UnitTest(unittest.TestCase):
    def setUp(self) -> None:
        self.queueObj = Queue.Queue()
        self.myListElements = [
            "Hello!!",
            "Welcome",
            "To",
            "Queue",
            "Implementation",
            "In",
            "Python",
            "This",
            "Can",
            "be",
            "implemented",
            "using",
            "Singly",
            "Linked",
            "List",
            "as",
            "well",
            "as",
            "Arrays",
        ]
        self.mylistLen = len(self.myListElements)
        for element in self.myListElements:
            self.queueObj.enqueue(element)

    def test_sizeOf(self):
        self.assertEqual(self.mylistLen, self.queueObj.sizeOf())

    def test_isEmpty(self):
        self.assertFalse(self.queueObj.isEmpty())
        self.assertTrue(self.queueObj.clear())
        self.assertTrue(self.queueObj.isEmpty())

    def test_dequeue(self):
        self.assertEqual("Hello!!", self.queueObj.dequeue())
        self.assertTrue(self.queueObj.clear())
        self.assertRaises(Exception, self.queueObj.dequeue)

    def test_enqueue(self):
        self.assertEqual(self.mylistLen + 1, self.queueObj.enqueue("3"))
        self.assertRaises(Exception, self.queueObj.enqueue, "3")

    def test_peek(self):
        self.assertEqual("Hello!!", self.queueObj.peek())
        self.assertTrue(self.queueObj.clear())
        self.assertRaises(Exception, self.queueObj.peek)

    def test_clear(self):
        self.assertTrue(self.queueObj.clear())
        self.assertTrue(self.queueObj.clear())

    def test_iterator(self):
        self.assertIsInstance(self.queueObj.iterator(), Iterable)
        self.assertIsInstance(self.queueObj.iterator(), Generator)


if __name__ == "__main__":
    unittest.main()
