class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Time O(N(log(N))) | Space O(N(log(N)))
def find_paths(root, target):
    res = []
    dfs(root, target, [], res)
    return res


def dfs(root, target, path, res):
    if root:
        if not root.left and not root.right and target == root.val:
            res.append(path + [root.val])
        dfs(root.left, target - root.val, path + [root.val], res)
        dfs(root.right, target - root.val, path + [root.val], res)


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(4)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    required_sum = 23
    print("Tree paths with required_sum " + str(required_sum) + ": " + str(find_paths(root, required_sum)))


if __name__ == '__main__':
    main()
