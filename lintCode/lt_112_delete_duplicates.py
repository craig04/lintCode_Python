class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    @param: head: head is the head of the linked list
    @return: head of linked list
    """

    def deleteDuplicates(self, head):
        node = head
        while node:
            next = node.next
            while next and next.val == node.val:
                next = next.next
            node.next = next
            node = next
        return head
