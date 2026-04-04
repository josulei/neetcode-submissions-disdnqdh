# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        curr = head 
        my_set = set()
        temp = True
        while curr is not None and temp: 
            if curr in my_set:
                return True
            else: 
                my_set.add(curr)
            curr = curr.next

        return False