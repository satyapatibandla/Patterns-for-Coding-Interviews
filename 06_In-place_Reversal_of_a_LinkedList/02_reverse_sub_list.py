class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def print_list(self):
        temp = self
        while temp is not None:
            print(temp.value, end=" ")
            temp = temp.next
        print()


# Time O(N) | Space O(1)
def reverse_sub_list(head, left, right):
    if not head:
        return None

    if left == right:
        return head

    curr, prev = head, None
    while left > 1:
        prev = curr
        curr = curr.next
        left -= 1
        right -= 1

    last_node_of_first_part = prev
    last_node_of_sub_list = curr

    while right:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
        right -= 1

    if last_node_of_first_part is not None:
        last_node_of_first_part.next = prev
    else:
        head = prev

    last_node_of_sub_list.next = curr
    return head


def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)

    print("Nodes of original LinkedList are: ", end='')
    head.print_list()
    result = reverse_sub_list(head, 2, 4)
    print("Nodes of reversed LinkedList are: ", end='')
    result.print_list()


if __name__ == '__main__':
    main()
