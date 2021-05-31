class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def print_path(root, sum_):
    if sum_ == 0:
        return True

    if root is None:
        return False

    left = print_path(root.left, sum_ - root.val)
    right = print_path(root.right, sum_ - root.val)

    if left or right:
        print(root.val, end=' ')

    return left or right


def get_root_to_leaf_sum(root):
    if root is None:
        return 0
    left = get_root_to_leaf_sum(root.left)
    right = get_root_to_leaf_sum(root.right)
    return (left if left > right else right) + root.val


# Time O(N(log(N))) | Space O(N(log(N)))
def find_max_sum_path(root):
    sum_ = get_root_to_leaf_sum(root)
    print("The maximum sum is: ", sum_)
    print("The maximum sum path is: ", end='')
    print_path(root, sum_)


def main():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(8)
    root.left.right = TreeNode(4)
    root.right.left = TreeNode(5)
    root.right.right = TreeNode(6)
    root.left.right.left = TreeNode(10)
    root.right.left.left = TreeNode(7)
    root.right.left.right = TreeNode(9)
    root.right.right.right = TreeNode(5)
    find_max_sum_path(root)


if __name__ == '__main__':
    main()
