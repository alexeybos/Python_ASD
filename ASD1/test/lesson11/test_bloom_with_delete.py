from unittest import TestCase

import random
from ASD1.test.lesson11.bloom_with_delete import BloomFilter

class TestBloomFilter(TestCase):
    def test_hash2(self):
        self.fail()

    def test_bloom_recovery(self):
        bfilter = BloomFilter(32)
        bfilter.add("0123456789")
        bfilter.add("2345678901")
        bfilter.add("4567890123")
        bfilter.add("6789012345")
        bfilter.add("8901234567")

        bloom_real = bin(bfilter.bloom)
        eq = False
        interation = 0
        bfilter_new = BloomFilter(32)
        vals = []
        while (not eq) and (interation < 100000):
            vals = []
            i = 0
            while i < 5:
                str1 = ''
                for j in range(10):
                    str1 = str1 + str(random.randint(0, 9))
                if bfilter.is_value(str1):
                    i = i + 1
                    bfilter_new.add(str1)
                    vals.append(str1)
            eq = bloom_real == bin(bfilter_new.bloom)
            interation = interation + 1
        print(eq)
        print(interation)
        for v in vals:
            print(v)


