# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.left = None
#         self.right = None
#
# class BinarySearchTree:
#     def __init__(self):
#         self.root = None
#
#     def insert(self, node, data):
#         if node is None:
#             return Node(data)
#
#         if data < node.data:
#             node.left = self.insert(node.left, data)
#         else:
#             node.right = self.insert(node.right, data)
#
#         return node
#
#     def search(self, node, data):
#         if node is None:
#             return Node
#
#         if data < node.left:
#             return self.search(node.left, data)
#         else:
#             return self.search(node.right, data)
#
#     def delete(self, node, data):
#         if node is None:
#             return Node
#
#         if data < node.data:
#             node.left = self.delete(node.left, data)
#         elif data > node.data:
#             node.right = self.delete(node.right, data)
#         else:
#             if not node.left:
#                 temp = node.right
#                 node = None
#                 return temp
#             elif not node.right:
#                 temp = node.right
#                 node = None
#                 return temp
#
#             node.data = self.min_value_node(node.right).data
#             node.right = self.delete(node.right, node.data)
#             return node
#
#     def min_value_node(self, node):
#         if node is None:
#             return None
#
#         current = node
#         while current.left is not None:
#             current = current.left
#         return current


# class Tree:
#     def __init__(self, data):
#         self.data = data
#         self.left = None
#         self.right = None
#
# class BST:
#     def __init__(self):
#         self.root = None
#
#     def insert(self, node, data):
#         if not self.root:
#             self.root = Tree(data)
#             return node, data
#
#         if node.data < data:
#             node.left = self.insert(node.left, data)
#         else:
#             node.right = self.insert(node.right, data)
#
#         return node
#
#     def search(self, node, data):
#         if not self.root:
#             return None
#
#         if data > node.data:
#             node.right = self.search(node, data)
#         else:
#             node.left = self.search(node, data)
#
#         return node, data
#
#     @staticmethod
#     def minimum(node):
#         if not node:
#             return None
#
#         while node.left is not None:
#             node = node.left
#
#         return node.data
#
#     @staticmethod
#     def maximum(node):
#         if not node:
#             return None
#
#         while node.right is not None:
#             node = node.right
#
#         return node.data
#
#     def delete(self, node, data):
#         if not self.root:
#             return None
#
#         if data < node.data:
#             node.left = self.delete(node.left, data)
#         elif data > node.data:
#             node.right = self.delete(node.right, data)
#         else:
#             if not node.left:
#                 temp = node.right
#                 node = None
#                 return temp
#
#             elif not node.right:
#                 temp = node.left
#                 node = None
#                 return temp
#
#             temp = self.minimum(node.right)
#             node.data = temp.data
#             node.right = self.delete(node.right, temp.data)
#         return node

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.left = None
#         self.right = None
#         self.height = 1
#
# class BinarySearchTree:
#     def get_height(self, node):
#         if not node:
#             return 0
#         return node.height
#
#     def balance_factor(self, node):
#         if not node:
#             return None
#         return self.get_height(node.left) - self.get_height(node.right)
#
#     def insert(self, node, data):
#         if not node:
#             node = Node(data)
#         else:
#             if data < node.data:
#                 node.left = self.insert(node.left, data)
#             else:
#                 node.right = self.insert(node.right, data)
#         return node
#
#
#     def search(self, node, target):
#         if not node:
#             raise ValueError("Empty Tree")
#         elif node.data == target:
#             return node
#         elif target < node.data:
#             return self.search(node.left, target)
#         else:
#             return self.search(node.right, target)
#
#
#     def min_value(self, node):
#         current = node
#         while current and current.left is not None:
#             current = current.left
#         return current
#
#     def max_value(self, node):
#         current = node
#         while current and current.right is not None:
#             current = current.right
#         return current
#
#     def delete(self, node, data):
#         if not node:
#             raise ValueError("Empty Tree")
#         else:
#             if data < node.data:
#                 node.left = self.delete(node.left, data)
#             elif data > node.data:
#                 node.right = self.delete(node.right, data)
#             else:
#                 if not node.left:
#                     temp = node.right
#                     node.right = None
#                     return temp
#
#                 elif not node.right:
#                     temp = node.left
#                     node.left = None
#                     return temp
#
#                 node.data = self.min_value(node.right).data
#                 node.right = self.delete(node.right, node.data)
#
#         return node
#
#
# bst = BinarySearchTree()
# root = None
# root = bst.insert(root, 10)
# root = bst.insert(root, 5)
# root = bst.insert(root, 2)
# root = bst.insert(root, 15)
# root = bst.insert(root, 19)


