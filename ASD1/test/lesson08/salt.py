import random

class SaltHashTable:
    def __init__(self, sz, stp):
        self.size = sz
        self.step = stp
        self.slots = [None] * self.size
        self.collision_cnt = 0
        self.salt = {}

    def hash_fun(self, value):
        sum = 0
        for c in value:
            sum += ord(c)
        return ((23 * sum + 53) % 79) % 17

    def seek_slot(self, value, search_val):
        slot = self.hash_fun(value)
        i = 0
        while i < self.step:
            if self.slots[slot] == search_val:
                return slot
            slot += self.step
            if search_val is None:
                self.collision_cnt += 1
            if slot >= self.size:
                slot -= self.size
                i += 1
        return None

    def get_salt_value(self, value):
        salt = self.salt.get(value)
        if salt is None:
            salt = value + 'salt frase' + str(random.randint(0, 100000000))
            self.salt.update({value: salt})
        return salt

    def put(self, value):
        salt_val = self.get_salt_value(value)
        slot = self.seek_slot(salt_val, None)
        if slot is not None:
            self.slots[slot] = value
        return slot

    def find(self, value):
        salt_val = self.get_salt_value(value)
        slot = self.seek_slot(salt_val, salt_val)
        return slot
