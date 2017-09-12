class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    @param: head: The first node of linked list.
    @param: n: An integer
    @return: Nth to last node of a singly linked list.
    """

    def nthToLast(self, head, n):
        anchor = head
        for i in range(n):
            anchor = anchor.next
        while anchor:
            head = head.next
            anchor = anchor.next
        return head