# class AVL:
#     def get_height(self, node):
#         if not node:
#             return 0
#         return node.height
#
#     def balance_factor(self, node):
#         if not node:
#             return None
#         return self.get_height(node.right) - self.get_height(node.left)
#
#     def left_rotate(self, x):
#         z = x.right
#
#
#     def insert(self, node, data):
#         if not node:
#             raise ValueError("Empty Tree")
#         else:
#             if data < node.data:
#                 node.left = self.insert(node.left, data)
#             elif data > node.data:
#                 node.right = self.insert(node.right, data)
#
#             node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))
#             balance = self.balance_factor(node)
#
#             #Left-Left
#             if balance > 1 and self.balance_factor(node.left) >= 0:
#                 return


# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.left = None
#         self.right = None
#
# class BinarySearchTreeRecursion:
#     def __init__(self):
#         self.root = None
#
#     def insert(self, node, data):
#         if self.root is None:
#             node = Node(data)
#         else:
#             if data < node.data:
#                 node.left = self.insert(node.left, data)
#             else:
#                 node.right = self.insert(node.right, data)
#         return node
#
#     def traversal(self, node):
#         if self.root is None:
#             return
#         print(node.data, end=', ')
#         self.traversal(node.left)
#         self.traversal(node.right)
#
# bst = BinarySearchTreeRecursion()
# bst.insert(10)
# bst.insert(20)
# bst.insert(root, 30)
# print(bst.traversal())


# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.left = None
#         self.right = None
#
# class BST:
#     def __init__(self):
#         self.root = None
#
#     def insert(self, data):
#         self.root = self._insert(self.root, data)
#
#     def _insert(self, node, data):
#         if node is None:
#             return Node(data)
#         if data < node.data:
#             node.left = self._insert(node.left, data)
#         else:
#             node.right = self._insert(node.right, data)
#         return node
#
#     def traversal(self):
#         self.root = self._traversal(self.root)
#
#     def _traversal(self, node):
#         if node is None:
#             return
#         print(node.data, end=', ')
#         self._traversal(node.left)
#         self._traversal(node.right)
#
# bst = BST()
# bst.insert(10)
# bst.insert(5)
# bst.insert(2)
# bst.insert(1)
# bst.insert(18)
# bst.insert(20)
# bst.insert(30)
# bst.traversal()


# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.left = None
#         self.right = None
#
# class BinarySearchTree:
#     def __init__(self):
#         self.root = None
#
#     def traversal(self):
#         pass
#
#     def insert(self, data):
#         new_node = Node(data)
#
#         if self.root is None:
#             self.root = new_node
#             return
#
#         current = self.root
#         while current:
#             if data < current.data:
#                 if current.left is None:
#                     current.left = new_node
#                     return
#                 current = current.left
#             elif data > current.data:
#                 if current.right is None:
#                     current.right = new_node
#                     return
#                 current = current.right
#             else:
#                 return
#
#
#     def search(self, data):
#         if self.root is None:
#             return None
#
#         current = self.root
#         while current:
#             if data == current.data:
#                 return current
#
#             if data < current.data:
#                 current = current.left
#             else:
#                 current = current.right
#
#         return None
#
#     def delete(self, data):
#         pass
#
#
#     def get_min(self):
#         if self.root is None:
#             return None
#
#         current = self.root
#         while current is not None:
#             current = current.left
#
#         return current
#
#     def get_max(self):
#         if self.root is None:
#             return None
#
#         current = self.root
#         while current is not None:
#             current = current.right
#
#         return current


