# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f"Node value {self.val}, next node {self.next.val if self.next else None}"


class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head:
            return None
        if not head.next:
            return head
        is_odd = True
        odd, odd_start = None, None
        even, even_start = None, None
        while head:
            if is_odd:
                if odd is not None:
                    odd.next = head
                    odd = odd.next
                else:
                    odd = head
                    odd_start = odd
            else:
                if even is not None:
                    even.next = head
                    even = even.next
                else:
                    even = head
                    even_start = head
            head = head.next
            is_odd = not is_odd
        odd.next = even_start
        even.next = None
        return odd_start
