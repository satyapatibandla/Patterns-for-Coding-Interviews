from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


# Time O(N) | Space O(N)
def level_order_traversal(root):
    result = []
    if not root:
        return result

    queue = deque([root])
    while queue:
        level_vals = []
        level_length = len(queue)
        for _ in range(level_length):
            node = queue.pop()
            level_vals.append(node.val)
            if node.left:
                queue.appendleft(node.left)
            if node.right:
                queue.appendleft(node.right)
        result.append(level_vals)

    return result


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Level order traversal: " + str(level_order_traversal(root)))


if __name__ == '__main__':
    main()
