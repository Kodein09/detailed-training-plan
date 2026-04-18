# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
#
# n1 = Node(1)
# n2 = Node(2)
# n3 = Node(3)
#
# n1.next = n2
# n2.next = n3
#
# n1.next.data = 19
# n2.next.data = 29
# print("Current n1 data:", n1.data)
# print("Next node n2 data:", n1.next.data)
# print(n2.data)
# print(n3.data)


# # # #Binary Tree
# # # class Node:    #Каждая вершина\объект бинарного дерева будет определяться через
# # #     def __init__(self, data):
# # #         self.data = data    #Указатель данных на вершине
# # #         self.left = self.right = None    #Указатели на потомков левый и правый
# # #
# # # class Tree:
# # #     def __init__(self):
# # #         self.root = None
# # #
# # #     def __find(self, node, parent, value):
# # #         if node is None:
# # #             return None, parent, False
# # #
# # #         if value == node.data:
# # #             return node, parent, True
# # #
# # #         if value < node.data:
# # #             if node.left:
# # #                 return self.__find(node.left, node, value)
# # #
# # #         if value > node.data:
# # #             if node.right:
# # #                 return self.__find(node.right, node, value)
# # #
# # #         return node, parent, False
# # #
# # #     def append(self, value):
# # #         if self.root is None:
# # #             self.root = value
# # #             return value
# # #
# # #         s, p, fl__find = self.__find(self.root, None, value.data)
# # #
# # #         if not fl__find and s:
# # #             if value.data < s.data:
# # #                 s.left = value
# # #             else:
# # #                 s.right = value
# # #         return value
# # #
# # #     def show_tree(self, node):
# # #         if node is None:
# # #             return
# # #
# # #         self.show_tree(node.left)
# # #         print(node.data)    #Curreny value on the top
# # #         self.show_tree(node.right)
# # #
# # # arr = [20,4,6,7,19,13,9,10]
# # # t = Tree()
# # #
# # # for x in arr:
# # #     t.append(Node(x))
# # #
# # # t.show_tree(t.root)
# #
# #
# # class Node:
# #     def __init__(self, data):
# #         self.data = data
# #         self.left = self.right = None
# #
# # class Tree:
# #     def __init__(self):
# #         self.root = None
# #
# #     def __find(self, node, parent, value):
# #         if node is None:
# #             return None, parent, False
# #
# #         if value == node.data:
# #             return node, parent, True
# #
# #         if value < node.data:
# #             if node.left:
# #                 return self.__find(node.left, node, value)
# #
# #         if value > node.data:
# #             if node.right:
# #                 return self.__find(node.right, node, value)
# #
# #         return node, parent, False
# #
# #     def append(self, obj):
# #         if self.root is None:
# #             self.root = obj
# #             return obj
# #
# #         s, p, fl_find = self.__find(self.root, None, obj.data)
# #
# #         if not fl_find and s:
# #             if obj.data < s.data:
# #                 s.left = obj
# #             else:
# #                 s.right = obj
# #
# #         return obj
# #
# #     def show_tree(self, node):
# #         if node is None:
# #             return
# #
# #         self.show_tree(node.left)
# #         print(node.data)
# #         self.show_tree(node.right)
# #
# #     def del_leaf(self, s, parent):
# #         if parent.left == s:
# #             parent.left = None
# #
# #         elif parent.right == s:
# #             parent.right = None
# #
# #     def __del_one_child(self, s, parent):    #Удаление вершин только с одни с одним потомком
# #         if parent.left == s:
# #             if s.left is None:
# #                 parent.left = s.right
# #             elif s.right is None:
# #                 parent.left = s.left
# #
# #         elif parent.right == s:
# #             if s.right is None:
# #                 parent.right = s.right
# #             elif s.left is None:
# #                 parent.right = s.left
# #
# #     def __find_min(self, node, parent):
# #         if node.left:
# #             return self.__find_min(node.left, node)
# #
# #         return node, parent
# #
# #     def delete_node(self, key):
# #         s, parent, flag_find = self.__find(self.root, None, key)
# #
# #         if not flag_find:
# #             return None
# #
# #         if s.left is None and s.right is None:
# #             self.del_leaf(s, parent)
# #
# #         elif s.left is None or s.right is None:
# #             self.__del_one_child(s, parent)
# #
# #         else:
# #             sr, pr = self.__find_min(s.right, s)
# #             s.data = sr.data
# #             self.__del_one_child(sr, pr)
# #
# #     def search_node(self, value):
# #
# #
# # t = Tree()
# #
# # arr = [10, 5, 7, 16, 13, 2, 20]
# #
# # for x in arr:
# #     t.append(Node(x))
# #
# # t.show_tree(t.root)
#
#
# # class TreeNode:
# #     def __init__(self, data):
# #         self.data = data
# #         self.left = self.right = None
# #
# # root = TreeNode('R')
# # nodeA = TreeNode('A')
# # nodeB = TreeNode('B')
# # nodeC = TreeNode('C')
# # nodeD = TreeNode('D')
# # nodeE = TreeNode('E')
# # nodeF = TreeNode('F')
# # nodeG = TreeNode('G')
# #
# # root.left = nodeA
# # root.right = nodeB
# #
# # nodeA.left = nodeC
# # nodeA.right = nodeD
# #
# # nodeB.left = nodeE
# # nodeB.right = nodeF
# #
# # nodeF.left = nodeG
# #
# # # print("root.left.right.data:", root.left.right.data)
# # # print(f"Write word 'FAR' by root and nodes: {root.right.right.data}{root.left.data}{root.data}")
# # # print(f"Write word 'CAR' by root and nodes: {root.left.left.data}{root.left.data}{root.data}")
# #
# # def pre_order(node):
# #     if node is None:
# #         return
# #     print(f"Pre-order node: {node.data}")
# #     pre_order(node.left)
# #     pre_order(node.right)
# #
# # print("Pre-order:", pre_order(root))
# #
# # def in_order(node):
# #     if node is None:
# #         return 0
# #
# #     in_order(node.left)
# #     print(f"In-order: {node.data}")
# #     in_order(node.right)
# #
# # print("Print in-order:", in_order(root))
# #
# # def post_order(node):
# #     if node is None:
# #         return
# #
# #     post_order(node.left)
# #     post_order(node.right)
# #     print(node.data)
# # print(post_order(root))
#
# # def search(nums: list[int], target: int) -> int:
# #     left = 0
# #     right = len(nums) - 1
# #
# #     while left < right:
# #         mid = (left + right) // 2
# #
# #         if nums[mid] == target:
# #             return nums[mid]
# #
# #         if nums[mid] > target:
# #             right = mid - 1
# #         else:
# #             left = mid - 1
# #         return mid
# #     return -1
# # print(search([1,5,-2,9,0,3,12], 9))
#
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
#         else:
#             if data < node.data:
#                 node.left = self.insert(node.left, data)
#             elif data > node.data:
#                 node.right = self.insert(node.right, data)
#         return node
#
#     def search(self, node, data):
#         if node is None:
#             return None
#
#         if data == node.data:
#             return node
#
#         elif data < node.data:
#             return self.search(node.left, data)
#
#         else:
#             return self.search(node.right, data)
#
#     def delete(self, node, data):
#         if node is None:
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
#             elif not node.right:
#                 temp = node.left
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
#
#     def max_value_node(self, node):
#         if node is None:
#             return None
#
#         current = node
#         while current.right is not None:
#             current = current.right
#         return current
#
# tree = BinarySearchTree()
# tree.root = tree.insert(tree.root, 10)
# tree.insert(tree.root, 5)
# tree.insert(tree.root, 15)
# print("Inserted value in BST:", tree.root.data)
# print("Inserted value in BST:", tree.root.left.data)
# print("Inserted value in BST:", tree.root.right.data)
#
# found = tree.search(tree.root, 15)
# print(f"Found data in BST: {found.data}")
#
# min_node = tree.min_value_node(tree.root)
# print(f"Min value in BST: {min_node.data}")
#
# max_node = tree.max_value_node(tree.root)
# print(f"Max value in BST: {max_node.data}")
#
# delete = tree.delete(tree.root, 15)
# print(f"Deleting value from BST: {delete}")

