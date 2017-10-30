class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    """
    @param: head: a ListNode
    @return: a ListNode
    """

    def swapPairs(self, head):
        fake = ListNode(-1)
        fake.next = head
        head = fake
        while head.next and head.next.next:
            swap = head.next
            head.next = swap.next
            swap.next = head.next.next
            head.next.next = swap
            head = head.next.next
        return fake.next
