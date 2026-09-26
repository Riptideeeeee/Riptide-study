# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head):
        while head and head.next:
            slow = slow.next
            fast = fast.next.next
        print(slow.val)
        print(fast.val)
s = Solution()
s.middleNode(head=ListNode([1,2,3,4,5]))