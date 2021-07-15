# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        try:
            hare = head.next
            tortoise = head
            while hare is not tortoise:
                hare = hare.next.next
                tortoise = tortoise.next
            return True
        except AttributeError:
            return False
