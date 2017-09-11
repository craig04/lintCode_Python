import heapq


class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    @param lists: a list of ListNode
    @return: The head of one sorted list.
    """

    def mergeKLists(self, lists):
        lists = filter(lambda e: e is not None, lists)
        heap = []
        for head in lists:
            heap.append([head.val, head])
        heapq.heapify(heap)

        fake = ListNode(0)
        node = fake
        while heap:
            top = heapq.heappop(heap)
            head = top[1]
            next = head.next
            node.next = head
            node = node.next
            if next:
                heapq.heappush(heap, [next.val, next])
        node.next = None
        return fake.next
