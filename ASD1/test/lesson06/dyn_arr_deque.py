from ASD1.lesson03.task03 import DynArray

# 6. Двусторонняя очередь (deque)
# 7.5.* Реализуйте двустороннюю очередь с помощью динамического массива.
# Методы добавления и удаления элементов с обоих концов деки работают за амортизированное время o(1)
class DynArrayDeque:
    def __init__(self):
        self.arr = DynArray()
        self.count = 0
        self.head = None
        self.tail = None
        for i in range(self.arr.capacity):
            self.arr.append(None)

    def addFront(self, item):
        index_for_ins = self.__move_index_right(self.head)
        if index_for_ins == self.tail:
            self.resize_array()
            index_for_ins = self.head
        if self.tail is None:
            self.tail = 0
        self.count += 1
        self.arr.array[index_for_ins] = item
        self.head = index_for_ins

    def addTail(self, item):
        index_for_ins = self.__move_index_left(self.tail)
        if index_for_ins == self.head:
            self.resize_array()
            index_for_ins = self.tail
        if self.head is None:
            self.head = 0
        self.count += 1
        self.arr.array[index_for_ins] = item
        self.tail = index_for_ins

    def removeFront(self):
        if self.size() == 0:
            return None
        self.count -= 1
        val = self.arr.array[self.head]
        self.arr.array[self.head] = None
        self.head = self.__move_index_left(self.head)
        if self.size() == 0:
            self.head = None
            self.tail = None
        return val

    def removeTail(self):
        if self.size() == 0:
            return None
        self.count -= 1
        val = self.arr.array[self.tail]
        self.arr.array[self.tail] = None
        self.tail = self.__move_index_right(self.tail)
        if self.size() == 0:
            self.head = None
            self.tail = None
        return val

    def size(self):
        return self.count

    def __move_index_right(self, index_for_move):
        if index_for_move is None or index_for_move + 1 == self.arr.capacity:
            return 0
        return index_for_move + 1

    def __move_index_left(self, index_for_move):
        if index_for_move is None:
            return 0
        if index_for_move == 0:
            return self.arr.capacity - 1
        return index_for_move - 1

    def resize_array(self):
        real_deque = []
        index = self.tail
        for i in range(self.arr.capacity):
            real_deque.append(self.arr[index])
            index = self.__move_index_right(index)
        for i in range(self.arr.capacity):
            self.arr.array[i] = real_deque[i]
        self.arr.append(None)
        for i in range(self.count, self.arr.capacity):
            self.arr.array[i] = None
        self.head = self.count - 1
        self.tail = 0
