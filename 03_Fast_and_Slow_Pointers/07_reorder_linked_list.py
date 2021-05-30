class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def print_list(self):
        temp = self
        while temp is not None:
            print(str(temp.value) + " ", end='')
            temp = temp.next
        print()


# Time O(N) | Space O(1)
def reorder_linked_list(head):
    if not head or not head.next:
        return

    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    prev = None
    curr = slow
    while curr:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp

    prev.print_list()

    first, second = head, prev
    while first and second:
        first_temp = first.next
        first.next = second
        first = first_temp

        second_temp = second.next
        second.next = first
        second = second_temp

    if first:
        first.next = None


def reverse(head):
    prev = None
    curr = head
    while curr:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
    return prev


def main():
    head = Node(2)
    head.next = Node(4)
    head.next.next = Node(6)
    head.next.next.next = Node(8)
    head.next.next.next.next = Node(10)
    head.next.next.next.next.next = Node(12)
    reorder_linked_list(head)
    head.print_list()


if __name__ == '__main__':
    main()
