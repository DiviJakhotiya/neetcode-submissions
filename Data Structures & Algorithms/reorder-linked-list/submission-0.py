# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        pointer1 = head
        pointer2 = head
        temp = head
        while pointer2.next:
            pointer2 = pointer2.next
        while pointer1 != pointer2:
            temp = pointer1.next
            pointer1.next = pointer2
            pointer2.next = temp
            pointer1 = temp
            while temp and temp.next != pointer2:
                temp = temp.next
            pointer2 = temp
        pointer2.next = None

        