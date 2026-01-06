# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        # Initialize queue for BFS (Level Order Traversal)
        queue = deque([root])
        
        # max_sum is initialized to -infinity to handle negative node values
        max_sum = float('-inf')
        max_level_idx = 1
        current_level_idx = 1
        
        while queue:
            level_sum = 0
            # Number of nodes at the current level
            nodes_at_level = len(queue)
            
            # Process all nodes at this specific level
            for _ in range(nodes_at_level):
                node = queue.popleft()
                level_sum += node.val
                
                # Add children for the next level
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            # If current level's sum is strictly greater than max_sum, update
            # This handles the "smallest level x" requirement automatically
            if level_sum > max_sum:
                max_sum = level_sum
                max_level_idx = current_level_idx
            
            # Increment level index for the next iteration
            current_level_idx += 1
            
        return max_level_idx
        