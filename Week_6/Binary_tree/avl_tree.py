# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.left = None
#         self.right = None
#         self.height = 1
#
# class AVLTree:
#     def __init__(self):
#         self.root = None
#
#     def get_height(self, node):
#         if not node:
#             return 0
#
#         return node.height
#
#     def get_balance(self, node):
#         if not node:
#             return 0
#
#         return self.get_height(node.left) - self.get_height(node.right)
#
#     def right_rotate(self, y):
#         print(f"Rotate right on node: {y.data}")
#         x = y.left
#         T2 = x.right
#         x.right = y
#         y.left = T2
#         y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
#         x.height = 1 + max(self.get_height(x.left), self.get_height(x.right))
#         return x
#
#     def left_rotate(self, x):
#         print(f"")
#         y = x.left
#         T2 = y.right
#         y.left = x
#         x.right = T2
#         x.height = 1 + max(self.get_height(x.left), self.get_height(x.right))
#         y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
#         return y
#
#     def insert(self, node, data):
#         if not node:
#             return Node(data)
#
#         if data < node.data:
#             node.left = self.insert(node.left, data)
#         elif data > node.data:
#             node.right = self.insert(node.right, data)
#
#         node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))
#         balance = self.get_balance(node)
#
#         #Left-Left
#         if balance > 1 and self.get_balance(node.left) >= 0:
#             return self.right_rotate(node)
#
#         #Right-Right
#         if balance < -1 and self.get_balance(node.right) <= 0:
#             return self.left_rotate(node)
#
#         #Left-Right
#         if balance > 1 and self.get_balance(node.left) < 0:
#             node.left = self.left_rotate(node.left)
#             return self.right_rotate(node)
#
#         #Right-Left
#
# class TreeNode:
#     def __init__(self, data):
#         self.data = data
#         self.left = None
#         self.right = None
#         self.height = 1
#
# class AVLTree:
#     def get_height_node(self, node):
#         if not node:
#             return 0
#         return node.height
#
#     def get_balance(self, node):
#         if not node:
#             return 0
#         return self.get_height_node(node.left) - self.get_height_node(node.right)
#
#     def right_rotate(self, node):
#         x = node.left
#         T2 = x.right
#         x.right = node
#         node.left = T2
#         x.height = 1 + max(self.get_height_node(x.left), self.get_height_node(x.right))
#         node.height = 1 + max(self.get_height_node(node.left), self.get_height_node(node.right))
#         return x
#
#     def left_rotate(self, node):
#         y = node.right
#         T1 = y.left
#         y.left = node
#         node.right = T1
#         node.height = 1 + max(self.get_height_node(node.left), self.get_height_node(node.right))
#         y.height = 1 + max(self.get_height_node(y.left), self.get_height_node(y.right))
#         return y
#
#     def insert(self, node, data):
#         if not node:
#             return TreeNode(data)
#
#         if data < node.data:
#             node.left = self.insert(node.left, data)
#         elif data > node.data:
#             node.right = self.insert(node.right, data)
#
#         #Update the balance factor and balance the tree
#         node.height = 1 + max(self.get_height_node(node.left), self.get_height_node(node.right))
#         balance = self.get_balance(node)
#
#         #Balance the tree
#         #Left Left
#         if balance > 1 and self.get_balance(node.left) >= 0:
#             return self.right_rotate(node)
#
#         #Left Right
#         if balance > 1 and self.get_balance(node.left) < 0:
#             node.left = self.left_rotate(node.left)
#             return self.right_rotate(node)
#
#         #Right Right
#         if balance < -1 and self.get_balance(node.right) <= 0:
#             return self.left_rotate(node)
#
#         #Right Left
#         if balance < -1 and self.get_balance(node.right) > 0:
#             node.right = self.right_rotate(node.right)
#             return self.left_rotate(node)
#
#         return node
#
#     def in_order_traversal(self, node):
#         if not node:
#             return
#
#         self.in_order_traversal(node.left)
#         print(node.data, end=', ')
#         self.in_order_traversal(node.right)
#
# avl_tree = AVLTree()
# root = None
# letters = ['C', 'B', 'E', 'A', 'D', 'H', 'G', 'F']
# for letter in letters:
#     root = avl_tree.insert(root, letter)


