class Node:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None

class DummyNode(Node):
    def __init__(self):
        super().__init__(None)

class TwoDummyLinkedList:
    def __init__(self):
        self.head = DummyNode()
        self.tail = DummyNode()
        self.head.next = self.tail
        self.tail.prev = self.head

    def get_head(self):
        if type(self.head.next) == DummyNode:
            return None
        return self.head.next

    def get_tail(self):
        if type(self.tail.prev) == DummyNode:
            return None
        return self.tail.prev

    def add_in_tail(self, item):
        self.tail.prev.next = item
        item.prev = self.tail.prev
        self.tail.prev = item
        item.next = self.tail

    def delete(self, val, all=False):
        node = self.head.next
        while type(node) is not DummyNode:
            if node.value == val:
                node.prev.next = node.next
                node.next.prev = node.prev
                if not all:
                    return
            node = node.next

    def len(self):
        node = self.head.next
        cnt = 0
        while type(node) is not DummyNode:
            cnt += 1
            node = node.next
        return cnt

    def insert(self, afterNode, newNode):
        node = self.head.next
        while type(node) is not DummyNode:
            if node == afterNode:
                newNode.next = node.next
                node.next = newNode
                newNode.prev = node
                return
            node = node.next

    def add_in_head(self, newNode):
        newNode.prev = self.head
        newNode.next = self.head.next
        self.head.next.prev = newNode
        self.head.next = newNode

class OneDummyLinkedList:
    def __init__(self):
        node = DummyNode()
        self.dummy_node = node
        self.dummy_node.next = self.dummy_node
        self.dummy_node.prev = self.dummy_node

    def get_head(self):
        if type(self.dummy_node.next) == DummyNode:
            return None
        return self.dummy_node.next

    def get_tail(self):
        if type(self.dummy_node.prev) == DummyNode:
            return None
        return self.dummy_node.prev

    def add_in_tail(self, item):
        self.dummy_node.prev.next = item
        item.prev = self.dummy_node.prev
        self.dummy_node.prev = item
        item.next = self.dummy_node

    def delete(self, val, all=False):
        node = self.dummy_node.next
        while type(node) is not DummyNode:
            if node.value == val:
                node.prev.next = node.next
                node.next.prev = node.prev
                if not all:
                    return
            node = node.next

    def len(self):
        node = self.dummy_node.next
        cnt = 0
        while type(node) is not DummyNode:
            cnt += 1
            node = node.next
        return cnt

    def insert(self, afterNode, newNode):
        node = self.dummy_node.next
        while type(node) is not DummyNode:
            if node == afterNode:
                newNode.next = node.next
                node.next = newNode
                newNode.prev = node
                return
            node = node.next

    def add_in_head(self, newNode):
        newNode.prev = self.dummy_node
        newNode.next = self.dummy_node.next
        self.dummy_node.next.prev = newNode
        self.dummy_node.next = newNode