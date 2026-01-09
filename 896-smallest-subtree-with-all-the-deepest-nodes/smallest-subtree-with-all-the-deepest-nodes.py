class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        
        def dfs(node):
            # Base case: null nodes have depth 0
            if not node:
                return 0, None
            
            left_depth, left_node = dfs(node.left)
            right_depth, right_node = dfs(node.right)
            
            # If left is deeper, the deepest nodes are on the left
            if left_depth > right_depth:
                return left_depth + 1, left_node
            
            # If right is deeper, the deepest nodes are on the right
            if right_depth > left_depth:
                return right_depth + 1, right_node
            
            # If depths are equal, this node is the LCA of the deepest nodes
            return left_depth + 1, node

        return dfs(root)[1]