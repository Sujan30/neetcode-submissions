# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head
        
        x = head
        prev = None

        while x!= None:
            curr = x
            temp = x.next
            curr.next = prev
            prev = curr
            x = temp
        return prev