# from collections import deque
#
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.left = None
#         self.right = None
#
# class BinaryTree:
#     def __init__(self):
#         self.root = None
#
#     def insert(self, node, data):
#         new_node = Node(data)
#         if node is None:
#             self.root = new_node
#
#         q = deque([self.root])
#         while q:
#             node = q.popleft()
#             if not node.left:
#                 node.left = new_node
#                 return
#             else:
#                 q.append(node.left)
#
#             if not node.right:
#                 node.right = new_node
#                 return
#             else:
#                 q.append(node.right)


# class Node:
#     def __init__(self, data=0, left=None, right=None):
#         self.data = data
#         self.left = left
#         self.right = right
#
# from collections import deque


# class Tree:
#     def __init__(self, root=None):
#         self.root = root
#
#     def __str__(self):
#         return str(Node().data)
#
#     def append(self, data):
#         if not self.root:
#             self.root = Node(data)
#             return self.root
#
#         queue = deque()
#         queue += [self.root]
#         while len(queue) > 0:
#             current_node = queue.popleft()
#             #if node has no children - insert node
#             #start from the left
#             if not current_node.left:
#                 current_node.left = Node(data)
#                 #print(self.bfs())
#                 return self.root
#             if not current_node.right:
#                 current_node.right = Node(data)
#                 #print(self.bfs())
#                 return self.root
#
#             queue.append(current_node.left)
#             #print(queue)
#             queue.append(current_node.right)
#             #print(queue)
#         return None
#
#     def search_bfs(self, data):
#         if not self.root:
#             print("Tree is empty")
#             return None
#
#         queue = deque([self.root])
#         print(f"Searching for element: {data}")
#         print(f"State of que right now: {[node.data for node in queue]}")
#
#         while queue:
#             print(queue)
#             node = queue.popleft()    #Extract node from the beginning
#             print(f"Extract from que (current node): {node.data}")
#
#             if node.data == data:
#                 print(f"The element was found: {node.data}")
#                 return node.data
#
#             if node.left:
#                 queue.append(node.left)
#                 print(f"Add in que left-child: {node.left.data}")
#
#             if node.right:
#                 queue.append(node.right)
#                 print(f"Add in que right-child: {node.right.data}")
#         return None

    # def search_bfs(self, data):
    #     if not self.root:
    #         return None
    #
    #     queue = deque([self.root])
    #     while queue:
    #         node = queue.popleft()
    #
    #         if node.data == data:
    #             return node.data
    #
    #         if node.left:
    #             queue.append(node.left)
    #         if node.right:
    #             queue.append(node.right)
    #
    #     return None

