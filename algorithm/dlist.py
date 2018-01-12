# DLinked List

class DListNode:
    def __init__(self, val):
        self.value = val
        self.prev = self.next = None

class DLinkList:
    def __init__(self):
        self.head = None

    def add(self, value):
        node = DListNode(value)
        if not self.head:
            self.head = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node

    def search(self, value):
        curr = self.head
        while curr:
            if curr.value == value:
                return curr
            curr = curr.next
        return None

    def remove(self, value):
        node = search(self, value)

        # Not found the element
        if not node:
            return False

        if node == self.head:


    def traverse(self):
        nxt = self.head
        while nxt:
            print('{} -> '.format(nxt.value), end='')
            nxt = nxt.next
        print('None')

dl = DLinkList()
dl.add(1)
dl.add(2)
dl.add(3)
dl.traverse()
