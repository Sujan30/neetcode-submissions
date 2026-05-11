# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        if list1 == None and list2 == None:
            return None
        if list1 == None:
            return list2
        if list2 == None:
            return list1
        
        x = list1
        y = list2

        head = ListNode(0)
        z = head
        while x != None and y != None:
            if x.val < y.val:
                z.next = x
                x = x.next
            else:
                z.next = y
                y = y.next
            z = z.next

        while x!=None:
            z.next = x
            z = z.next
            x = x.next
        while y!=None:
            z.next = y
            z = z.next
            y = y.next
        
        return head.next


        