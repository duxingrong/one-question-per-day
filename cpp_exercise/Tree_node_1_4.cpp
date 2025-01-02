/*
路径总和

给定一个二叉和一个目标和，判断该树中是否存在根节点到叶子节点的路径,这条路径上的所有节点值相加等于目标和

这道题目是找到就能返回

*/

#include <cstddef>

struct TreeNode {
  int val;
  TreeNode *left;
  TreeNode *right;
  TreeNode(int data) : val(data), left(NULL), right(NULL) {}
};

// 直接用递归,后续遍历,到叶子节点收获结果
// 这里不需要回溯，因为每次传下去的是新的值，这样的话每当回到该层的时候,也会自动恢复成上一层的值
class Solution {
public:
  bool hasPathSum(TreeNode *root, int sum) {
    if (root == NULL)
      return false;
    return dfs(root, sum);
  }

  bool dfs(TreeNode *node, int count) {
    // 终止条件
    if (!node->left && !node->right)
      return count == node->val;

    // 不断下到最底层
    count -= node->val;
    if (node->left && dfs(node->left, count))
      return true; // 为真的话，就一直返回true
    if (node->right && dfs(node->right, count))
      return true;

    return false;
  }
};
