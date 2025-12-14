from unittest import TestCase

from ASD1.test.lesson09.ordered_dict import OrderedDictionary

class TestOrderedDictionary(TestCase):
    def test_put(self):
        dict = OrderedDictionary()
        dict.put('9', 'value9')
        self.assertEqual('value9', dict.get('9'))
        dict.put('4', 'value4')
        self.assertEqual('value9', dict.get('9'))
        self.assertEqual('value4', dict.get('4'))
        dict.put('5', 'value5')
        self.assertEqual('value9', dict.get('9'))
        self.assertEqual('value4', dict.get('4'))
        self.assertEqual('value5', dict.get('5'))
        dict.put('10', 'value10')
        self.assertEqual('value9', dict.get('9'))
        self.assertEqual('value4', dict.get('4'))
        self.assertEqual('value5', dict.get('5'))
        self.assertEqual('value10', dict.get('10'))
        dict.put('15', 'value15')
        self.assertEqual('value9', dict.get('9'))
        self.assertEqual('value4', dict.get('4'))
        self.assertEqual('value5', dict.get('5'))
        self.assertEqual('value10', dict.get('10'))
        self.assertEqual('value15', dict.get('15'))

        self.assertEqual('value10', dict.values[0])
        self.assertEqual('value15', dict.values[1])
        self.assertEqual('value4', dict.values[2])
        self.assertEqual('value5', dict.values[3])
        self.assertEqual('value9', dict.values[4])
