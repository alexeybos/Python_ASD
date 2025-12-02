from ASD1.lesson06.task06 import Deque
from ASD1.lesson04.task04 import Stack

# 6. Двусторонняя очередь (deque)
#  7.3.* Напишите функцию, которая с помощью deque проверяет, является ли некоторая строка палиндромом (читается одинаково слева направо и справа налево).
# Сложность временная O(n) и пространственная O(n)
def is_palindrome(str_for_check) -> bool:
    deque = Deque()
    for char in str_for_check:
        if char.isalpha():
            deque.addFront(char.lower())
    while deque.size() > 1:
        if deque.removeFront() != deque.removeTail():
            return False
    return True

# 6. Двусторонняя очередь (deque)
# 7.6.* Напишите автономную функцию, которая проверяет баланс скобок в символьном выражении. Внутри этой функции используйте стек.
# Алгоритм должен работать за O(N)
def is_parenthesis_balanced(str_for_check) -> bool:
    stack = Stack()
    dct = {'(': ')', '[': ']', '{': '}'}
    is_bracket_equal = True
    for char in str_for_check:
        if char in dct.keys():
            stack.push(dct.get(char))
        elif char in dct.values():
            is_bracket_equal = stack.pop() == char
        if not is_bracket_equal:
            return False
    return stack.size() == 0