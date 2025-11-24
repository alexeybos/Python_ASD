from ASD1.test.lesson04.stack import Stack

# 4. Стек
# 5.* Напишите функцию, которая проверяет сбалансированность открывающих и закрывающих скобок
# Сложность временная и пространственная O(n)
def is_brackets_balanced(brackets: str) -> bool:
    stack = Stack()
    cur_char = '('
    for char in brackets:
        if char == '(':
            stack.push(char)
        else:
            cur_char = stack.pop()
        if cur_char is None:
            return False
    return stack.size() == 0

# 4. Стек
# 6.* Расширьте функцию проверки сбалансированности скобок, если скобки могут быть трех типов: (), {}, [].
# Сложность временная и пространственная O(n)
def is_brackets_balanced_extended(brackets: str) -> bool:
    stack = Stack()
    dct = {'(': ')', '[': ']', '{': '}'}
    is_bracket_equal = True
    for char in brackets:
        if char in dct.keys():
            stack.push(dct.get(char))
        else:
            is_bracket_equal = stack.pop() == char
        if not is_bracket_equal:
            return False
    return stack.size() == 0

# 4. Стек
# 9*. Напишите функцию, которая с помощью двух стеков реализует вычисление постфиксных выражений.
# Сложность временная и пространственная O(n)
def calc_postfix_expression(expression: str):
    stack1 = Stack()
    stack2 = Stack()
    lambda_sum = lambda x, y: x + y
    lambda_subtract = lambda x, y: x - y
    lambda_prod = lambda x, y: x * y
    lambda_div = lambda x, y: x / y
    operators = {'+': lambda_sum, '-': lambda_subtract, '*': lambda_prod, '/': lambda_div}
    result = 0
    expression_as_list = expression[::-1].split()
    for item in expression_as_list:
        stack1.push(item)
    item = stack1.pop()
    while item is not None and item != '=':
        if item in operators.keys():
            x = stack2.pop()
            y = stack2.pop()
            result = operators[item](int(x), int(y))
            stack2.push(result)
        else:
            stack2.push(item)
        item = stack1.pop()
    return result

