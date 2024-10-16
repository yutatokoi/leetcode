/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
int sumOfLeftLeaves(struct TreeNode* root) {
    if (!root) {
        return 0;
    }   

    int ans = 0;

    if (root->left) {
        if (!root->left->left && !root->left->right) {
            ans += root->left->val;
        } else {
            ans += sumOfLeftLeaves(root->left);
        }
    }

    ans += sumOfLeftLeaves(root->right);

    return ans;
}
