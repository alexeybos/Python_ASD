from unittest import TestCase

from ASD1.test.lesson04.head_stack import HeadStack

class TestHeadStack(TestCase):
    def test_push(self):
        stack = HeadStack()
        stack.push(11)
        self.assertEqual(11, stack.stack[0])
        stack.push(22)
        self.assertEqual(22, stack.stack[0])
        stack.push(33)
        self.assertEqual(33, stack.stack[0])

    def test_size(self):
        stack = HeadStack()
        stack.push(11)
        self.assertEqual(1, stack.size())
        stack.push(12)
        self.assertEqual(2, stack.size())
        stack.push(13)
        self.assertEqual(3, stack.size())

    def test_peek(self):
        stack = HeadStack()
        self.assertIsNone(stack.peek())
        stack.push(11)
        self.assertEqual(1, stack.size())
        self.assertEqual(11, stack.peek())
        stack.push(12)
        self.assertEqual(2, stack.size())
        self.assertEqual(12, stack.peek())
        stack.push(13)
        self.assertEqual(3, stack.size())
        self.assertEqual(13, stack.peek())

    def test_pop(self):
        stack = HeadStack()
        stack.push(11)
        stack.push(12)
        stack.push(13)
        self.assertEqual(13, stack.pop())
        self.assertEqual(12, stack.pop())
        self.assertEqual(11, stack.pop())
        self.assertIsNone(stack.pop())
        self.assertIsNone(stack.peek())
