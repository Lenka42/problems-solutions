# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        result = None
        result_start = None
        transfer = 0
        while l1 or l2 or transfer:
            val = (l1.val if l1 else 0) + (l2.val if l2 else 0) + transfer
            if val > 9:
                val -= 10
                transfer = 1
            else:
                transfer = 0
            node = ListNode(val)
            if result is None:
                result = node
                result_start = node
            else:
                result.next = node
                result = node
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        return result_start


