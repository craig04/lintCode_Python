class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    @param: head: a ListNode
    @param: val: An integer
    @return: a ListNode
    """

    def removeElements(self, head, val):
        fake = node = ListNode(0)
        while head:
            if head.val != val:
                node.next = head
                node = node.next
            head = head.next
        node.next = None
        return fake.next
