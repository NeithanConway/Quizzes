# Given the root of a binary tree, determine if it is a valid binary search tree (BST).

# A valid BST is defined as follows:

# The left subtree of a node contains only nodes with keys less than the node's key.
# The right subtree of a node contains only nodes with keys greater than the node's key.
# Both the left and right subtrees must also be binary search trees.

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.isValidBSTRec(root)

    def isValidBSTRec(
        self, node, low_boundary=float("-inf"), high_boundary=float("inf")
    ):
        if not node:
            return True

        if (
            (node.val > low_boundary and node.val < high_boundary)
            and self.isValidBSTRec(node.left, low_boundary, node.val)
            and self.isValidBSTRec(node.right, node.val, high_boundary)
        ):
            return True

        return False


node = TreeNode(5)
node.left = TreeNode(2)
node.right = TreeNode(8)

print(Solution().isValidBST(node))

node.left.left = TreeNode(6)

print(Solution().isValidBST(node))
