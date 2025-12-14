from ASD1.test.lesson07.no_duplicate import *

# 9. Ассоциативный массив
#  5.* Реализуйте словарь с использованием упорядоченного списка по ключу для оптимизации производительности поиска.
#  В таком массиве поиск O(log(n)), вставка и удаление за счет смещения элементов O(n)
class OrderedDictionary():
    def __init__(self):
        self.keys = OrderedStringList(True)
        self.values = []

    def is_key(self, key):
        return self.keys.find(key) is not None

    def put(self, key, value):
        slot = self.keys.get_index(key)
        if slot != -1:
            self.values[slot] = value

        self.keys.add(key)
        slot = self.keys.get_index(key)
        self.values.insert(slot, value)

    def get(self, key):
        slot = self.keys.get_index(key)
        if slot == -1:
            return None
        return self.values[slot]