from ASD1.test.lesson10.bag import Bag

class BloomFilter:

    def __init__(self, f_len):
        self.filter_len = f_len
        self.bloom = int(2 << (f_len - 1))
        self.counter = Bag()

    def delete(self, str1):
        index1 = 1 << self.hash1(str1)
        index2 = 1 << self.hash2(str1)
        self.counter.remove_first(index1)
        self.counter.remove_first(index2)
        if self.counter.get_freq(index1) < 1 and self.counter.get_freq(index2) < 1:
            self.bloom = self.bloom & ~index1
            self.bloom = self.bloom & ~index2

    def hash1(self, str1):
        prev_res = 0
        i = 1
        for c in str1:
            code = ord(c)
            prev_res = (prev_res * 17 + code * i) % self.filter_len
            i = i + 1
        return prev_res

    def hash2(self, str1):
        prev_res = 0
        i = 1
        for c in str1:
            code = ord(c)
            prev_res = (prev_res * 223 + code * i) % self.filter_len
            i = i + 1
        return prev_res

    def add(self, str1):
        index1 = 1 << self.hash1(str1)
        index2 = 1 << self.hash2(str1)
        self.bloom = self.bloom | index1
        self.bloom = self.bloom | index2
        self.counter.put(index1)
        self.counter.put(index2)

    def is_value(self, str1):
        index1 = 1 << self.hash1(str1)
        index2 = 1 << self.hash2(str1)
        return ((self.bloom & index1) == index1) and ((self.bloom & index2) == index2)