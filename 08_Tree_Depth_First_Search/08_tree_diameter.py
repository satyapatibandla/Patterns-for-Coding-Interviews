class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class TreeDiameter:
    def __init__(self):
        self.tree_diameter = 0

    # Time O(N) | Space O(N)
    def find_diameter(self, root):
        self.helper(root)
        return self.tree_diameter

    def helper(self, node):
        if not node:
            return 0
        left = self.helper(node.left)
        right = self.helper(node.right)
        if left is not None and right is not None:
            self.tree_diameter = max(self.tree_diameter, left + right + 1)
        return max(left, right) + 1


def main():
    tree_diameter = TreeDiameter()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.right.left = TreeNode(5)
    root.right.right = TreeNode(6)
    print("Tree Diameter: " + str(tree_diameter.find_diameter(root)))
    root.left.left = None
    root.right.left.left = TreeNode(7)
    root.right.left.right = TreeNode(8)
    root.right.right.left = TreeNode(9)
    root.right.left.right.left = TreeNode(10)
    root.right.right.left.left = TreeNode(11)
    print("Tree Diameter: " + str(tree_diameter.find_diameter(root)))


if __name__ == '__main__':
    main()
