# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        subtree_sums = []

        # Helper function to calculate sum of subtrees and store them
        def calculate_sum(node):
            if not node:
                return 0
            
            # Post-order traversal: sum = left_child_sum + right_child_sum + current_val
            current_sum = calculate_sum(node.left) + calculate_sum(node.right) + node.val
            subtree_sums.append(current_sum)
            return current_sum

        # 1. Get the total sum of the tree
        total_sum = calculate_sum(root)
        
        # 2. Iterate through all recorded subtree sums to find max product
        max_prod = 0
        for s in subtree_sums:
            # product = (sum of one part) * (sum of the other part)
            product = s * (total_sum - s)
            if product > max_prod:
                max_prod = product
        
        return max_prod % (10**9 + 7)
        