class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Time O(N^2) | Space O(N)
# Time O(N(log(N))) best case when balanced tree
def count_paths(root, target):
    result = [0]
    cache = {0: 1}
    dfs(root, target, 0, cache, result)
    return result[0]


def dfs(root, target, curr_path_sum, cache, result):
    if root is None:
        return

    curr_path_sum += root.val
    old_path_sum = curr_path_sum - target
    result[0] += cache.get(old_path_sum, 0)

    cache[curr_path_sum] = cache.get(curr_path_sum, 0) + 1

    dfs(root.left, target, curr_path_sum, cache, result)
    dfs(root.right, target, curr_path_sum, cache, result)

    cache[curr_path_sum] -= 1


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(4)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Tree has paths: " + str(count_paths(root, 11)))


if __name__ == '__main__':
    main()
