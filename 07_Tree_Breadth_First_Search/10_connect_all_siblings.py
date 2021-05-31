from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right, self.next = None, None, None

    def print_tree(self):
        print("Traversal using 'next' pointer: ", end='')
        current = self
        while current:
            print(str(current.val) + " ", end='')
            current = current.next


# Time O(N) | Space O(N)
def connect_all_siblings(root):
    if not root:
        return None

    queue = deque([root])
    while queue:
        level_length = len(queue)
        for _ in range(level_length):
            node = queue.pop()
            if node.left:
                queue.appendleft(node.left)
            if node.right:
                queue.appendleft(node.right)
            if queue:
                node.next = queue[-1]

    return root


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    connect_all_siblings(root)
    root.print_tree()


if __name__ == '__main__':
    main()
