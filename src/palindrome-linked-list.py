# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        cur = head
        num = []
        while cur != None:
            num.append(str(cur.val))
            cur = cur.next
        return num == num[::-1]