# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        a,b=head,head
        while a and a.next:
            a=a.next.next
            b=b.next
            if a==b:
                return True

        return False