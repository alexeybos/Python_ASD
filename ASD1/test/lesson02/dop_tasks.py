class Node:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None

class LinkedList2:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_in_tail(self, item):
        if self.head is None:
            self.head = item
            item.prev = None
            item.next = None
        else:
            self.tail.next = item
            item.prev = self.tail
        self.tail = item

    def find(self, val):
        node = self.head
        while node is not None:
            if node.value == val:
                return node
            node = node.next
        return None

    def find_all(self, val):
        find_result = []
        node = self.head
        while node is not None:
            if node.value == val:
                find_result.append(node)
            node = node.next
        return find_result

    def delete(self, val, all=False):
        node = self.head
        while node is not None:
            if node.value == val:
                if self.head == node:
                    self.head = node.next
                else:
                    node.prev.next = node.next
                if self.tail == node:
                    self.tail = node.prev
                else:
                    node.next.prev = node.prev
                if not all:
                    return
            node = node.next

    def clean(self):
        self.head = None
        self.tail = None

    def len(self):
        node = self.head
        cnt = 0
        while node != None:
            cnt += 1
            node = node.next
        return cnt

    def insert(self, afterNode, newNode):
        node = self.head
        if afterNode is None:
            self.add_in_tail(newNode)
            return
        while node is not None:
            if node == afterNode:
                newNode.prev = node
                newNode.next = node.next
                node.next = newNode
                if self.tail == node:
                    self.tail = newNode
            node = node.next

    def add_in_head(self, newNode):
        newNode.next = self.head
        newNode.prev = None
        if self.head == None:
            self.tail = newNode
        self.head = newNode

# 2. Двунаправленный связный (связанный) список
# 2.10.* Метод, который "переворачивает" порядок элементов в связном списке.
# Сложность временная O(n) и пространственная O(1)
    def revert_list(self):
        node = self.head
        self.head = self.tail
        self.tail = node
        while node is not None:
            prev_node = node.prev
            node.prev = node.next
            node.next = prev_node
            node = node.prev

# 2. Двунаправленный связный (связанный) список
#2.11.* Добавьте булев метод, который сообщает, имеются ли циклы (замкнутые на себя по кругу) внутри списка.
# Сложность временная O(n) и пространственная O(1)
    def has_cycles(self) -> bool:
        if self.head is None or self.head.next is None:
            return False
        node = self.head
        fast_node = self.head.next
        while node != fast_node:
            if fast_node.next is None or fast_node.next.next is None:
                return False
            fast_node = fast_node.next.next
            node = node.next
        return True

# 2. Двунаправленный связный (связанный) список
#2.12.* Добавьте метод, сортирующий список.
# Использовалась сортировка слиянием. Сложность временная O(n log n), пространственная: O(log n)
    def sort(self):
        list = self.__merge_sort(self)
        self.head = list.head
        self.tail = list.tail

    def __merge_sort(self, list):
        size = list.len()
        if size < 2:
            return list
        left_list = LinkedList2()
        right_list = LinkedList2()
        node = list.head
        for i in range(int(size / 2)):
            left_list.add_in_tail(Node(node.value))
            node = node.next
        for i in range(int(size / 2), size):
            right_list.add_in_tail(Node(node.value))
            node = node.next

        left_list = self.__merge_sort(left_list)
        right_list = self.__merge_sort(right_list)
        return self.__merge(left_list, right_list)

    def __merge(self, list1, list2):
        merged_list = LinkedList2()
        node1 = list1.head
        node2 = list2.head
        while node1 is not None and node2 is not None:
            if node1.value < node2.value:
                merged_list.add_in_tail(Node(node1.value))
                node1 = node1.next
            else:
                merged_list.add_in_tail(Node(node2.value))
                node2 = node2.next
        while node1 is not None:
            merged_list.add_in_tail(Node(node1.value))
            node1 = node1.next
        while node2 is not None:
            merged_list.add_in_tail(Node(node2.value))
            node2 = node2.next
        return merged_list

# 2. Двунаправленный связный (связанный) список
#2.13.* Добавьте метод, объединяющий два списка в третий. Cписки предварительно отсортировать, и выдать результирующий список, в котором все элементы также будут упорядочены.
# Т.к. использоется сортировка слиянием, сложность временная O(n log n), пространственная: O(log n)
    def sort_and_union(self, list1, list2):
        list1.sort()
        list2.sort()
        return self.__merge(list1, list2)