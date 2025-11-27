from ASD1.lesson04.task04 import Stack

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
        return self.stack1.size() + self.stack2.size() # размер очереди