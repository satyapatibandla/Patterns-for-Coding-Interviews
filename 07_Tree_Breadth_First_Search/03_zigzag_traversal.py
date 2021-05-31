from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


# Time O(N) | Space O(N)
def zigzag_traversal(root):
    result = []
    if not root:
        return result

    queue = deque([root])
    left_to_right = True

    while queue:
        level_vals = deque([])
        level_length = len(queue)
        for _ in range(level_length):
            node = queue.pop()
            if left_to_right:
                level_vals.append(node.val)
            else:
                level_vals.appendleft(node.val)

            if node.left:
                queue.appendleft(node.left)
            if node.right:
                queue.appendleft(node.right)

        result.append(list(level_vals))
        left_to_right = not left_to_right

    return result


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    root.right.left.left = TreeNode(20)
    root.right.left.right = TreeNode(17)
    print("Zigzag traversal: " + str(zigzag_traversal(root)))


if __name__ == '__main__':
    main()
