def show_list(head):
    while head:
        if head.next:
            print str(head.val) + ',',
        else:
            print head.val
        head = head.next


def show_matrix(matrix):
    for row in matrix:
        print row
