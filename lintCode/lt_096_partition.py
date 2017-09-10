class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    @param: head: The first node of linked list
    @param: x: An integer
    @return: A ListNode
    """

    def partition(self, head, x):
        first = f = ListNode(0)
        second = s = ListNode(0)
        while head:
            next = head.next
            if head.val < x:
                f.next = head
                f = f.next
            else:
                s.next = head
                s = s.next
            head = next
        s.next = None
        f.next = second.next
        return first.next
