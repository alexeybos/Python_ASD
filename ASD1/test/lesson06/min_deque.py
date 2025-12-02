from ASD1.lesson06.task06 import Deque
from ASD1.lesson04.task04 import Stack

# 6. Двусторонняя очередь (deque)
# 7.4.* Напишите метод, который возвращает минимальный элемент деки за O(1).
class MinDeque(Deque):
    def __init__(self):
        super().__init__()
        self.min_head = Stack()
        self.min_tail = Stack()

    def get_min(self):
        if self.min_tail.size() == 0 and self.min_head.size() == 0:
            return None
        elif self.min_tail.size() == 0:
            return self.min_head.peek()
        elif self.min_head.size() == 0:
            return self.min_tail.peek()
        val_min_head = self.min_head.peek()
        val_min_tail = self.min_tail.peek()
        return min(val_min_head, val_min_tail)

    def remove_min(self, val, stack1: Stack, stack2: Stack):
        if stack1.size() > 0 and stack1.peek() == val:
            return stack1.pop()
        while stack2.size() > 0 and stack2.peek() >= val:
            stack1.push(stack2.pop())
        return stack1.pop()

    def addFront(self, item):
        if self.min_head.size() == 0 or item <= self.min_head.peek():
            self.min_head.push(item)
        super().addFront(item)

    def addTail(self, item):
        if self.min_tail.size() == 0 or item <= self.min_tail.peek():
            self.min_tail.push(item)
        super().addTail(item)

    def removeFront(self):
        val = super().removeFront()
        if val is not None:
            self.remove_min(val, self.min_head, self.min_tail)
        return val

    def removeTail(self):
        val = super().removeTail()
        if val is not None:
            self.remove_min(val, self.min_tail, self.min_head)
        return val