# class AVLTree:
#     class Node:
#         def __init__(self, data):
#             self.data = data
#             self.left = None
#             self.right = None
#             self.height = 1
#
#         def __str__(self):
#             return str(self.data)
#
#     def __init__(self):
#         self.root = None
#
#     def get_height(self, node):
#         if node is None:
#             return 0
#         return node.height
#
#     def balance_factor(self, node):
#         if node is None:
#             return 0
#         return self.get_height(node.left) - self.get_height(node.right)
#
#     def update_height(self, node):
#         node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))
#
#     def insert(self, data):
#         def _insert(node, data):
#             if node is None:
#                 return AVLTree.Node(data)
#
#             elif data < node.data:
#                 node.left = _insert(node.left, data)
#             else:
#                 node.right = _insert(node.right, data)
#
#             self.update_height(node)
#             balance = self.balance_factor(node)
#
#             #LL
#             if balance > 1 and self.balance_factor(node.left) >= 0:
#                 return self.left_left(node)
#
#             #RR
#             if balance < -1 and self.balance_factor(node.right) <= 0:
#                 return self.right_right(node)
#
#             #LR
#             if balance > 1 and self.balance_factor(node.left) < 0:
#                 return self.left_right(node)
#             #RL
#             if balance < -1 and self.balance_factor(node.right) > 0:
#                 return self.right_left(node)
#
#             return node
#         self.root = _insert(self.root, data)
#
#     def delete(self, data):
#         def _delete(node, data):
#             if node is None:
#                 return None
#
#             if data < node.data:
#                 node.left = _delete(node.left, data)
#             elif data > node.data:
#                 node.right = _delete(node.right, data)
#             else:
#                 if not node.left and not node.right:
#                     return None
#
#                 if node.left and not node.right:
#                     return node.left
#
#                 if not node.left and node.right:
#                     return node.right
#
#                 if node.left and node.right:
#                     successor = node.right
#                     while successor.left is not None:
#                         successor = successor.left
#
#                     node.data = successor.data
#
#                     node.right = _delete(node.right, successor.data)
#
#                 self.update_height(node)
#                 balance = self.balance_factor(node)
#
#                 if balance > 1 and self.balance_factor(node.left) >= 0:
#                     return self.right_right(node)
#
#                 if balance < -1 and self.balance_factor(node.right) <= 0:
#                     return self.left_left(node)
#
#                 if balance > 1 and self.balance_factor(node.left) < 0:
#                     node.left = self.right_right(node.left)
#                     return self.left_left(node)
#
#                 if balance < -1 and self.balance_factor(node.right) > 0:
#                     node.right = self.left_left(node.right)
#                     return self.right_right(node)
#
#                 return node
#         self.root = _delete(self.root, data)
#
#     def left_left(self, node):
#         node_left = node.left #B
#         temp = node_left.right #X
#
#         node_left.right = node #B.right = A
#         node.left = temp #A.left = X
#
#         self.update_height(node)
#         self.update_height(node_left)
#
#         return node_left
#
#     def right_right(self, node):
#         new_root = node.right #B
#         temp = new_root.left #X (Usually None if RR)
#
#         new_root.left = node #B.left = A
#         node.right = temp #A.right = X
#
#         self.update_height(node)
#         self.update_height(new_root)
#
#         return new_root
#
#     def left_right(self, node):
#         node.left = self.right_right(node.left)
#
#         return self.left_left(node)
#
#
#     def right_left(self, node):
#         node.right = self.left_left(node.right)
#
#         return self.right_right(node)
#
#     def pre_order(self, node, result=None):
#         if result is None:
#             result = []
#
#         if node is None:
#             return result
#
#         result.append(node.data)
#         self.pre_order(node.left, result)
#         self.pre_order(node.right, result)
#
#         return result
#
#     def inorder_traversal(self, node, result=None):
#         if result is None:
#             result = []
#
#         if node is None:
#             return result
#
#         self.inorder_traversal(node.left, result)
#         result.append(node.data)
#         self.inorder_traversal(node.right, result)
#
#         return result
#
#     def post_order(self, node, result=None):
#         if result is None:
#             result = []
#
#         if node is None:
#             return result
#
#         self.post_order(node.left, result)
#         self.post_order(node.right, result)
#         result.append(node.data)
#
#         return result
#
# import unittest
#
# class TestAVLTree(unittest.TestCase):
#     def setUp(self):
#         self.avl = AVLTree()
#
#     def test_height(self):
#         self.avl.insert(10)
#         self.avl.insert(5)
#         self.avl.insert(3)
#         print(self.avl.root.data)
#         self.avl.get_height(self.avl.root)
#         actual_height = self.avl.get_height(self.avl.root)
#         self.assertEqual(actual_height, 2)
#         self.assertEqual(self.avl.root.data, 5)
#         self.assertIsNotNone(self.avl.root)
#
#     def test_balance_factor(self):
#         balance = self.avl.balance_factor(self.avl.root)
#         self.assertIsNotNone(balance)
#         self.assertEqual(balance, 0)
#
#     def test_insert(self):
#         self.avl.insert(100)
#         self.assertEqual(self.avl.root.data, 100)
#         self.assertIsNotNone(self.avl.root)
#
#     def test_pre_order(self):
#         self.avl.insert(30)
#         self.avl.insert(20)
#         self.avl.insert(10)
#
#         actual_order = self.avl.pre_order(self.avl.root)
#
#         expected_order = [20, 10, 30]
#         self.assertEqual(actual_order, expected_order)
#
#     def test_in_order(self):
#         self.avl.insert(29)
#         self.avl.insert(25)
#         self.avl.insert(64)
#
#         actual_order = self.avl.inorder_traversal(self.avl.root)
#
#         expected_order = [25, 29, 64]
#         self.assertEqual(actual_order, expected_order)
#
#     def test_post_order(self):
#         self.avl.insert(10)
#         self.avl.insert(20)
#         self.avl.insert(30)
#
#         actual_order = self.avl.post_order(self.avl.root)
#         expected_order = [10, 30, 20]
#         self.assertEqual(actual_order, expected_order)
#
#     def test_delete(self):
#         self.avl.insert(10)
#         self.assertIsNotNone(self.avl.root)
#         self.avl.delete(10)
#         self.assertIsNone(self.avl.root)
#
#     def test_delete_leaf(self):
#         self.avl.insert(20)
#         self.avl.insert(30)
#         self.avl.delete(30)
#         self.assertEqual(self.avl.root.right, None)
#         self.assertIsNone(self.avl.root.right)
#
#     def test_delete_with_one_child(self):
#         pass
#
#     def test_delete_with_both_children(self):
#         pass

    # def balance_factor(self, node):
    #     if node is None:
    #         return 0
    #     return self.get_height(node.left) - self.get_height(node.right)
    #
    # def update_height(self, node):
    #     node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))

    # def left_left(self, node):
    #     node_left = node.left
    #     temp = node_left.right
    #
    #     node_left.right = node
    #     node.left = temp
    #
    #     return node_left
    #
    # def right_right(self, node):
    #     node_right = node.right
    #     temp_left_subtree_of_node_right = node_right.left
    #
    #     node_right.left = node
    #     node.right = temp_left_subtree_of_node_right
    #
    #     return node_right


    # def left_left(self, node):
    #     node_left = node.left
    #     temp = node_left.right
    #
    #     node_left.right = node
    #     node.left = temp
    #
    # def right_right(self, node):
    #     node_right = node.right
    #     temp = node_right.left
    #
    #     node_right.left = node
    #     node.right = temp

    # def right_right(self, node):
    #     right_child = node.right
    #     temp = right_child.left
    #
    #     right_child.left = node
    #     node.right = temp
    #
    #     self.update_height(node)
    #     self.update_height(right_child)
    #
    #     return right_child
    #
    # def left_left(self, node):
    #     left_child = node.left
    #     temp = left_child.left
    #
    #     left_child.left = node
    #     node.right = temp
    #
    #     self.update_height(node)
    #     self.update_height(left_child)
    #
    #     return left_child