#     def search_dfs(self, node, data):
#         if not node:
#             return None
#
#         print(f"Visiting node: {node.data}")
#
#         print(f"Current node: {node.data}")
#         if node.data == data:
#             print(f"Find node: {node.data}!")
#             return node
#
#         print(f"Turn to left sub-tree from node: {node.data}")
#         left_node = self.search_dfs(node.left, data)
#         if left_node:
#             return left_node
#
#         print(f"Turn to right sub-tree from node: {node.data}")
#         right_node = self.search_dfs(node.right, data)
#         if right_node:
#             return right_node
#
#         return None
#
#     def bfs(self):
#         queue = deque()
#         queue += [self.root]
#         while queue:
#             for _ in range(len(queue)):
#                 node = queue.popleft()
#                 if node is not None:
#                     print(node.data, end=' ')
#                     queue += [node.left]
#                     queue += [node.right]
#             print()
#
#     def dfs(self):
#         pass
#
#     def insert_via_bfs(self, data):
#         if not self.root:
#             self.root = Node(data)
#             print(f"Inserted new root: {self.root}")
#             return self.bfs()
#
#         queue = deque([self.root])
#
#         while queue:
#             node = queue.popleft()
#
#             if not node.left:
#                 node.left = Node(data)
#                 print(f"Inserted {data} as new left child of node - {node.data}")
#                 return self.bfs()
#             else:
#                 queue.append(node.left)
#
#             if not node.right:
#                 node.right = Node(data)
#                 print(f"Inserted {data} as new right child of node - {node.data}")
#                 return self.bfs()
#             else:
#                 queue.append(node.right)
#
#         return None
#
#     def delete_node(self, data):
#         if not self.root:
#             return
#
#         queue = deque([self.root])
#         target_node = None
#         node = None
#
#         while queue:
#             node = queue.popleft()
#             print(f"Current node '{node.data}' and also this node has been removed from queue")
#
#             if node.data == data:
#                 target_node = node
#
#             if node.left:
#                 queue.append(node.left)
#                 print(f"Node '{node.left.data}' was added in queue")
#
#             if node.right:
#                 queue.append(node.right)
#                 print(f"Node '{node.right.data}' was added in queue")
#
#         if target_node is None:
#             print(f"Node with value {data} not found")
#             return
#
#         temp_data = node.data
#
#         self._delete_deepest(node)
#
#         target_node.data = temp_data
#         print(f"Successfully deleted node: {data}. Replacement was made via {temp_data}")
#
#     def _delete_deepest(self, data):
#         queue = deque([self.root])
#
#         while queue:
#             node = queue.popleft()
#             print(f"Current node: {node.data}")
#
#             if node.data == data:
#                 node.data = None
#                 return
#
#             if node.left == data:
#                 print(f"Current node: {node.data}, child node: '{node.left.data}' will be None")
#                 node.left = None
#                 return
#
#             if node.right == data:
#                 print(f"Current node: {node.data}, child node: '{node.left.data}' will be None")
#                 node.right = None
#                 return
#
#             if node.left:
#                 queue.append(node.left)
#                 print(f"Append node '{node.left.data}' in queue")
#             if node.right:
#                 queue.append(node.right)
#                 print(f"Append node '{node.right.data}' in queue")
#
#
# tree = Tree()
# tree.append("A")
# tree.append("B")
# tree.append("C")
# tree.append("D")
# tree.append("E")
# tree.append("F")
# tree.append("G")
# tree.bfs()
#
# find_letter = tree.search_bfs('G')
# print(find_letter)
# print(tree.search_dfs(tree.root, 'E'))
# tree.insert_via_bfs("H")
# tree.insert_via_bfs("I")
# tree.insert_via_bfs("K")
# tree.delete_node("I")
# tree.bfs()

