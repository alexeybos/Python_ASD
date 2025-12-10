from ASD1.lesson03.task03 import DynArray

class DynHashTable():
    def __init__(self):
        self.capacity = 16
        self.step = 3
        self.count = 0
        self.slots = DynArray()
        for i in range(self.slots.capacity):
            self.slots.append(None)

    def hash_fun(self, value):
        sum = 0
        for c in value:
            sum += ord(c)
        return sum % self.capacity

    def seek_slot(self, value):
        slot = self.hash_fun(value)
        i = 0
        while i < self.step:
            if self.slots[slot] is None:
                return slot
            slot += self.step
            if slot >= self.capacity:
                slot -= self.capacity
                i += 1
        return None

    def put(self, value):
        self.__resize_if_need()
        slot = self.seek_slot(value)
        if slot is not None:
            self.slots[slot] = value
            self.count += 1
        return slot

    def find(self, value):
        slot = self.hash_fun(value)
        i = 0
        if slot is None:
            return None
        while i < self.step:
            if self.slots[slot] == value:
                return slot
            slot += self.step
            if slot >= self.capacity:
                slot -= self.capacity
                i += 1
        return None

    def __resize_if_need(self):
        if (self.count + 1) / self.capacity < 0.75:
            return
        tmp_table = []
        new_capacity = self.capacity * 2
        self.slots.resize(new_capacity)
        for i in range(self.capacity):
            tmp_table.append(self.slots[i])
            self.slots[i] = None
        for i in range(self.capacity, new_capacity):
            self.slots.append(None)
        self.capacity = new_capacity
        # делаю rehash
        self.count = 0
        for el in tmp_table:
            if el is not None:
                self.put(el)
