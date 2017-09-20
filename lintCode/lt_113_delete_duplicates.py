class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    @param: head: head is the head of the linked list
    @return: head of the linked list
    """

    def deleteDuplicates(self, head):
        fake = ListNode(0)
        fake.next = head
        node = fake
        while node.next:
            next = node.next
            while next and next.next and next.next.val == node.next.val:
                next = next.next
            if next != node.next:
                node.next = next.next
            else:
                node = next
        return fake.next
