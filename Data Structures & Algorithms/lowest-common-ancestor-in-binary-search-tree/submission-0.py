# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        def path(node: TreeNode, set_to_add: list, n: TreeNode):
            if node == None:
                return None
            set_to_add.append(node.val)
            if node.val < n.val:
                path(node.right, set_to_add, n)
            if node.val > n.val:
                path(node.left, set_to_add, n)
            
            return set_to_add
        
        set_to_p = path(root, [], p)
        set_to_q = path(root, [], q)

        similarities =[x for x in set_to_p if x in set_to_q]

        return TreeNode(similarities[-1])
            


