from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


# Time O(N) | Space O(N)
def tree_right_view(root):
    result = []
    if not root:
        return result

    queue = deque([root])

    while queue:
        level_length = len(queue)
        for i in range(level_length):
            node = queue.pop()
            if i == level_length - 1:
                result.append(node)
            if node.left:
                queue.appendleft(node.left)
            if node.right:
                queue.appendleft(node.right)

    return result


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    root.left.left.left = TreeNode(3)
    result = tree_right_view(root)
    print("Tree right view: ")
    for node in result:
        print(str(node.val) + " ", end='')


if __name__ == '__main__':
    main()
