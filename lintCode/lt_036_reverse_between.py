class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    @param: head: ListNode head is the head of the linked list
    @param: m: An integer
    @param: n: An integer
    @return: The head of the reversed ListNode
    """

    def reverseBetween(self, head, m, n):
        fake = ListNode(0)
        fake.next = head
        prev = fake
        for i in range(1, m):
            prev = fake.next
        node = prev.next
        prev.next = None
        for i in range(n - m + 1):
            next = node.next
            node.next = prev.next
            prev.next = node
            node = next
        while prev.next:
            prev = prev.next
        prev.next = node
        return fake.next
