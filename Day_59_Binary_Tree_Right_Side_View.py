# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        def dfs(node,depth,result):
            if not node:
                return
            if depth==len(result):
                result.append(node.val)
            dfs(node.right,depth+1,result)
            dfs(node.left,depth+1,result)
        result=[]
        dfs(root,0,result)
        return result
        
