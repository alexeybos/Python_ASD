# 3. Динамические массивы
# 3.5.* Реализуйте динамический массив на основе банковского метода.
import ctypes

class BankDynArray:

    def __init__(self):
        self.count = 0
        self.capacity = 16
        self.bank = 0
        self.array = self.make_array(self.capacity)

    def __len__(self):
        return self.count

    def make_array(self, new_capacity):
        return (new_capacity * ctypes.py_object)()

    def __getitem__(self, i):
        if i < 0 or i >= self.count:
            raise IndexError('Index is out of bounds')
        return self.array[i]

    def resize(self, new_capacity):
        new_array = self.make_array(new_capacity)
        for i in range(self.count):
            new_array[i] = self.array[i]
        # Тратим сэкономленное
        if new_capacity > self.capacity:
            self.bank -= new_capacity - self.capacity
        else:
            self.bank -= int((self.capacity - new_capacity) * 0.1)
        self.array = new_array
        self.capacity = new_capacity


    def append(self, itm):
        # ресайз делаем также по факту полной заполненности массива. Хотя можно, например, по определенному порогу в self.bank
        if self.count == self.capacity:
            self.resize(2 * self.capacity)
        else:
            self.bank += 2  # откладываем на реаллокацию
        self.array[self.count] = itm
        self.count += 1


    def insert(self, i, itm):
        if i < 0 or i > self.count:
            raise IndexError('Index is out of bounds')
        if self.count >= self.capacity:
            self.resize(2 * self.capacity)
        else:
            self.bank += 1  # откладываем на реаллокацию
        for ind in range(self.count, i, -1):
            self.array[ind] = self.array[ind - 1]
        self.array[i] = itm
        self.count += 1

    def delete(self, i):
        if i < 0 or i >= self.count:
            raise IndexError('Index is out of bounds')
        if self.count <= self.capacity / 2 and self.capacity > 16:
            self.resize(max(16, int(self.capacity / 1.5)))
        else:
            self.bank += 1  # откладываем на реаллокацию
        for ind in range(i, self.count - 1):
            self.array[ind] = self.array[ind + 1]
        self.count -= 1



