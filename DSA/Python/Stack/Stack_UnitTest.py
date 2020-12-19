import unittest
import Stack


class Stack_UnitTest(unittest.TestCase):
    def setUp(self) -> None:
        self.stackObj = Stack.Stack()
        self.stackObj.push("Garlic")
        self.stackObj.push("Cabbage")
        self.stackObj.push("Potato")
        self.stackObj.push("Apple")
        self.size = self.stackObj.sizeOf()

    def test_sizeOf(self):
        self.assertEqual(self.size, self.stackObj.sizeOf())

    def test_push(self):
        self.assertEqual(self.size + 1, self.stackObj.push("Onion"))

    def test_pop(self):
        self.assertEqual("Apple", self.stackObj.pop())
        self.assertTrue(self.stackObj.clear())
        self.assertRaises(Exception, self.stackObj.pop)

    def test_peek(self):
        self.assertEqual("Apple", self.stackObj.peek())
        self.assertTrue(self.stackObj.clear())
        self.assertRaises(Exception, self.stackObj.peek)

    def test_search(self):
        self.assertEqual(3, self.stackObj.search("Garlic"))
        self.assertFalse(self.stackObj.search("GarLic"))
        self.assertTrue(self.stackObj.clear())
        self.assertRaises(Exception, self.stackObj.search)

    def test_clear(self):
        self.assertTrue(self.stackObj.clear())
        self.assertTrue(self.stackObj.clear())


if __name__ == "__main__":
    unittest.main()
