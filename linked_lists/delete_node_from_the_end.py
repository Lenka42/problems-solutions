# https://leetcode.com/explore/interview/card/top-interview-questions-easy/93/linked-list/603/

class ListNode:
    def __repr__(self):
        return f"Node value {self.val}, next node {self.next.val if self.next else None}"

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(-1, head)
        first = dummy
        second = dummy
        for i in range(0, n + 1):
            first = first.next
        while first is not None:
            first = first.next
            second = second.next
        second.next = second.next.next
        return dummy.next
