class MultiHashTable:
    def __init__(self, sz, stp):
        self.size = sz
        self.step = stp
        self.slots = [None] * self.size
        self.hashes = []
        self.hashes[0] = lambda val: self.hash_fun1(val)
        self.hashes[1] = lambda val: self.hash_fun2(val)
        self.hashes[2] = lambda val: self.hash_fun3(val)

    def hash_fun1(self, value):
        sum = 0
        for c in value:
            sum += ord(c)
        return sum % 17

    def hash_fun2(self, value):
        sum = 0
        for c in value:
            sum += ord(c)
        return ((11 * sum + 90) % 97) % 17

    def hash_fun3(self, value):
        sum = 0
        for c in value:
            sum += ord(c)
        return ((23 * sum + 53) % 79) % 17

    def seek_slot(self, value, search_val):
        slot = None
        for i in range(3):
            slot = self.hashes[i](value)
            if self.slots[slot] == search_val:
                return slot
        i = 0
        while i < self.step:
            if self.slots[slot] == search_val:
                return slot
            slot += self.step
            if slot >= self.size:
                slot -= self.size
                i += 1
        return None

    def put(self, value):
        slot = self.seek_slot(value, None)
        if slot is not None:
            self.slots[slot] = value
        return slot

    def find(self, value):
        slot = self.seek_slot(value, value)
        return slot




