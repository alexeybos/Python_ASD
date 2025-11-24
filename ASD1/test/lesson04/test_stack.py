from unittest import TestCase

from ASD1.test.lesson04.stack import Stack

class TestStack(TestCase):
    def test_get_min_value(self):
        stack = Stack()
        stack.push(5)
        stack.push(3)
        stack.push(4)
        stack.push(3)
        stack.push(1)
        stack.push(7)
        self.assertEqual(1, stack.get_min_value())
        stack.pop()
        self.assertEqual(1, stack.get_min_value())
        stack.pop()
        self.assertEqual(3, stack.get_min_value())
        stack.pop()
        self.assertEqual(3, stack.get_min_value())
        stack.pop()
        self.assertEqual(3, stack.get_min_value())
        stack.pop()
        self.assertEqual(5, stack.get_min_value())

    def test_get_average(self):
        stack = Stack()
        stack.push(5)
        self.assertEqual(5, stack.get_average())
        stack.push(3)
        self.assertEqual(4, stack.get_average())
        stack.push(7)
        self.assertEqual(5, stack.get_average())
        stack.pop()
        self.assertEqual(4, stack.get_average())

