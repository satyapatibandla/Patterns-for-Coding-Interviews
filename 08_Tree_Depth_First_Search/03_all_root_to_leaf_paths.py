class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Time O(N(log(N))) | Space O(N(log(N)))
def find_paths(root):
    res = []
    dfs(root, [], res)
    return res


def dfs(root, path, res):
    if root:
        if not root.left and not root.right:
            res.append(path + [root.val])
        dfs(root.left, path + [root.val], res)
        dfs(root.right, path + [root.val], res)


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(4)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("All root to leaf paths: " + str(find_paths(root)))


if __name__ == '__main__':
    main()
