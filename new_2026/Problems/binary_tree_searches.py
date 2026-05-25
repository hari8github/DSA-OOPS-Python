class TreeNode:
    def __init__(self, val, right = None, left = None):
        self.val = val
        self.right = right
        self.left = left
    def __str__(self):
        return str(self.val)

A = TreeNode(10)
B = TreeNode(20)
C = TreeNode(30)
D = TreeNode(40)
E = TreeNode(50)

A.left = B
A.right = C
B.left = D
B.right = E

"""1) Given a binary tree, find its maximum depth (height)."""

def max_depth(node):
    if node is None:                                      # base case — empty node
        return 0
    else:
        depth = 1 + max(max_depth(node.left), max_depth(node.right))  # 1 (current node) + deeper subtree
    return depth                                     

(max_depth(A))
"""2) Given a binary tree, return all node values level by level (BFS)."""

from collections import deque
def bfs(node):
    q = deque()
    q.append(node)              # start with root in queue
    while q:                    # continue while queue has elements
        node = q.popleft()      # dequeue front node
        print(node)             # visit node
        if node.left:           # enqueue left child if exists
            q.append(node.left)
        if node.right:          # enqueue right child if exists
            q.append(node.right)

"""3) Given a binary tree, check if it is symmetric (mirror of itself)."""

def is_mirror(left, right):
    if not left and not right:   # both None — symmetric at this point
        return True
    if not left or not right:    # one is None, other isn't — not symmetric
        return False
    return (left.val == right.val and           # current values must match
            is_mirror(left.left, right.right) and  # outer nodes must mirror
            is_mirror(left.right, right.left))     # inner nodes must mirror

def symmetry(node):
    if node is None:             # empty tree is symmetric
        return True
    return is_mirror(node.left, node.right)  # check left and right subtrees

(symmetry(A))

"""4) Given a BST, check if a value exists in it."""

BST = TreeNode(10)
BST.left = TreeNode(5)
BST.right = TreeNode(15)
BST.left.left = TreeNode(3)
BST.left.right = TreeNode(7)
BST.right.left = TreeNode(12)
BST.right.right = TreeNode(20)

def search_bst(node, target):
    if not node:
        return False
    if node.val == target:
        return True
    if target < node.val:
        return search_bst(node.left, target)
    else:
        return search_bst(node.right, target)

(search_bst(BST, 2))

"""5) Given a BST, insert a new value in the correct position."""

def insert_bst(node, val):
    if not node:                              # base case — empty spot found, insert here
        return TreeNode(val)
    if val < node.val:                        # value smaller — go left
        node.left = insert_bst(node.left, val)   # link result back to left
    else:                                     # value larger — go right
        node.right = insert_bst(node.right, val)  # link result back to right
    return node

(insert_bst(BST, 2))
(search_bst(BST, 2))