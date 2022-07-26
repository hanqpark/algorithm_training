# Definition for singly-linked list.

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        p = head
        lst = []
        while p:
            lst.append(p.val)
            p = p.next
        
        lst.sort()
        
        p = head
        for l in lst:
            p.val = l
            p = p.next
        return head