# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        pointer = dummy
        pointer2 = dummy
        for _ in range(n):
            pointer = pointer.next
        while pointer.next:
            pointer = pointer.next
            pointer2 = pointer2.next
        pointer2.next = pointer2.next.next
        return dummy.next
        