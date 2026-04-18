class Node:
    def __init__(self, data: int) -> None:
        self.data = data
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    def __init__(self) -> None:
        self.root = None

    def balance_factor(self, node: Node):
        return self.get_height(node.left) - self.get_height(node.right)

    def update_height(self, node: Node) -> None:
        if node is None:
            return
        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))

    def get_height(self, node: Node) -> int:
        if node is None:
            return 0
        return node.height

    def insert(self, node: Node, value: int) -> Node:
        if node is None:
            return Node(value)

        if value < node.data:
            node.left = self.insert(node.left, value)
        elif value > node.data:
            node.right = self.insert(node.right, value)
        else:
            return node

        self.update_height(node)
        balance = self.balance_factor(node)

        #LL
        if balance > 1 and self.balance_factor(node.left) >= 0:
            return self.right_rotate(node)

        #LR
        if balance > 1 and self.balance_factor(node.left) < 0:
            return self.left_right(node)

        #RR
        if balance < -1 and self.balance_factor(node.right) <= 0:
            return self.left_rotate(node)

        #RL
        if balance < -1 and self.balance_factor(node.right) > 0:
            return self.right_left(node)

        return node

    def search(self, node: Node, value: int) -> Node | None:
        if node is None:
            return None

        if value == node.data:
            return node

        if value < node.data:
            return self.search(node.left, value)
        elif value > node.data:
            return self.search(node.right, value)
        return None

    def delete(self, node: Node, value: int) -> Node | None:
        if node is None:
            return None

        if value < node.data:
            node.left = self.delete(node.left, value)
        elif value > node.data:
            node.right = self.delete(node.right, value)
        else:
            if node.left is None:
                return node.right
            if node.right is None:
                return node.left

            successor = node.right
            while successor.left is not None:
                successor = successor.left
            node.data = successor.data
            node.right = self.delete(node.right, successor.data)

        self.update_height(node)
        balance = self.balance_factor(node)

        #LL
        if balance > 1 and self.balance_factor(node.left) >= 0:
            return self.right_rotate(node)

        #RR
        if balance < -1 and self.balance_factor(node.right) <= 0:
            return self.left_rotate(node)

        #LR
        if balance > 1 and self.balance_factor(node.left) < 0:
            return self.left_right(node)

        #RL
        if balance < -1 and self.balance_factor(node.right) > 0:
            return self.right_left(node)

        return node

    def left_rotate(self, node: Node) -> Node:
        new_root = node.right
        temp = new_root.left

        new_root.left = node
        node.right = temp

        self.update_height(node)
        self.update_height(new_root)

        return new_root

    def right_rotate(self, node: Node) -> Node:
        new_root = node.left
        temp = new_root.right

        new_root.right = node
        node.left = temp

        self.update_height(node)
        self.update_height(new_root)

        return new_root

    def left_right(self, node: Node) -> Node:
        node.left = self.left_rotate(node.left)
        return self.right_rotate(node)

    def right_left(self, node: Node) -> Node:
        node.right = self.right_rotate(node.right)
        return self.left_rotate(node)

import unittest

class TestAVLTree(unittest.TestCase):
    def setUp(self):
        self.avl = AVLTree()

    def test_insert(self):
        self.avl.root = self.avl.insert(self.avl.root, 10)
        self.avl.root = self.avl.insert(self.avl.root, 20)
        self.avl.root = self.avl.insert(self.avl.root, 8)
        self.assertEqual(self.avl.root.data, 10)
        self.assertEqual(self.avl.root.left.data, 8)
        self.assertEqual(self.avl.root.right.data, 20)

    def test_search(self):
        self.avl.root = self.avl.insert(self.avl.root, 100)
        self.avl.root = self.avl.insert(self.avl.root, 200)
        self.avl.root = self.avl.insert(self.avl.root, 50)
        self.avl.root = self.avl.insert(self.avl.root, 25)

        search = self.avl.search(self.avl.root, 25)
        self.assertEqual(search.data, 25)

        error_search = self.avl.search(self.avl.root, 1)
        self.assertIsNone(error_search)

    def test_delete(self):
        self.avl.root = self.avl.insert(self.avl.root, 10)
        self.avl.root = self.avl.insert(self.avl.root, 6)
        self.avl.root = self.avl.insert(self.avl.root, 18)
        self.avl.root = self.avl.insert(self.avl.root, 3)

        self.avl.root = self.avl.delete(self.avl.root, 3)
        self.assertIsNone(self.avl.root.left.left)

    def test_left_rotate(self):
        self.avl.root = self.avl.insert(self.avl.root, 1)
        self.avl.root = self.avl.insert(self.avl.root, 2)
        self.avl.root = self.avl.insert(self.avl.root, 3)

        self.assertEqual(self.avl.root.data, 2)
        self.assertEqual(self.avl.root.left.data, 1)
        self.assertEqual(self.avl.root.right.data, 3)

    def test_right_rotate(self):
        self.avl.root = self.avl.insert(self.avl.root, 3)
        self.avl.root = self.avl.insert(self.avl.root, 2)
        self.avl.root = self.avl.insert(self.avl.root, 1)

        self.assertEqual(self.avl.root.data, 2)
        self.assertEqual(self.avl.root.left.data, 1)
        self.assertEqual(self.avl.root.right.data, 3)

    def test_left_right(self):
        self.avl.root = self.avl.insert(self.avl.root, 10)
        self.avl.root = self.avl.insert(self.avl.root, 5)
        self.avl.root = self.avl.insert(self.avl.root, 7)

        self.assertEqual(self.avl.root.data, 7)
        self.assertEqual(self.avl.root.left.data, 5)
        self.assertEqual(self.avl.root.right.data, 10)

    def test_right_left(self):
        self.avl.root = self.avl.insert(self.avl.root, 10)
        self.avl.root = self.avl.insert(self.avl.root, 20)
        self.avl.root = self.avl.insert(self.avl.root, 15)

        self.assertEqual(self.avl.root.data, 15)
        self.assertEqual(self.avl.root.left.data, 10)
        self.assertEqual(self.avl.root.right.data, 20)