# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteNodes(self, head: ListNode, m: int, n: int) -> ListNode:
        cur = head
        deleted = 0
        last = None
        while cur != None:
            for i in range(0, m):
                if cur == None:
                    break
                if i == 0 and last != None:
                    last.next = cur
                if i == m - 1:
                    last = cur
                cur = cur.next
            for i in range(0, n):
                if cur == None:
                    break
                last.next = None
                cur = cur.next
        return head