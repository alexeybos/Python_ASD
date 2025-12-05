# 7. Упорядоченный список
# 8.* Добавьте метод удаления всех дубликатов из упорядоченного списка.
# Сложность временная O(n) и пространственная O(1)
# 10.* Напишите метод проверки наличия заданного упорядоченного под-списка (параметр метода) в текущем списке.
# Сложность временная O(n) и пространственная O(1)

# 11.* Добавьте метод, который находит наиболее часто встречающееся значение в списке.
# Сложность временная O(n) и пространственная O(1)
#
# 12.* Добавьте в упорядоченный список возможность найти индекс элемента (параметр) в списке, которая должна работать за o(log N).
class Node:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None

class OrderedList:
    def __init__(self, asc):
        self.head = None
        self.tail = None
        self.__ascending = asc

    # 8.* Добавьте метод удаления всех дубликатов из упорядоченного списка.
    # Сложность временная O(n) и пространственная O(1)
    def delete_duplicates(self):
        node = self.head
        if node is None:
            return
        while node.next is not None:
            if node.value == node.next.value:
                self.__del_node(node)
            node = node.next

    def delete(self, val):
        node = self.find(val)
        self.__del_node(node)

    def __del_node(self, node: Node):
        if node is None:
            return
        if node.prev is None and node.next is None:
            self.clean(self.__ascending)
            return
        if self.head == node:
            self.head = node.next
            node.next.prev = None
            return
        if self.tail == node:
            self.tail = node.prev
            node.prev.next = None
            return
        node.prev.next = node.next
        node.next.prev = node.prev

    # 10.* Напишите метод проверки наличия заданного упорядоченного под-списка (параметр метода) в текущем списке.
    # Сложность временная O(n) и пространственная O(1)
    def check_sub_list_in_list(self, list) -> bool:
        if len(list) > self.len():
            return False
        i = 0
        node = self.find(list[i])
        if node is None:
            return False
        while node is not None:
            if node.value == list[i] and i == len(list) - 1:
                return True
            if node.value == list[i]:
                i += 1
            else:
                i = 0
            node = node.next
        return False

    # 11.* Добавьте метод, который находит наиболее часто встречающееся значение в списке.
    # Сложность временная O(n) и пространственная O(1)
    def find_most_frequent(self):
        node = self.head
        most_frequent = node.value
        cur_frequent = node.value
        max_cnt = 0
        cnt = 0
        while node is not None:
            if node.value == cur_frequent:
                cnt += 1
            else:
                cur_cnt = cnt
                cnt = 1
            if node.value != cur_frequent and cur_cnt > max_cnt:
                most_frequent = cur_frequent
                cur_frequent = node.value
                max_cnt = cur_cnt
            node = node.next
        return most_frequent

    # 12.* Добавьте в упорядоченный список возможность найти индекс элемента (параметр) в списке, которая должна работать за o(log N).
    def get_index(self, val):
        cnt = self.len()
        if self.head is None:
            return -1
        if self.head == val:
            return 0
        if self.tail == val:
            return cnt - 1
        node = self.head
        left_node = self.head
        left_index = 0
        right_index = cnt - 1
        mid = int((right_index - left_index) / 2)
        while left_index <= right_index:
            ind = 0
            for i in range(ind, mid):
                node = node.next
                ind += 1
            if self.__ascending:
                compare_result = self.compare(val, node.value)
            else:
                compare_result = self.compare(node.value, val)
            if compare_result == 0:
                return ind + left_index
            if compare_result == -1:
                right_index = ind + left_index - 1
                node = left_node
            else:
                left_index = ind + left_index + 1
                left_node = node.next
                node = node.next
            mid = int((right_index - left_index) / 2)
        return -1

    def compare(self, v1, v2):
        if v1 < v2:
            return -1
        elif v1 > v2:
            return 1
        return 0

    def add(self, value):
        new_node = Node(value)
        if self.__ascending:
            compare_result = -1
        else:
            compare_result = 1
        node = self.head
        # empty
        if node is None:
            self.head = new_node
            self.tail = new_node
            return
        # new head
        if self.compare(self.head.value, value) != compare_result:
            node.prev = new_node
            new_node.next = node
            self.head = new_node
            return
        # new tail
        if self.compare(self.tail.value, value) == compare_result:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
            return
        # usual
        while node is not None and self.compare(node.value, value) == compare_result:
            node = node.next
        new_node.prev = node.prev
        new_node.prev.next = new_node
        node.prev = new_node
        new_node.next = node

    def find(self, val):
        node = self.head
        if self.__ascending:
            expected_compare_result = -1
        else:
            expected_compare_result = 1
        while node is not None:
            compare_result = self.compare(node.value, val)
            if compare_result == 0:
                return node
            if compare_result != expected_compare_result:
                return None
            node = node.next
        return None

    def clean(self, asc):
        self.head = None
        self.tail = None
        self.__ascending = asc

    def len(self):
        cnt = 0
        node = self.head
        while node is not None:
            cnt += 1
            node = node.next
        return cnt

    def get_all(self):
        r = []
        node = self.head
        while node != None:
            r.append(node)
            node = node.next
        return r

class OrderedStringList(OrderedList):
    def __init__(self, asc):
        super(OrderedStringList, self).__init__(asc)

    def compare(self, v1, v2):
        str1 = v1.strip()
        str2 = v2.strip()
        if str1 == str2:
            return 0
        elif str1 > str2:
            return 1
        return -1
