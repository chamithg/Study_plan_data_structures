# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        charMap = set()
        dh = ListNode()
        dh.next = head
        curr = dh

        while curr.next:
            if curr.next.val not in charMap:
                charMap.add(curr.next.val)
                curr = curr.next
            else:
                if curr.next.next:curr.next = curr.next.next
                else: curr.next = None
        
        return dh.next