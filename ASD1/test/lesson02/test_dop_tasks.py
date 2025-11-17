from unittest import TestCase

from ASD1.test.lesson02.dop_tasks import LinkedList2, Node

class TestLinkedList2(TestCase):
    def test_revert_list_empty(self):
        list = LinkedList2()
        list.revert_list()
        self.assertIsNone(list.head)
        self.assertIsNone(list.tail)
        self.assertEqual(0, list.len())

    def test_revert_list_one(self):
        list = LinkedList2()
        list.add_in_tail(Node(5))
        list.revert_list()
        self.assertEqual(1, list.len())
        self.assertEqual(5, list.head.value)
        self.assertEqual(5, list.tail.value)


    def test_revert_list_many(self):
        list = LinkedList2()
        list.add_in_tail(Node(1))
        list.add_in_tail(Node(2))
        list.add_in_tail(Node(3))
        list.add_in_tail(Node(4))
        list.revert_list()
        self.assertEqual(4, list.len())
        node = list.head
        for i in range(4, 0, -1):
            self.assertEqual(i, node.value)
            node = node.next

    def test_has_cycles(self):
        list = LinkedList2()
        self.assertFalse(list.has_cycles())

    def test_has_cycles_one(self):
        list = LinkedList2()
        list.add_in_tail(Node(5))
        self.assertFalse(list.has_cycles())

    def test_has_cycles_two_no(self):
        list = LinkedList2()
        list.add_in_tail(Node(5))
        list.add_in_tail(Node(7))
        self.assertFalse(list.has_cycles())

    def test_has_cycles_many_no(self):
        list = LinkedList2()
        list.add_in_tail(Node(5))
        list.add_in_tail(Node(7))
        list.add_in_tail(Node(9))
        list.add_in_tail(Node(3))
        self.assertFalse(list.has_cycles())

    def test_has_cycles_many_yes(self):
        list = LinkedList2()
        list.add_in_tail(Node(5))
        list.add_in_tail(Node(7))
        list.add_in_tail(Node(9))
        list.add_in_tail(Node(3))
        list.head.prev = list.tail
        list.tail.next = list.head
        self.assertTrue(list.has_cycles())

    def test_sort_empty(self):
        list = LinkedList2()
        list.sort()
        self.assertIsNone(list.head)
        self.assertIsNone(list.tail)
        self.assertEqual(0, list.len())

    def test_sort_one(self):
        list = LinkedList2()
        list.add_in_tail(Node(5))
        list.sort()
        self.assertEqual(1, list.len())
        self.assertEqual(5, list.head.value)
        self.assertEqual(5, list.tail.value)

    def test_sort_two_no(self):
        list = LinkedList2()
        list.add_in_tail(Node(5))
        list.add_in_tail(Node(7))
        list.sort()
        self.assertEqual(2, list.len())
        self.assertEqual(5, list.head.value)
        self.assertEqual(7, list.tail.value)

    def test_sort_two_yes(self):
        list = LinkedList2()
        list.add_in_tail(Node(7))
        list.add_in_tail(Node(5))
        list.sort()
        self.assertEqual(2, list.len())
        self.assertEqual(5, list.head.value)
        self.assertEqual(7, list.tail.value)

    def test_sort_many_yes(self):
        list = LinkedList2()
        list.add_in_tail(Node(4))
        list.add_in_tail(Node(7))
        list.add_in_tail(Node(6))
        list.add_in_tail(Node(3))
        list.add_in_tail(Node(5))
        list.sort()
        self.assertEqual(5, list.len())
        node = list.head
        for i in range(3, 8):
            self.assertEqual(i, node.value)
            node = node.next