# class AVLTree:
#     class Node:
#         def __init__(self, data):
#             self.data = data
#             self.left = None
#             self.right = None
#             self.height = 1
#
#         def __str__(self):
#             return str(self.data)
#
#     def __init__(self):
#         self.root = None
#
#     def get_height(self, node):
#         if node is None:
#             return 0
#
#         return node.height
#
#     def balance_factor(self, node):
#         return self.get_height(node.left), self.get_height(node.right)
#
#     def update_height(self, node):
#         node.height = 1 + max(self.get_height(node.left) - self.get_height(node.right))
#
#     def insert(self, data):
#         def _insert(node, data):
#             if node is None:
#                 return AVLTree.Node(data)
#
#             if data < node.data:
#                 node.left = _insert(node.left, data)
#             elif data > node.data:
#                 node.right = _insert(node.right, data)
#
#             self.update_height(node)
#             balance = self.balance_factor(node)
#
#             #LL
#             if balance > 1 and self.balance_factor(node.left) >= 0:
#                 return self.left_left(node)
#
#             #RR
#             if balance < -1 and self.balance_factor(node.right) <= 0:
#                 return self.right_right(node)
#
#             #LR
#             if balance > 1 and self.balance_factor(node.left) < 0:
#                 return self.left_right(node)
#
#             #RL
#             if balance < -1 and self.balance_factor(node.right) > 0:
#                 return self.right_left(node)
#
#             return node
#
#         self.root = _insert(self.root, data)
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
#     def delete(self, data):
#         def _delete(node, data):
#             if node is None:
#                 return None
#
#             if data < node.data:
#                 node.left = _delete(node.left, data)
#             elif data > node.data:
#                 node.right = _delete(node.right, data)
#             else:
#                 if not node.left and not node.right:
#                     return None
#
#                 if node.left and not node.right:
#                     return node.left
#
#                 if not node.left and node.right:
#                     return node.right
#
#                 if node.left and node.right:
#                     successor = node.right
#                     while successor.left is not None:
#                         successor = successor.left
#
#                     node.data = successor.data
#
#                     node.right = _delete(node.right, successor.data)
#
#             if node is None:
#                 return node
#
#             self.update_height(node)
#             balance = self.balance_factor(node)
#
#             if balance > 1 and self.balance_factor(node.left) >= 0:
#                 return self.left_left(node)
#
#             if balance < -1 and self.balance_factor(node.right) <= 0:
#                 return self.right_right(node)
#
#             if balance > 1 and self.balance_factor(node.left) < 0:
#                 return self.left_right(node)
#
#             if balance < -1 and self.balance_factor(node.right) > 0:
#                 return self.right_left(node)
#
#             return node
#
#         self.root = _delete(self.root, data)
#
#     def left_left(self, node):
#         new_root = node.left
#         temp = new_root.right
#
#         new_root.right = node
#         node.left = temp
#
#         self.update_height(node)
#         self.update_height(new_root)
#
#         return new_root
#
#     #RR
#     def right_right(self, node):
#         new_root = node.right
#         temp = new_root.left
#
#         new_root.left = node
#         node.right = temp
#
#         self.update_height(node)
#         self.update_height(new_root)
#
#         return new_root
#
#     #LR
#     def left_right(self, node):
#         node.left = self.right_right(node.left)
#         return self.left_left(node)
#
#     #RL
#     def right_left(self, node):
#         node.right = self.left_left(node.right)
#         return self.right_right(node)


