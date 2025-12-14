from unittest import TestCase

from ASD1.test.lesson09.bit_dict import BitDictionary

class TestBitDictionary(TestCase):
    def test_bit_dict(self):
        bit_dict = BitDictionary(8)
        bit_dict.put("01010101", "value1")
        self.assertEqual(bit_dict.get("01010101"), "value1")
        bit_dict.put("01111101", "value2")
        bit_dict.put("01010101", "value3")
        self.assertEqual(bit_dict.get("01111101"), "value2")
        self.assertEqual(bit_dict.get("01010101"), "value3")
