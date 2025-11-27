import ctypes

# 5. Очереди
# 6.* Реализуйте круговую (циклическую буферную) очередь статическим массивом фиксированного размера.
class RoundQueue:
    def __init__(self, size):
        self.max_size = size
        self.queue = (size * ctypes.py_object)()
        for i in range(size):
            self.queue[i] = None
        self.head_index, self.tail_index = 0, 0
        self.count = 0

    def is_full(self):
        return self.count >= self.max_size

    def enqueue(self, item):
        if self.is_full():
            raise Exception('Queue overflow')
        if self.count == 0:
            self.head_index, self.tail_index = 0, 0
        else:
            self.tail_index = self.__move_index_right(self.tail_index)
        self.queue[self.tail_index] = item
        self.count += 1

    def dequeue(self):
        if self.size() == 0:
            return None
        self.count -= 1
        val = self.queue[self.head_index]
        self.head_index = self.__move_index_right(self.head_index)
        return val

    def size(self):
        return self.count

    def __move_index_right(self, index):
        if index + 1 == self.max_size:
            return 0
        else:
            return index + 1
