# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.reverseHelper(head)


    def reverseHelper(self, node) -> ListNode:
        if node is None or node.next is None: 
            return node
        back = self.reverseHelper(node.next)
        node.next.next = node
        node.next = None
        return back 
        