# class BinarySearchTree:
#     class Node:
#         def __init__(self, data):
#             self.data = data
#             self.left = None
#             self.right = None
#
#         def __str__(self):
#             return str(self.data)
#
#     def __init__(self):
#         self.root = None
#
#     def add(self, data):
#         def _add(node, data):
#             if node is None:
#                 return BinarySearchTree.Node(data)
#
#             if data < node.data:
#                 node.left = _add(node.left, data)
#             elif data > node.data:
#                 node.right = _add(node.right, data)
#
#             return node
#         self.root = _add(self.root, data)
#
#     def delete(self, data):
#         def _delete(node, data):
#             if node is None:
#                 return None
#
#             if data < node.data:
#                 node.left = _delete(node.left, data)
#                 return node
#
#             if data > node.data:
#                 node.right = _delete(node.right, data)
#                 return node
#
#             #Leaf
#             if node.left is None and node.right is None:
#                 return None
#
#             #Left child
#             if node.left is not None and node.right is None:
#                 return node.left
#
#             #Right child
#             if node.left is None and node.right is not None:
#                 return node.right
#
#             #Both children
#             successor = node.right
#             while successor.left is not None:
#                 successor = successor.left
#
#             node.data = successor.data
#
#             node.right = _delete(node.right, successor.data)
#
#             return node
#
#         self.root = _delete(self.root, data)
#
#
#     def pre_order(self, node):
#         if node is None:
#             return
#
#         self.pre_order(node.left)
#         print(node.data)
#         self.pre_order(node.right)
#
#         return
#
#     def in_order(self, node):
#         if node is None:
#             return
#
#         print(node.data)
#         self.in_order(node.left)
#         self.in_order(node.right)
#
#         return
#
#     def post_order(self, node):
#         if node is None:
#             return
#
#         self.post_order(node.left)
#         self.post_order(node.right)
#         print(node.data)
#
#         return
#
#     def search(self, data):
#         def _search(node, data):
#             if node is None:
#                 return None
#
#             if data == node.data:
#                 return node
#
#             if data < node.data:
#                 return _search(node.left, data)
#             else:
#                 return _search(node.right, data)
#
#         return _search(self.root, data)

    # def add(self, data):
    #     def _add(node, data):
    #         if node is None:
    #             return BinarySearchTree.Node(data)
    #
    #         if data < node.data:
    #             node.left = _add(node.left, data)
    #
    #         elif data > node.data:
    #             node.right = _add(node.right, data)
    #
    #         return node
    #
    #     self.root = _add(self.root, data)

    # def pre_order(self, node):
    #     if node is None:
    #         return
    #
    #     self.pre_order(node.left)
    #     print(node.data)
    #     self.pre_order(node.right)
    #
    #     return
    #
    #
    # def in_order(self, node):
    #     if node is None:
    #         return
    #
    #     print(node.data)
    #     self.in_order(node.left)
    #     self.in_order(node.right)
    #
    #     return
    #
    # def post_order(self, node):
    #     if node is None:
    #         return
    #
    #     self.post_order(node.left)
    #     self.post_order(node.right)
    #     print(node.data)
    #
    #     return


# bst = BinarySearchTree()
# bst.add(1)
# bst.add(5)
# bst.add(3)
# bst.add(2)
# bst.add(6)
# bst.add(4)
# print(bst.search(3))
# bst.add(-1)


