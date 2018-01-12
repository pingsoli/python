# List

class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, head=None):
        self.head = head

    # Add an element in the tail of linked list
    def add_tail(self, node):
        head = self.head
        prev = None
        while head:
            prev = head
            head = head.next

        # Empty linked list
        if not prev:
            self.head = node
        else:
            prev.next = node

    # Add an element in the head of linked list
    def add(self, node):
        if not self.head:
            self.head = node
        else:
            node.next = self.head
            self.head = node

    def search(self, value):
        head = self.head
        while head:
            if head.value == value:
                return head
            head = head.next
        return None

    def reverse(self):
        prev = None
        head = self.head
        while head:
            temp = head.next
            head.next = prev
            prev = head
            head = temp
        self.head = prev

    def remove(self, value):
        # If delete head
        if self.head.value == value:
            tmp = self.head
            self.head = self.head.next
            del tmp
            return True

        prv = self.head
        nxt = self.head.next
        while nxt:
            if nxt.value == value:
                prv.next = nxt.next
                del nxt
                return True
            prv = nxt
            nxt = nxt.next
        return False

    def traverse(self):
        next_node = self.head
        while next_node:
            print('{} -> '.format(next_node.value), end='')
            next_node = next_node.next
        print('None')

#n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)
l = LinkedList()
#l.add(n1)
l.add(n2)
l.add(n3)

# l.traverse()
# l.reverse()
# l.traverse()

if l.remove(4):
    l.traverse()
else:
    print('Not Found element')
