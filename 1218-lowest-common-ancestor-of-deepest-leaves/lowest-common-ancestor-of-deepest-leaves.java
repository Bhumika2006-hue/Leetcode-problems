class Solution {
    // Helper class to return two values from the recursion
    class Result {
        TreeNode node;
        int depth;
        Result(TreeNode node, int depth) {
            this.node = node;
            this.depth = depth;
        }
    }

    public TreeNode lcaDeepestLeaves(TreeNode root) {
        return getLCA(root).node;
    }

    private Result getLCA(TreeNode node) {
        if (node == null) {
            return new Result(null, 0);
        }

        Result left = getLCA(node.left);
        Result right = getLCA(node.right);

        // Case 1: Left is deeper
        if (left.depth > right.depth) {
            return new Result(left.node, left.depth + 1);
        } 
        // Case 2: Right is deeper
        else if (right.depth > left.depth) {
            return new Result(right.node, right.depth + 1);
        } 
        // Case 3: Depths are equal - this node is the current LCA
        else {
            return new Result(node, left.depth + 1);
        }
    }
}