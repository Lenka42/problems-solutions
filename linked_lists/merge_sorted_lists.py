# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        result_start = ListNode(-1)
        result_head = result_start
        while True:
            if l1 and l2:
                if l1.val <= l2.val:
                    node = l1
                    l1 = l1.next
                else:
                    node = l2
                    l2 = l2.next
            elif l1 is not None:
                node = l1
                l1 = None
            elif l2 is not None:
                node = l2
                l2 = None
            else:
                break
            result_head.next = node
            result_head = result_head.next
        return result_start.next


class SolutionMagic:  # recursive
    def mergeTwoLists(self, a, b):
        if a and b:
            if a.val > b.val:
                a, b = b, a
            a.next = self.mergeTwoLists(a.next, b)
        return a or b