# class BinarySearchTree:
#     class Node:
#         def __init__(self, data):
#             self.data = data
#             self.left = None
#             self.right = None
#
#         def __str__(self):
#             return str(self.data)
#
#     def __init__(self):
#         self.root = None
#
#     def insert(self, data):
#         def _insert(node, data):
#             if node is None:
#                 return BinarySearchTree.Node(data)
#
#             if data < node.data:
#                 node.left = _insert(node.left, data)
#             elif data > node.data:
#                 node.right = _insert(node.right, data)
#             else:
#                 pass
#
#             return node
#
#         self.root = _insert(self.root, data)
#
#
#     def search(self, data):
#         def _search(node, data):
#             if node is None:
#                 return None
#
#             if data == node.data:
#                 return node
#
#             if data < node.data:
#                 return _search(node.left, data)
#             else:
#                 return _search(node.right, data)
#
#         return _search(self.root, data)
#
#
#     def delete(self, data):
#         def _delete(node, data):
#             if node is None:
#                 return None
#
#             print(f"Current node: {node.data}")
#             if data < node.data:
#                 print(f"Current node: {node.data}, his left child: {node.left.data} and right child is None")
#                 node.left = _delete(node.left, data)
#                 return node
#
#             if data > node.data:
#                 print(f"Current node: {node.data}, his left child is: {node if node.left else None} and right child: {node if node.right else None}")
#                 node.right = _delete(node.right, data)
#                 print(f"Current node is still: {node.data}, but he has new right child-node: {node.right.data}")
#                 return node
#
#             #Leaf
#             print(f"Current node: {node.data}, his left child: {node.left if node.left is not None else None} and right child: {node.right if node.right is not None else None}")
#             if node.left is None and node.right is None:
#                 return None
#
#             #Left child
#             if node.left is not None and node.right is None:
#                 print(f"Node which will be returned: {node.left.data}")
#                 return node.left
#
#             #Right child
#             if node.left is None and node.right is not None:
#                 print(f"Node which will be returned from recursive _delete func-call: {node.right.data}")
#                 return node.right
#
#             #Both children
#             successor = node.right
#             print(f"Current successor: {successor.data}")
#             while successor.left is not None:
#                 successor = successor.left #Get down straight to the min node in right sub-tree which will be replaced with node to delete
#
#             print(f"Current node: {node.data}")
#             node.data = successor.data
#
#             print(f"New current node: {node.data} after swap and right child of current node: {node.right.data}")
#             node.right = _delete(node.right, successor.data)
#
#             print(f"Returned node: {node.data} and delete node which was replaced with root: {node.right if node.right is not None else None}")
#             return node
#
#         self.root = _delete(self.root, data)
#         print(f"New current self.root: {self.root.data}")
#
#     def iteration_min_value(self):
#         def _min_value(node):
#             if node is None:
#                 return None
#
#             while node is not None:
#                 node = node.left
#
#             return node
#         return _min_value(self.root)
#
#     def recursion_min_value(self):
#         def _min(node):
#             if node is None:
#                 return None
#
#             if node.left is None:
#                 return node
#
#             return _min(node.left)
#
#         return _min(self.root)
#
#     def iteration_max_value(self):
#         def _max_value(node):
#             if node is None:
#                 return None
#
#             while node.right is not None:
#                 node = node.right
#
#             return node
#         return _max_value(self.root)
#
#     def recursion_max_value(self):
#         def _max_value(node):
#             if node is None:
#                 return None
#
#             if node.right is None:
#                 return node
#
#             return _max_value(node.right)
#
#         return _max_value(self.root)
#
#
#     def pre_order(self, node):
#         if node is None:
#             return
#
#         print(node.data)
#         self.pre_order(node.left)
#         self.pre_order(node.right)
#
#         return
#
#
#     def in_order(self, node):
#         if node is None:
#             return
#
#         self.in_order(node.left)
#         print(node.data)
#         self.in_order(node.right)
#
#         return
#
#     def post_order(self, node):
#         if node is None:
#             return
#
#         self.post_order(node.left)
#         self.post_order(node.right)
#         print(node.data)
#
#         return
#
# bst = BinarySearchTree()
# bst.insert(10)
# bst.insert(13)
# bst.insert(5)
# bst.insert(2)
# bst.insert(4)
# bst.insert(1)
# bst.delete(10)
# print(bst.search(1))
# print(bst.recursion_min_value())
# print(bst.recursion_max_value())


