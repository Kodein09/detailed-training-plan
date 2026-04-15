class BinarySearchTree:
    class Node:
        def __init__(self, value):
            self.value = value
            self.left = None
            self.right = None

    def __init__(self):
        self.root = None

    def insert(self, node, value):
        if not node:
            return BinarySearchTree.Node(value)

        if value < node.value:
            node.left = self.insert(node.left, value)
        elif value > node.value:
            node.right = self.insert(node.right, value)

        return node

    def search(self, node, value):
        if node is None:
            return None

        if value < node.value:
            return self.search(node.left, value)
        elif value > node.value:
            return self.search(node.right, value)
        else:
            return node


    def delete(self, node, value):
        if node is None:
            return None

        if value < node.value:
            node.left = self.delete(node.left, value)
        elif value > node.value:
            node.right = self.delete(node.right, value)
        else:
            if node.left is None:
                return node.right
            if node.right is None:
                return node.left

            successor = node.right
            while successor.left is not None:
                successor = successor.left
            node.value = successor.value
            node.right = self.delete(node.right, successor.value)

        return node

    def min_node(self, node):
        if node is None:
            return None

        self.min_node(node.left)
        return node

    def max_node(self, node):
        if node is None:
            return None

        self.max_node(node.right)
        return node

    def serialize(self, node):
        if not node:
            return None

        return (str(node.data) + ', ' +
                self.serialize(node.left) + ', ' +
                self.serialize(node.right))

    def deserialize(self, data):
        value = iter(data.split(', '))
        def build():
            val = next(value)
            if val == 'None':
                return None

            node = BinarySearchTree.Node(int(val))
            node.left = build()
            node.right = build()
            return node

        self.root = build()

    # def delete(self, node, value):
    #     if node is None:
    #        return None
    #
    #     if value < node.value:
    #         node.left = self.delete(node.left, value)
    #     elif value > node.value:
    #         node.right = self.delete(node.right, value)
    #     else:
    #         if not node.left and not node.right:
    #             return None
    #
    #         elif node.left and not node.right:
    #             return node.left
    #
    #         elif not node.left and node.right:
    #             return node.right
    #
    #         else:
    #             successor = node.right
    #             while successor.left is not None:
    #                 successor = successor.left
    #
    #             node.value = successor.value
    #
    #             node.right = self.delete(node.right, successor.value)
    #
    #         return node

    def pre_order(self, node):
        if not node:
            raise ValueError("Empty Binary Search Tree")

        print(node.value)
        self.pre_order(node.left)
        self.pre_order(node.right)

    def in_order(self, node):
        if not node:
            raise ValueError("Empty Binary Search Tree")

        self.in_order(node.left)
        print(node.value)
        self.in_order(node.right)

    def post_order(self, node):
        if not node:
            raise ValueError("Empty Binary Search Tree")

        self.post_order(node.left)
        self.post_order(node.right)
        print(node.value)

import unittest

class TestBinarySearchTree(unittest.TestCase):
    def setUp(self):
        self.bst = BinarySearchTree()

    def test_insert(self):
        root = self.bst.insert(self.bst.root, 10)
        left = self.bst.insert(self.bst.root, 8)
        right = self.bst.insert(self.bst.root, 12)
        self.assertEqual(root.value, 10)
        self.assertEqual(left.value, 8)
        self.assertEqual(right.value, 12)

    def test_search(self):
        self.bst.root = self.bst.insert(self.bst.root,10)
        self.bst.root = self.bst.insert(self.bst.root, 20)
        self.bst.root = self.bst.insert(self.bst.root, 30)
        result = self.bst.search(self.bst.root, 30)
        self.assertEqual(result.value, 30)
        #Non-existing value
        result = self.bst.search(self.bst.root, 100)
        self.assertIsNone(result)

    def test_delete(self):
        for n in [10, 15, 5, 2, 3, 25, 12]:
            self.bst.root = self.bst.insert(self.bst.root, n)

        #delete root
        self.bst.root = self.bst.delete(self.bst.root, 10)
        self.assertEqual(self.bst.root.value, 12)

        #left child
        self.bst.root = self.bst.insert(self.bst.root, 20)
        self.bst.root = self.bst.delete(self.bst.root, 25)
        self.assertEqual(self.bst.root.right.right.value, 20)

        #right child
        self.bst.root = self.bst.delete(self.bst.root, 15)
        self.assertEqual(self.bst.root.right.value, 20)

        #delete node without children
        self.bst.root = self.bst.delete(self.bst.root, 20)
        self.assertIsNone(self.bst.root.right)