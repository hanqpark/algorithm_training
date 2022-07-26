# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        q, lst = head, []
        while q:
            lst.append(q.val)
            q = q.next
        
        lst.sort()
        
        q = head
        for l in lst:
            q.val = l
            q = q.next
        
        return head