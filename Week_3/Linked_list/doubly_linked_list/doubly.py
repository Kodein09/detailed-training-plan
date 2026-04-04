class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, data, pos):
        if not self.head:
            new_node = Node(data)
            self.head = new_node
            self.tail = new_node
        elif pos == 0:
            self.insert_at_beginning(data)
        else:
            new_node = Node(data)
            current = self.head
            while current and pos:
                current = current.next
                pos -= 1
            new_node.next = current
            new_node.prev = current.prev
            if current.prev:
                current.prev.next = new_node
            current.prev = new_node

    def insert_at_beginning(self, data):
        if not self.head:
            new_node = Node(data)
            self.head = new_node
            self.tail = new_node
        else:
            new_node = Node(data)
            new_node.next = self.head
            self.head.prev = new_node
            new_node.prev = None
            self.head = new_node

    def insert_at_end(self, data):
        if not self.head:
            new_node = Node(data)
            self.head = new_node
            self.tail = new_node
        else:
            new_node = Node(data)
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def search(self, data):
        if not self.head:
            raise ValueError("Searching while Doubly Linked-List is Empty!")
        else:
            current = self.head
            while current:
                if current.data == data:
                    return f"Search completed successfully: {current.data}"
                else:
                    current = current.next
        return None

    def delete(self, pos):
        if not self.head:
            raise ValueError("Deleting from Empty Doubly Linked-List")
        else:
            current = self.head
            count = 0
            while current and pos:
                current = current.next
                count += 1
                if count == pos:
                    break

            if self.head == self.tail:
                self.head = None
                self.tail = None
                return
            elif pos == 0:
                self.head = self.head.next
                self.head.prev = None
                return
            elif current.next is None:
                self.tail = self.tail.prev
                self.tail.next = None
            else:
                current.prev.next = current.next
                current.next.prev = current.prev
                current.next = None
                current.prev = None

    def delete_first(self):
        if not self.head:
            raise ValueError("Doubly Linked-List is Empty!")
        else:
            if self.head == self.tail:
                self.head = None
                self.tail = None
                return
        self.head = self.head.next
        self.head.prev = None

    def delete_last(self):
        if not self.head:
            raise ValueError("Doubly Linked-List is Empty!")
        else:
            if self.head == self.tail:
                self.head = None
                self.tail = None
                return
        self.tail = self.tail.prev
        self.tail.next = None

    def traversal(self):
        print("Forward:")
        current = self.head
        tail = None
        while current:
            print(current.data, end='->')
            tail = current
            current = current.next

        print("\n\nBackward:")
        while tail:
            print(tail.data, end='<-')
            tail = tail.prev

doubly = DoublyLinkedList()
doubly.insert_at_beginning(5)
doubly.insert_at_beginning(12)
doubly.insert_at_end(100)
doubly.insert_at_end(200)
doubly.insert_at_end(87689)
doubly.insert(18, 2)

print(doubly.traversal(), end='\n\n')
# print(doubly.search(100), end='\n\n')
doubly.delete(2)
print(doubly.traversal())