# import unittest
#
# class TestBST(unittest.TestCase):
#
#     def setUp(self):
#         self.bst = BinarySearchTree()
#         for value in [5,3,6,2,4,7]:
#             self.bst.insert(value)
#
#     def test_insert_root(self):
#         tree = BinarySearchTree()
#         tree.insert(10)
#         self.assertIsNotNone(tree.root)
#         self.assertEqual(tree.root.data, 10)
#
#     def test_insert_structure(self):
#         self.assertEqual(self.bst.root.data, 5)
#         self.assertEqual(self.bst.root.left.data, 3)
#         self.assertEqual(self.bst.root.right.data, 6)
#
#     def test_search(self):
#         node = self.bst.search(6)
#         self.assertIsNotNone(node)
#         self.assertEqual(node.data, 6)
#
#     def test_search_missing(self):
#         node = self.bst.search(100)
#         self.assertIsNone(node)
#
#     def test_delete_leaf(self):
#         self.bst.delete(7)
#         result = self.bst.search(7)
#         self.assertIsNone(result)
#
#     def test_delete_node_with_one_child(self):
#         self.bst.delete(6)
#         result = self.bst.search(6)
#         self.assertIsNone(result)
#         self.assertEqual(self.bst.root.right.data, 7)
#
#     def test_delete_node_with_both_children(self):
#         self.bst.delete(5)
#         result = self.bst.search(5)
#         self.assertIsNone(result)
#         self.assertEqual(self.bst.root.data, 6)
#
#     def test_delete_wrong_value(self):
#         self.bst.delete(100)
#
#
# class BinarySearchTree:
#     class Node:
#         def __init__(self, data):
#             self.data = data
#             self.left = None
#             self.right = None
#
#         def __str__(self):
#             return str(self.data)
#
#     def __init__(self):
#         self.root = None
#
#     def insert(self, data):
#         def _insert(node, data):
#             if node is None:
#                 return BinarySearchTree.Node(data)
#
#             if data < node.data:
#                 node.left = _insert(node.left, data)
#                 return node
#             elif data > node.data:
#                 node.right = _insert(node.right, data)
#                 return node
#             else:
#                 return node
#
#         self.root = _insert(self.root, data)
#
#
#     def search(self, data):
#         def _search(node, data):
#             if node is None:
#                 return None
#
#             print(f"Current node: {node.data}")
#             if data == node.data:
#                 return node
#
#             print(f"Left child: {node.left if node.left is not None else None}, right child: {node.right if node.right is not None else None}")
#             if data < node.data:
#                 return _search(node.left, data)
#             else:
#                 print(f"Left child: {node.left if node.left is not None else None}, right child: {node.right if node.right is not None else None}")
#                 return _search(node.right, data)
#
#         return _search(self.root, data)
#
#     def delete(self, data):
#         def _delete(node, data):
#             if node is None:
#                 return None
#
#             print(f"Current node: {node.data}")
#             if data < node.data:
#                 print(f"Left child: {node.left if node.left is not None else None} of current node: {node.data}")
#                 node.left = _delete(node.left, data)
#                 print(f"Current node: {node.data}, and his children now: {node.left if node.left is not None else None}, {node.right if node.right is not None else None}")
#                 return node
#             elif data > node.data:
#                 print(f"Right child: {node.right if node.right is not None else None} of current node: {node.data}")
#                 node.right = _delete(node.right, data)
#                 return node
#
#             #Leaf
#             if node.left is None and node.right is None:
#                 print(f"If current node: {node.data} doesn't have any children: {node.left if node.left is not None else None and node.right if node.right is not None else None} then we return None on current node")
#                 return None
#
#             #Left child
#             if node.left is not None and node.right is None:
#                 return node.left
#
#             #Right child
#             if node.left is None and node.right is not None:
#                 return node.right
#
#             #Both children
#             if node.left and node.right:
#                 successor = node.right
#                 while successor.left is not None:
#                     successor = successor.left
#
#                 node.data = successor.data
#
#                 node.right = _delete(node.right, successor.data)
#
#             return node
#
#         self.root = _delete(self.root, data)
#
#
# bst = BinarySearchTree()
# bst.insert(5)
# bst.insert(2)
# bst.insert(1)
# bst.insert(7)
# bst.insert(4)
# bst.insert(8)
# bst.insert(6)
# bst.search(2)
# bst.delete(5)

class BST:
    class Node:
        def __init__(self, val):
            self.val = val
            self.left = None
            self.right = None

    def __init__(self):
        self.root = None

    def insert(self, node, val):
        if node is None:
            return BST.Node(val)

        if val < node.val:
            node.left = self.insert(node.left, val)
            return node
        elif val > node.val:
            node.right = self.insert(node.right, val)
            return node
        else:
            return node

    def range_sum(self, node, low, high):
        if node is None:
            return 0

        result = 0

        if low <= node.val <= high:
            result += node.val

        print(node.val)
        result += self.range_sum(node.left, low, high)
        result += self.range_sum(node.right, low, high)
        return result

bst = BST()
bst.root = bst.insert(bst.root, 10)
bst.root = bst.insert(bst.root, 5)
bst.root = bst.insert(bst.root, 15)
bst.root = bst.insert(bst.root, 3)
bst.root = bst.insert(bst.root, 7)
bst.root = bst.insert(bst.root, 18)
print('Summa:', bst.range_sum(bst.root, 7, 15))