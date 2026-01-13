class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class MergeTwoSortedList:
    def __init__(self):
        self.head = None

    def merge_two_lists(self, list1, list2):
        dummy = Node(0)
        tail = dummy

        while list1 and list2:
            if list1.data < list2.data:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2

        return dummy.next