class AVLTree:
    class Node:
        def __init__(self, data):
            self.data = data
            self.left = None
            self.right = None
            self.height = 1

        def __str__(self):
            return str(self.data)

    def __init__(self):
        self.root = None

    def get_height(self, node):
        if node is None:
            return 0

        return node.height

    def balance_factor(self, node):
        return self.get_height(node.left) - self.get_height(node.right)

    def update_height(self, node):
        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))

    def left_left(self, node):
        new_root = node.left
        temp = new_root.right

        new_root.right = node
        node.left = temp

        self.update_height(node)
        self.update_height(new_root)

        return new_root

    def right_right(self, node):
        new_root = node.right
        temp = new_root.left

        new_root.left = node
        node.right = temp

        self.update_height(node)
        self.update_height(new_root)

        return new_root

    def left_right(self, node):
        node.left = self.right_right(node.left)
        return self.left_left(node)

    def right_left(self, node):
        node.right = self.left_left(node.right)
        return self.right_right(node)

    def insert(self, data):
        def _insert(node, data):
            if node is None:
                return AVLTree.Node(data)

            if data < node.data:
                node.left = _insert(node.left, data)
            elif data > node.data:
                node.right = _insert(node.right, data)
            else:
                return node

            self.update_height(node)
            balance = self.balance_factor(node)

            if balance > 1 and self.balance_factor(node.left) >= 0:
                return self.left_left(node)

            if balance < -1 and self.balance_factor(node.right) <= 0:
                return self.right_right(node)

            if balance > 1 and self.balance_factor(node.left) < 0:
                return self.left_right(node)

            if balance < -1 and self.balance_factor(node.right) > 0:
                return self.right_left(node)

            return node

        self.root = _insert(self.root, data)

    def delete(self, data):
        def _delete(node, data):
            if node is None:
                return None

            if data < node.data:
                node.left = _delete(node.left, data)
            elif data > node.data:
                node.right = _delete(node.right, data)
            else:
                if not node.left and not node.right:
                    return None

                if node.left and not node.right:
                    return node.left

                if not node.left and node.right:
                    return node.right

                if node.left and node.right:
                    successor = node.right
                    while successor.left is not None:
                        successor = successor.left

                    node.data = successor.data

                    node.right = _delete(node.right, successor.data)

            if node is None:
                return node

            self.update_height(node)
            balance = self.balance_factor(node)

            if balance > 1 and self.balance_factor(node.left) >= 0:
                return self.left_left(node)

            if balance < -1 and self.balance_factor(node.right) <= 0:
                return self.right_right(node)

            if balance > 1 and self.balance_factor(node.left) < 0:
                return self.left_right(node)

            if balance < - 1 and self.balance_factor(node.right) > 0:
                return self.right_left(node)

            return node

        self.root = _delete(self.root, data)

    def search(self, data):
        def _search(node, data):
            if node is None:
                return None

            if data == node.data:
                return node

            if data < node.data:
                return _search(node.left, data)
            else:
                return _search(node.right, data)

        return _search(self.root, data)