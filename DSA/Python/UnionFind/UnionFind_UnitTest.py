import unittest
import UnionFind as UF

class UnionFind_UnitTest(unittest.TestCase):
    def setUp(self) -> None:
        self.setSize = 12
        self.unionfindObj = UF.UnionFind(self.setSize)
    
    def test_find(self):
        self.assertEqual(4, self.unionfindObj.find(4))
        self.assertNotEqual(32, self.unionfindObj.find(4))

    def test_connected(self):
        self.assertFalse(self.unionfindObj.connected(3,4))
        self.unionfindObj.unify(3,4)
        self.assertTrue(self.unionfindObj.connected(3,4))
        self.assertRaises(Exception, self.unionfindObj.connected, 3, 54)

    def test_componentSize(self):
        self.assertEqual(1, self.unionfindObj.componentSize(3))
        self.unionfindObj.unify(3,4)
        self.assertEqual(2, self.unionfindObj.componentSize(4))
        self.assertRaises(Exception, self.unionfindObj.componentSize, 54)

    def test_sizeOf(self):
        self.assertEqual(self.setSize, self.unionfindObj.sizeOf())
        self.assertNotEqual(self.setSize + 1, self.unionfindObj.sizeOf())

    def test_components(self):
        self.assertEqual(self.setSize, self.unionfindObj.components())
        self.unionfindObj.unify(3,4)
        self.assertEqual(self.setSize-1, self.unionfindObj.components())
        self.assertNotEqual(self.setSize, self.unionfindObj.components())

    def test_unify(self):
        self.unionfindObj.unify(3,4)
        self.assertEqual(self.setSize-1, self.unionfindObj.components())
        self.assertIsNone(self.unionfindObj.unify(3,4))
        self.assertRaises(Exception, self.unionfindObj.unify, 3,41)
        self.unionfindObj.unify(5,5)
        self.assertEqual(self.setSize-1, self.unionfindObj.components())

if __name__ == '__main__':
    unittest.main()