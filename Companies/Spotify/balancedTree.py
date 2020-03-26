"""
Write a function that return a boolean representing 
wheather a Binary Tree is balanced.

How to determine if a Binary Tree is hight-balanced:
A tree where no leaf is much farther away from the root 
than any other leaf. Different balancing schemes allow 
different definitions of “much farther” and different amounts 
of work to keep them balanced. Consider a height-balancing 
scheme where following conditions should be checked to determine
if a binary tree is balanced. An empty tree is height-balanced. 

A non-empty binary tree T is balanced if:
1) Left subtree of T is balanced
2) Right subtree of T is balanced
3) The difference between heights of left subtree and right 
subtree is not more than 1.

To check if a tree is height-balanced, get the height of left 
and right subtrees. Return true if difference between heights
is not more than 1 and left and right subtrees are balanced, 
otherwise return false.
"""

class Node:
  #Constructor to create a new Node
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None

# Find the Binary tree height
def height(root):
  # if tree is empty
  if root is None:
    return 0
  return max(height(root.left), height(root.right)) + 1

# Check f Tree is height-balanced or not
def isBalanced(root):
  # Base condition
  if root is None:
    return True

  left_height = height(root.left)
  right_height = height(root.right)

  # Allowed values for (left_height - right_height) 
  # are 1, -1, 0
  if (abs(left_height - right_height) <= 1) and isBalanced(root.left) is True and isBalanced(root.right) is True:
    return True

  # Else the tree is not height-balanced
  return False

if __name__ == '__main__':
  root = Node(1)
  root.left = Node(2)
  root.right = Node(3)
  root.left.left = Node(4)
  root.left.right = Node(5)
  root.left.left.left = Node(8)
  if isBalanced(root):
    print("Tree is balanced")
  else: 
    print("Tree is not balanced")


