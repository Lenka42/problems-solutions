# Definition for singly-linked list.
class ListNode:
    def __repr__(self):
        return f"Node value {self.val}, next node {self.next.val if self.next else None}"

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class SolutionIterative:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        # first node becomes last node
        prev = None
        curr = head
        while curr:
            curr.next, prev, curr = prev, curr, curr.next
        return prev


class SolutionMagic:  # recursive
    def reverseList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        p = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return p
