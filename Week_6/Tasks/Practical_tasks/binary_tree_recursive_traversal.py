from collections import deque

class Tree:
    class Node:
        def __init__(self, data):
            self.data = data
            self.left = None
            self.right = None

    def __init__(self):
        self.root = None

    #Insert and Breadth-First-Search
    def insert_bfs(self, value):
        new_node = Tree.Node(value)
        if not self.root:
            self.root = new_node
            return

        queue = deque([self.root])
        while queue:
            node = queue.popleft()
            if not node.left:
                node.left = new_node
                return
            else:
                queue.append(node.left)

            if not node.right:
                node.right = new_node
                return
            else:
                queue.append(node.right)

    #Search via Depth-First-Search
    def search_dfs(self, node, value):
        if not node:
            return False

        if node.data == value:
            return True

        return (
            self.search_dfs(node.left, value) or
            self.search_dfs(node.right, value)
        )

    def dfs(self, node, order='pre'):
        if not node:
            return

        if order == 'pre':
            print(node.data)
        self.dfs(node.left, order)
        if order == 'in':
            print(node.data)
        self.dfs(node.right, order)
        if order == 'post':
            print(node.data)

    def serialize(self, node):
        if not node:
            return 'None'

        return (
            str(node.data) + ',' +
            self.serialize(node.left) + ',' +
            self.serialize(node.right)
        )

    def deserialize(self, data):
        value = iter(data.split(','))

        def build():
            val = next(value)
            if val == 'None':
                return None

            node = Tree.Node(int(val))
            node.left = build()
            node.right = build()
            return node

        self.root = build()

    # #Traversal-Depth-First-Search
    # def traversal_dfs(self, node):
    #     if not node:
    #         return
    #
    #     print(node.data)
    #     self.traversal_dfs(node.left)
    #     self.traversal_dfs(node.right)

    # #NLR
    # def pre_order(self, node):
    #     print(node.data)
    #     self.pre_order(node.left)
    #     self.pre_order(node.right)
    #
    # #LNR
    # def in_order(self, node):
    #     self.in_order(node.left)
    #     print(node.data)
    #     self.in_order(node.right)
    #
    # #LRN
    # def post_order(self, node):
    #     self.post_order(node.left)
    #     self.post_order(node.right)
    #     print(node.data)

    # def insert_bfs(self, value):
    #     new_node = Tree.Node(value)
    #     if not self.root:
    #         self.root = new_node
    #         return
    #
    #     self.search_bfs(new_node)
    #
    # #BFS (Breadth-First-Search) - обход в ширину для поиска первого пустого места для вставки новой ноды
    # def search_bfs(self, new_node):
    #     queue = deque([self.root])
    #     while queue:
    #         node = queue.popleft()
    #
    #         if not node.left:
    #             node.left= new_node
    #         else:
    #             queue.append(node.left)
    #
    #         if not node.right:
    #             node.right = new_node
    #         else:
    #             queue.append(node.right)

    # def insert_dfs(self, value):
    #     if not self.root:
    #         self.root = Tree.Node(value)
    #         return self.root
    #
    #     return self.search_dfs(self.root, value)
    #
    # #DFS
    # def search_dfs(self, node, new_node):
    #     if not node.left:
    #         node.left = new_node
    #     else:
    #         self.search_dfs(node.left, new_node)
    #
    #     if not node.right:
    #         node.right = new_node
    #     else:
    #         self.search_dfs(node.right, new_node)

import unittest

class TestBinaryTree(unittest.TestCase):
    def setUp(self):
        self.bt = Tree()

    def test_insert(self):
        self.bt.insert_bfs(10)
        self.bt.insert_bfs(20)
        self.assertEqual(self.bt.root.data, 10)
        self.assertEqual(self.bt.root.left.data, 20)

    def test_search_dfs(self):
        self.bt.insert_bfs(10)
        self.bt.insert_bfs(20)
        self.bt.insert_bfs(30)
        result = self.bt.search_dfs(self.bt.root, 30)
        self.assertEqual(result, True)
        error = self.bt.search_dfs(self.bt.root, 100)
        self.assertIs(error, False)

    def test_traversal_dfs(self):
        self.bt.insert_bfs(1)
        self.bt.insert_bfs(2)
        self.bt.insert_bfs(3)
        self.bt.insert_bfs(4)
        self.assertEqual(self.bt.dfs(self.bt.root, 'pre'), None)
        self.assertEqual(self.bt.dfs(self.bt.root, 'in'), None)
        self.assertEqual(self.bt.dfs(self.bt.root, 'post'), None)

tree = Tree()
tree.insert_bfs(10)
tree.insert_bfs(20)
tree.insert_bfs(30)
print('Result:', tree.search_dfs(tree.root, 30))