from collections import deque

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if not self.root:
            self.root = Node(data)
            return

        queue = deque([self.root])
        while queue:
            node = queue.popleft()

            if not node.left:
                node.left = Node(data)
                return

            if not node.right:
                node.right = Node(data)
                return

        return

    def search_bfs(self, data):
        if not self.root:
            return None

        queue = deque([self.root])
        while queue:
            node = queue.popleft()

            if node.data == data:
                return node.data

            if node.left == data:
                return node.left.data

            if node.right == data:
                return node.left.data

        return None

    def search_dfs(self, node, data):
        if not node:
            return None

        print(f"Visiting node: {node.data}")

        if node.data == data:
            print(f"Find searching node: {node.data}")
            return node.data

        print(f"Turn to left sub-tree from current node: {node.data}")
        node_left = self.search_dfs(node.left, data)
        if node_left:
            return node_left

        print(f"Turn to right sub-tree from current node: {node.data}")
        node_right = self.search_dfs(node.right, data)
        if node_right:
            return node_right

        return None

    def delete(self, data):
        if not self.root:
            return

        queue = deque([self.root])
        target_node = None
        node = None

        while queue:
            node = queue.popleft()

            if node.data == data:
                target_node = node

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        if target_node is None:
            print(f"Can't find node with value {data}")
            return

        temp_data = node.data

        self._delete_deepest(node)
        target_node.data = temp_data
        print(f"Node {data} was successfully deleted. Replacement was made via {temp_data}")


    def _delete_deepest(self, data):
        queue = deque([self.root])
        while queue:
            node = queue.popleft()

            if node.left == data:
                node.left = None
                return
            if node.right == data:
                node.right = None
                return

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    def traversal_bfs(self):
        if not self.root:
            return None

        queue = deque([self.root])
        while queue:
            node = queue.popleft()

            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)

        return None

    def traversal_dfs(self, node):
        if not node:
            return

        if node.left:
            self.traversal_dfs(node.left)
        if node.right:
            self.traversal_dfs(node.right)

        return

tree = BinaryTree()
tree.traversal_bfs()

#Leetcode 897
# class BinaryTree:
#     class Node:
#         def __init__(self, val):
#             self.val = val
#             self.left = None
#             self.right = None
#
#     def __init__(self):
#         self.root = None
#
#     def bfs_insert(self, value):
#         if self.root is None:
#             self.root = Node(value)
#             return
#
#         queue = [self.root]
#         while queue:
#             node = queue.pop(0)
#
#             if not node.left:
#                 node.left = Node(value)
#                 return
#             if not node.right:
#                 node.right = Node(value)
#                 return
#
#             if node.left:
#                 queue.append(node.left)
#
#             if node.right:
#                 queue.append(node.right)
#
#     def increasing(self):
#         self.dfs_in_order(self.root)
#
#     def dfs_in_order(self, node, parent=None):
#         if node is None:
#             return
#
#         parent = node
#         print(node.val)
#         print(parent.val)
#         self.dfs_in_order(node.left, parent)
#         print(node.val, parent.val)
#         self.dfs_in_order(node.right, parent)
#
# bt = BinaryTree()
# bt.bfs_insert(10)
# bt.bfs_insert(10)
# bt.bfs_insert(20)
# bt.bfs_insert(6)
# bt.bfs_insert(6)
# bt.bfs_insert(2)
# bt.bfs_insert(2)
# bt.dfs_in_order(bt.root)
#897
# class Solution:
#     class Node:
#         def __init__(self, data):
#             self.data = data
#             self.left = None
#             self.right = None
#
#     def __init__(self):
#         self.root = None
#         self.current = None
#
#     def insert(self, value):
#         if not self.root:
#             self.root = Node(value)
#             return
#
#         queue = [self.root]
#         while queue:
#             node = queue.pop(0)
#
#             if not node.left:
#                 node.left = Node(value)
#                 return
#
#             if not node.right:
#                 node.right = Node(value)
#                 return
#
#             if node.left:
#                 queue.append(node.left)
#
#             if node.right:
#                 queue.append(node.right)
#
#     def increasing_bst(self, node):
#         if not node:
#             return
#
#         print(node.data)
#         self.increasing_bst(node.left)
#
#         if self.current:
#             print(node.data)
#             self.current.right = node
#             print("Node right:", node.right.data)
#         else:
#             self.root = node
#
#         print("Node left:", node.left)
#         node.left = None
#         self.current = node
#
#         self.increasing_bst(node.right)
#
# s = Solution()
# s.insert(10)
# s.insert(15)
# s.insert(5)
# s.insert(1)
# s.insert(4)
# s.increasing_bst(s.root)