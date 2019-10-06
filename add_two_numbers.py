"""
You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order and each of their nodes contain a single digit. 
Add the two numbers and return it as a linked list.
You may assume the two numbers do not contain any leading zero, 
except the number 0 itself.

Example:
Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 == None:
            return l2
            
        if l2 == None:
            return l1
            
        total_val = l1.val + l2.val
        if total_val < 10:
            new_node = ListNode(total_val)
            new_node .next = self.addTwoNumbers(l1.next, l2.next)
            return new_node 
        else:
            result_val = l1.val + l2.val - 10
            new_node  = ListNode(result_val)
            new_node .next = self.addTwoNumbers(ListNode(1), self.addTwoNumbers(l1.next, l2.next))
            return new_node 

