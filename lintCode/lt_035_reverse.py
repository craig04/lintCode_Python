class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    @param: head: n
    @return: The new head of reversed linked list.
    """

    def reverse(self, head):
        fake = ListNode(0)
        node = head
        while node:
            next = node.next
            node.next = fake.next
            fake.next = node
            node = next
        return fake.next
