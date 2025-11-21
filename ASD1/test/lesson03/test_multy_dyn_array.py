from unittest import TestCase

from ASD1.test.lesson03.multy_dyn_array import MultyDynArray

class TestMultyDynArray(TestCase):
    def test_make_array(self):
        arr = MultyDynArray(3, 4, 3, 2)
        self.assertEqual(24, len(arr.array))

    def test_resize(self):
        arr = MultyDynArray(3, 2, 3, 4)
        arr.resize((3, 3, 4))
        self.assertEqual(36, len(arr.array))

    def test_append_to_empty(self):
        arr = MultyDynArray(3, 4, 3, 2)
        arr[0, 0, 0] = 1
        self.assertEqual(1, arr[0, 0, 0])

    def test_insert_out_bounds(self):
        arr = MultyDynArray(3, 4, 3, 2)
        arr[5, 0, 0] = 1
        self.assertEqual(1, arr[5, 0, 0])

    def test_get_real_index(self):
        arr = MultyDynArray(3, 4, 3, 2)
        #arr.get_real_index(0, 2, 2) #10
        self.assertEqual(10, arr.get_real_index(0, 2, 2))
        self.assertEqual(12, arr.get_real_index(1, 0, 0))
        self.assertEqual(23, arr.get_real_index(1, 2, 3))

        x, y, z = arr.retain_indices(10)
        self.assertEqual(0, x)
        self.assertEqual(2, y)
        self.assertEqual(2, z)

        x, y, z = arr.retain_indices(12)
        self.assertEqual(1, x)
        self.assertEqual(0, y)
        self.assertEqual(0, z)

        x, y, z = arr.retain_indices(23)
        self.assertEqual(1, x)
        self.assertEqual(2, y)
        self.assertEqual(3, z)

    def test_resize_by_add(self):
        arr = MultyDynArray(3, 4, 3, 2)
        arr[0, 0, 3] = 103 # index = 3 new_ = 3
        arr[0, 1, 0] = 104  # index = 4 new_index = 5
        arr[0, 2, 3] = 111 # index = 11 new_index = 13
        arr[1, 0, 0] = 112 # index = 12 new_index = 15
        self.assertEqual(103, arr[0, 0, 3])
        self.assertEqual(104, arr[0, 1, 0])
        self.assertEqual(4, arr.get_real_index(0, 1, 0))
        self.assertEqual(111, arr[0, 2, 3])
        self.assertEqual(11, arr.get_real_index(0, 2, 3))
        self.assertEqual(112, arr[1, 0, 0])
        self.assertEqual(12, arr.get_real_index(1, 0, 0))
        arr[0, 0, 4] = 1004 # new_index = 4
        self.assertEqual(103, arr[0, 0, 3])
        self.assertEqual(1004, arr[0, 0, 4])
        self.assertEqual(4, arr.get_real_index(0, 0, 4))
        self.assertEqual(104, arr[0, 1, 0])
        self.assertEqual(5, arr.get_real_index(0, 1, 0))
        self.assertEqual(111, arr[0, 2, 3])
        self.assertEqual(13, arr.get_real_index(0, 2, 3))
        self.assertEqual(112, arr[1, 0, 0])
        self.assertEqual(15, arr.get_real_index(1, 0, 0))