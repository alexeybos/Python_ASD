from unittest import TestCase

from ASD1.test.lesson08.lesson08 import DynHashTable

class TestDynHashTable(TestCase):
    def test_resize(self):
        table = DynHashTable()
        for i in range(11):
            table.put(str(i))
        self.assertEqual(11, table.count)
        self.assertEqual(16, table.capacity)
        table.put('123')
        self.assertEqual(12, table.count)
        self.assertEqual(32, table.capacity)
        self.assertIsNotNone(table.find('123'))
        for i in range(11):
            self.assertIsNotNone(table.find(str(i)))
