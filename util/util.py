def printList(head):
    while head:
        if head.next:
            print str(head.val) + ',',
        else:
            print head.val
        head = head.next
