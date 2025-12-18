from unittest import TestCase

from ASD1.test.lesson10.ext_power_set import PowerSet
from ASD1.test.lesson10.bag import Bag

class TestPowerSet(TestCase):
    def test_cartesian(self):
        my_set1 = PowerSet()
        my_set2 = PowerSet()
        my_set1.put(10)
        my_set1.put(11)
        my_set1.put('meow')
        my_set2.put(100)
        my_set2.put(111)

        result = my_set1.cartesian(my_set2)
        self.assertEqual(6, result.size())
        self.assertTrue(result.get((10,100)))
        self.assertTrue(result.get((10,111)))
        self.assertTrue(result.get((11,100)))
        self.assertTrue(result.get((11,111)))
        self.assertTrue(result.get(('meow', 100)))
        self.assertTrue(result.get(('meow', 111)))

        result = my_set2.cartesian(my_set1)
        self.assertEqual(6, result.size())
        self.assertTrue(result.get((100, 10)))
        self.assertTrue(result.get((100, 11)))
        self.assertTrue(result.get((100, 'meow')))
        self.assertTrue(result.get((111, 10)))
        self.assertTrue(result.get((111, 11)))
        self.assertTrue(result.get((111, 'meow')))

    def test_bag(self):
        my_set1 = Bag()
        my_set2 = Bag()
        my_set1.put(10)
        my_set1.put(11)
        my_set1.put('meow')
        my_set2.put(10)
        my_set2.put(10)
        my_set2.put(111)
        res = my_set1.union(my_set2)
        self.assertEqual(6, res.size())
        res = my_set1.intersection(my_set2)
        self.assertEqual(1, res.size())
        res = my_set1.difference(my_set2)
        self.assertEqual(2, res.size())
        res = my_set2.difference(my_set1)
        self.assertEqual(2, res.size())