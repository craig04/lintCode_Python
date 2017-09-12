class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    @param: head: A ListNode.
    @return: A boolean.
    """

    def isPalindrome(self, head):
        if not head:
            return True
        fast = slow = head
        while True:
            if not fast or not fast.next or not fast.next.next:
                break
            fast = fast.next.next
            slow = slow.next
        slow.next = self.__reverse(slow.next)
        last = slow.next
        isPalindrome = True
        while last:
            if head.val != last.val:
                isPalindrome = False
                break
            last = last.next
            head = head.next
        slow.next = self.__reverse(slow.next)
        return isPalindrome

    def __reverse(self, head):
        fake = ListNode(0)
        while head:
            next = head.next
            head.next = fake.next
            fake.next = head
            head = next
        return fake.next
