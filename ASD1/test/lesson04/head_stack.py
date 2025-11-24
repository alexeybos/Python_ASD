# 4. Стек
# 4.2 Переделайте реализацию стека так, чтобы она работала не с хвостом списка как с верхушкой стека, а с его головой
# Сложность pop() - O(n); push() O(n) - т.к. при удалении и вставке первого элемента всегда происходит сдвиг массива
class HeadStack:
    def __init__(self):
        self.stack = []

    def size(self):
        return len(self.stack)

    def pop(self):
        val = self.peek()
        if val is None:
            return None
        del self.stack[0]
        return val

    def push(self, value):
        self.stack.insert(0, value)

    def peek(self):
        if self.size() == 0:
            return None
        val = self.stack[0]
        return val