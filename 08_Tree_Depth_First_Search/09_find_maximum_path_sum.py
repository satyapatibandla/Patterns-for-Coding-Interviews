class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Time O(N) | Space O(N)
def find_maximum_path_sum(root):
    max_path_sum = [float('-inf')]
    helper(root, max_path_sum)
    return max_path_sum[0]


def helper(node, max_path_sum):
    if not node:
        return 0
    left_gain = max(helper(node.left, max_path_sum), 0)
    right_gain = max(helper(node.right, max_path_sum), 0)
    max_path_sum[0] = max(max_path_sum[0], left_gain + node.val + right_gain)
    return node.val + max(left_gain, right_gain)


def main():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)

    print("Maximum Path Sum: " + str(find_maximum_path_sum(root)))
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    root.right.left = TreeNode(5)
    root.right.right = TreeNode(6)
    root.right.left.left = TreeNode(7)
    root.right.left.right = TreeNode(8)
    root.right.right.left = TreeNode(9)
    print("Maximum Path Sum: " + str(find_maximum_path_sum(root)))

    root = TreeNode(-1)
    root.left = TreeNode(-3)
    print("Maximum Path Sum: " + str(find_maximum_path_sum(root)))


if __name__ == '__main__':
    main()
