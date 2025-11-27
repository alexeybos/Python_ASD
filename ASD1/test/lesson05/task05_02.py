from ASD1.lesson05.task05 import Queue
from ASD1.lesson04.task04 import Stack
# 5. Очереди
# 3.* Напишите функцию, которая "вращает" очередь по кругу на N элементов.
# Сложность временная О(n) и пространственная О(1)
def queue_rotate(queue, shift):
    for i in range(shift):
        queue.enqueue(queue.dequeue())

# 5. Очереди
# 4.* Реализуйте очередь с помощью двух стеков.
# Сложность enqueue О(1) и dequeue О(n)
class QueueByStacks:
    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()

    def enqueue(self, item):
        self.stack1.push(item)

    def dequeue(self):
        if self.stack2.size() > 0:
            return self.stack2.pop()
        while self.stack1.size() > 0:
            self.stack2.push(self.stack1.pop())
        return self.stack2.pop()

    def size(self):
        return self.stack1.size() + self.stack2.size()

# 5. Очереди
# 5.* Добавьте функцию, которая обращает все элементы в очереди в обратном порядке.
# Сложность временная О(n) и пространственная О(n)
def queue_reverse(queue):
    stack = Stack()
    while queue.size() > 0:
        stack.push(queue.dequeue())
    while stack.size() > 0:
        queue.enqueue(stack.pop())

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
