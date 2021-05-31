class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Time O(N) | Space O(N)
def find_path_with_given_sequence(root, sequence):
    if not root:
        return len(sequence) == 0
    return dfs(root, sequence, 0)


def dfs(node, sequence, index):
    if not node:
        return False

    seq_len = len(sequence)
    if index >= seq_len or node.val != sequence[index]:
        return False

    if not node.left and not node.right and index == seq_len - 1:
        return True

    return dfs(node.left, sequence, index + 1) or dfs(node.right, sequence, index + 1)


def main():
    root = TreeNode(1)
    root.left = TreeNode(0)
    root.right = TreeNode(1)
    root.left.left = TreeNode(1)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(5)

    print("Tree has path sequence: " + str(find_path_with_given_sequence(root, [1, 0, 7])))
    print("Tree has path sequence: " + str(find_path_with_given_sequence(root, [1, 1, 6])))


if __name__ == '__main__':
    main()
