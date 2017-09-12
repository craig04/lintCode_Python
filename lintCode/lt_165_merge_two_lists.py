class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    @param two ListNodes
    @return a ListNode
    """

    def mergeTwoLists(self, l1, l2):
        fake = node = ListNode(0)
        while l1 and l2:
            pick = l1 if l1.val < l2.val else l2
            next = pick.next
            pick.next = node.next
            node.next = pick
            node = node.next
            if l1.val < l2.val:
                l1 = next
            else:
                l2 = next
        node.next = l1 if l1 else l2
        return fake.next
