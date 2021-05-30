class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


# Time O(N) | Space O(1)
def is_palindromic_linked_list(head):
    if not head or not head.next:
        return True

    slow = fast = head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next

    head_second_half = reverse_list(slow.next)

    result = True
    first_pos = head
    second_pos = head_second_half
    while result and second_pos:
        if first_pos.value != second_pos.value:
            result = False
        first_pos = first_pos.next
        second_pos = second_pos.next

    slow.next = reverse_list(head_second_half)

    return result


def reverse_list(head):
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
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(2)

    print("Is palindrome: " + str(is_palindromic_linked_list(head)))

    head.next.next.next.next.next = Node(2)
    print("Is palindrome: " + str(is_palindromic_linked_list(head)))


if __name__ == '__main__':
    main()
