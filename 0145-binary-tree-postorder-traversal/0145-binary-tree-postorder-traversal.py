# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        def preorder(root):
            if root is None: return
            preorder(root.left)
            preorder(root.right)
            result.append(root.val)
        preorder(root)
        return result 
        