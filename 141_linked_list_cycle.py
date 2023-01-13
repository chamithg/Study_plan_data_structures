# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # brute force solution -->
        # seenNodes = set()
        # runner = head
        # while runner:
        #     if runner in seenNodes:
        #         return True
        #     else:
        #         seenNodes.add(runner)
        #         runner = runner.next
        # return False
        
        
        # also we can solve this by using hare and torties method
        
        slow = fast = head
        
        while slow and fast and fast.next:
            slow= slow.next
            fast = fast.next.next
            if slow == fast:
                return True
            
        return False
        
        
        
        