# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
def min_function(arr):

    if all (arr[i] == None for i in range(len(arr))):
        return -1
    min1 = float('inf')
    for i in range(len(arr)):
        if arr[i] is not None:
            min1 = min(arr[i].val, min1)
    for i in range(len(arr)):
        if arr[i] is not None:
            if min1 == arr[i].val:
                return i
def array_to_linked_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for value in arr[1:]:
        current.next = ListNode(value)
        current = current.next
    return head 
class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        pointerarr = [lists[i] for i in range(len(lists))]
        res = []
        linked = 0
        while linked >= 0:
            linked = min_function(pointerarr)
            if linked == -1:
                break
            res.append(pointerarr[linked].val)
            pointerarr[linked] = pointerarr[linked].next
        return array_to_linked_list(res)
        

        