from unittest import TestCase

from ASD1.test.lesson08.salt import SaltHashTable

class TestSaltHashTable(TestCase):
    def test_put(self):
        stab = SaltHashTable(17, 3)
        self.assertEqual(7, stab.hash_fun('hash'))
        self.assertEqual(7, stab.hash_fun('hash ok'))
        self.assertEqual(7, stab.hash_fun('1010101ку'))
        self.assertEqual(7, stab.hash_fun('1sd0qww10101ку'))
        self.assertEqual(7, stab.hash_fun('wegwfgwefc11111111'))

        # без соли 4 коллизии
        # с солью 0 - 1 коллизия
        stab.put('hash')
        stab.put('hash ok')
        stab.put('1010101ку')
        stab.put('1sd0qww10101ку')
        stab.put('wegwfgwefc11111111')
        print(f'collision_cnt = {stab.collision_cnt}')
