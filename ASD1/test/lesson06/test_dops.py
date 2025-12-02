from unittest import TestCase

from ASD1.test.lesson06.dops import is_palindrome, is_parenthesis_balanced
from ASD1.test.lesson06.min_deque import MinDeque
from ASD1.test.lesson06.dyn_arr_deque import DynArrayDeque


class Test(TestCase):
    def test_is_palindrome(self):
        self.assertTrue(is_palindrome(''))
        self.assertTrue(is_palindrome("А роза упала на лапу Азора"))
        self.assertFalse(is_palindrome("А роза не упала на лапу Азора"))
        self.assertTrue(is_palindrome(""))
        self.assertTrue(is_palindrome("Лёша на полке клопа нашёл"))
        self.assertTrue(is_palindrome("Anna"))
        self.assertTrue(is_palindrome("Madam, I’m Adam"))


    def test_min_deque(self):
        min_deque = MinDeque()
        min_deque.addFront(5)
        min_deque.addFront(6)
        min_deque.addFront(4)
        min_deque.addTail(8)
        min_deque.addTail(5)
        min_deque.addTail(1)
        self.assertEqual(1, min_deque.get_min())
        min_deque.removeTail()
        self.assertEqual(4, min_deque.get_min())
        min_deque.removeTail()
        self.assertEqual(4, min_deque.get_min())
        min_deque.removeTail()
        min_deque.removeFront()
        self.assertEqual(5, min_deque.get_min())

    def test_dyn_arr_deque(self):
        deque = DynArrayDeque()
        for i in range(8):
            deque.addFront(i + 1)
        self.assertEqual(8, deque.size())
        for i in range(8, 16):
            deque.addTail(i + 2)
        self.assertEqual(16, deque.size())
        self.assertEqual(16, deque.arr.capacity)
        deque.addFront(0)
        self.assertEqual(32, deque.arr.capacity)
        self.assertEqual(17, deque.size())

        self.assertEqual(0, deque.removeFront())
        self.assertEqual(17, deque.removeTail())

    def test_is_parenthesis_balanced(self):
        self.assertTrue(is_parenthesis_balanced(''))
        self.assertTrue(is_parenthesis_balanced('(2 + 3)*(abs[1] - 8)'))
        self.assertTrue(is_parenthesis_balanced('(2 + {3})*{(abs[1] - 8)}'))
        self.assertFalse(is_parenthesis_balanced('(2 + [{3})]*{(abs[1] - 8)}'))
