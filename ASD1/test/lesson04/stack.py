class Stack:
    def __init__(self):
        self.stack = []
        self.min_values = []
        self.sum = 0

    def size(self):
        return len(self.stack)

    def pop(self):
        val = self.peek()
        if val is None:
            return None
        del self.stack[-1]
        if isinstance(val, (int, float)):
            self.sum -= val
        if isinstance(val, (int, float)) and val == self.min_values[-1]:
            self.min_values.pop()
        return val

    def push(self, value):
        self.stack.append(value)
        if isinstance(value, (int, float)):
            self.sum += value
        if isinstance(value, (int, float)) and (len(self.min_values) == 0 or value <= self.min_values[-1]):
            self.min_values.append(value)

    def peek(self):
        if self.size() == 0:
            return None
        val = self.stack[self.size() - 1]
        return val

    # 4. Стек
    # 7.* Добавьте в стек функцию, возвращающую текущий минимальный элемент в нём за O(1)
    def get_min_value(self):
        return self.min_values[-1]

    # 4. Стек
    # 8.* Добавьте в стек функцию, которая возвращает среднее значение всех элементов в стеке. Она должна выполняться за O(1).
    def get_average(self):
        return self.sum / self.size()