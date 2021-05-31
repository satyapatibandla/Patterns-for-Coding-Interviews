class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Time O(N) | Space O(N)
def has_path_sum(root, target):
    if not root:
        return False

    if root.val == target and not root.left and not root.right:
        return True

    return has_path_sum(root.left, target - root.val) or has_path_sum(root.right, target - root.val)


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Tree has path sum: " + str(has_path_sum(root, 23)))
    print("Tree has path sum: " + str(has_path_sum(root, 16)))


if __name__ == '__main__':
    main()
