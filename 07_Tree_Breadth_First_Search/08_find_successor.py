from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


# Time O(N) | Space O(N)
def find_successor(root, key):
    if not root:
        return None
    return_next = False
    queue = deque([root])
    while queue:
        for _ in range(len(queue)):
            curr = queue.pop()
            if return_next:
                return curr
            if key == curr.val:
                return_next = True
            if curr.left:
                queue.appendleft(curr.left)
            if curr.right:
                queue.appendleft(curr.right)
    return None


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    result = find_successor(root, 12)
    if result:
        print(result.val)
    result = find_successor(root, 9)
    if result:
        print(result.val)


if __name__ == '__main__':
    main()
