from unittest import TestCase

from ASD1.lesson01.task01 import LinkedList, Node
from ASD1.test.lesson1.task01_2 import sum_one_size_lists

class Test(TestCase):
    def test_sum_one_size_lists_empty(self):
        list1 = LinkedList()
        list2 = LinkedList()
        list3 = sum_one_size_lists(list1, list2)
        self.assertEqual(list3.len(), 0)

    def test_sum_one_size_lists_one_node(self):
        list1 = LinkedList()
        list1.add_in_tail(Node(11))
        list2 = LinkedList()
        list2.add_in_tail(Node(22))
        list3 = sum_one_size_lists(list1, list2)
        self.assertEqual(list3.len(), 1)
        self.assertEqual(list3.head.value, 33)

    def test_sum_one_size_lists_not_one_size(self):
        list1 = LinkedList()
        list1.add_in_tail(Node(11))
        list1.add_in_tail(Node(55))
        list2 = LinkedList()
        list2.add_in_tail(Node(22))
        list2.add_in_tail(Node(33))
        list2.add_in_tail(Node(44))
        list3 = sum_one_size_lists(list1, list2)
        self.assertEqual(list3.len(), 0)

    def test_sum_one_size_lists(self):
        list1 = LinkedList()
        list1.add_in_tail(Node(11))
        list1.add_in_tail(Node(55))
        list1.add_in_tail(Node(100))
        list2 = LinkedList()
        list2.add_in_tail(Node(22))
        list2.add_in_tail(Node(33))
        list2.add_in_tail(Node(44))
        list3 = sum_one_size_lists(list1, list2)
        self.assertEqual(list3.len(), 3)
        self.assertEqual(list3.head.value, 33)
        self.assertEqual(list3.head.next.value, 88)
        self.assertEqual(list3.tail.value, 144)