from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


# Time O(N) | Space O(N)
def find_minimum_depth(root):
    if not root:
        return 0

    queue = deque([root])
    depth = 1
    while queue:
        level_length = len(queue)
        for _ in range(level_length):
            node = queue.pop()
            if not node.left and not node.right:
                return depth
            if node.left:
                queue.appendleft(node.left)
            if node.right:
                queue.appendleft(node.right)
        depth += 1


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Tree Minimum Depth: " + str(find_minimum_depth(root)))
    root.left.left = TreeNode(9)
    root.right.left.left = TreeNode(11)
    print("Tree Minimum Depth: " + str(find_minimum_depth(root)))


if __name__ == '__main__':
    main()
