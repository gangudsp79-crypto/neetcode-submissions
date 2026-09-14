# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head): 
        if not head and not head.next:
            return 
        #mid break
        slow=head
        fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        second=slow.next
        slow.next=None

        #reverse 2nd LL
        prev=None
        curr=second
        while curr:
            next_node=curr.next
            curr.next=prev
            prev=curr
            curr=next_node
        

        #alternative merge
        first=head
        second=prev
        while second:
            next_first=first.next
            next_second=second.next

            first.next=second
            second.next=next_first

            first=next_first
            second=next_second
        