# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        vals = []
        self.helper3(root, vals)
        return max(vals)
    def helper3(self, root, vals):
        if root is None: 
            return 
        else: 
            self.helper2(root, vals)
            self.helper2(root.left, vals)
            self.helper2(root.right, vals)

        

    def helper2(self, root, maxValues):
        if root is None: 
            return
        else: 
            valuesLeft = []
            self.helper(root.left, 0, valuesLeft)
            leftDeep = valuesLeft[0]
            valuesRight = []
            self.helper(root.right, 0, valuesRight)
            rightDeep = valuesRight[0]
            maxValues.append(leftDeep+rightDeep)

    def helper(self, root, curr, maxValue):
        if root is None: 
            if len(maxValue) <= 0: 
                maxValue.append(curr)
            else: 
                if curr > maxValue[0]:
                    maxValue[0] = curr
        else: 
            self.helper(root.left, curr+1, maxValue) 
            self.helper(root.right, curr+1, maxValue)
