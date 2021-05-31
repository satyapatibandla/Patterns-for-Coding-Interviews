from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right, self.next = None, None, None

    # level order traversal using 'next' pointer
    def print_level_order(self):
        next_level_root = self
        while next_level_root:
            current = next_level_root
            next_level_root = None
            while current:
                print(str(current.val) + " ", end='')
                if not next_level_root:
                    if current.left:
                        next_level_root = current.left
                    elif current.right:
                        next_level_root = current.right
                current = current.next
            print()


# Time O(N) | Space O(N)
def connect_level_order_siblings(root):
    if not root:
        return None

    queue = deque([root])
    while queue:
        level_length = len(queue)
        for i in range(level_length):
            node = queue.pop()
            if i < level_length - 1:
                node.next = queue[-1]
            if node.left:
                queue.appendleft(node.left)
            if node.right:
                queue.appendleft(node.right)

    return root


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    connect_level_order_siblings(root)

    print("Level order traversal using 'next' pointer: ")
    root.print_level_order()


if __name__ == '__main__':
    main()
