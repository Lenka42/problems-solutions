# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        # Reverse the first half while finding the middle.
        rev = None
        fast = head
        while fast and fast.next:
            fast = fast.next.next
            rev, rev.next, head = head, rev, head.next
        tail = head.next if fast else head
        is_pali = True
        # Compare the reversed first half with the second half.
        while rev:
            is_pali = is_pali and rev.val == tail.val
            head, head.next, rev = rev, head, rev.next
            tail = tail.next
        return is_pali
