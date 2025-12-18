from __future__ import annotations
from typing import Any
# 10. Множества
# 6.* Реализуйте мульти-множество (Bag), в котором каждый элемент может присутствовать несколько раз.
# Добавьте методы добавления элементов, удаления одного экземпляра элемента и получения списка всех элементов с их частотами (сколько раз встречаются).
class Bag:
    def __init__(self):
        self._data = {}
        self._size = 0

    def put(self, key, freq = 1):
        if key in self._data:
            self._data[key] = self._data[key] + freq
        else:
            self._data[key] = freq
        self._size += freq

    def remove_first(self, key):
        if key in self._data:
            self._size -= 1
        if key in self._data and self._data[key] > 1:
            self._data[key] = self._data[key] - 1
        else:
            self._data.pop(key)

    def get_elements_with_freq(self):
        return self._data

    def get(self, value: Any) -> bool :
        return value in self._data

    def get_freq(self, value: Any) -> bool :
        return self._data.get(value, 0)

    def size(self) -> int:
        return int(self._size)

    def intersection(self, set2: Bag) -> Bag:
        result = Bag()
        for key in self._data:
            freq = set2.get_freq(key)
            if freq > 0:
                result.put(key, min(self._data[key], freq))
        return result

    def union(self, set2: Bag) -> Bag:
        result = Bag()
        for key in self._data:
            result.put(key, self._data[key])
        for key in set2._data:
            result.put(key, set2._data[key])
        return result

    def difference(self, set2: Bag) -> Bag:
        result = Bag()
        for key in self._data:
            freq = set2.get_freq(key)
            if freq < self._data[key]:
                result.put(key, self._data[key] - freq)
        return result

    def issubset(self, set2: Bag) -> bool:
        diff = set2.difference(self)
        return diff.size() == 0

    def equals(self, set2: Bag) -> bool:
        diff = set2.difference(self)
        return diff.size() == 0