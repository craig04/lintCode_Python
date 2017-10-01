class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    @param: l1: the first list
    @param: l2: the second list
    @return: the sum list of l1 and l2
    """

    def addLists(self, l1, l2):
        c = 0
        fake = node = ListNode(0)
        while l1 or l2:
            l1, v1 = self.__next(l1)
            l2, v2 = self.__next(l2)
            v = v1 + v2 + c
            c = v / 10
            node.next = ListNode(v % 10)
            node = node.next
        if c:
            node.next = ListNode(1)
        return fake.next

    def __next(self, l):
        return [l.next, l.val] if l else [None, 0]
