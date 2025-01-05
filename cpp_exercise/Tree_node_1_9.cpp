/*

验证二叉搜索树

给定一个二叉树,判断其是否是一个有效的二叉搜索树

假设一个二叉搜索树具有如下特征:
- 节点的左子树只包含小于当前节点的数
- 节点的右子树只包含大于当前节点的数
- 所有左子树和右子树自身必须也是二叉搜索树

这道题目的重点在于要维护一个全局的变量,min
和max,并不是简单的看单个节点满足左<中<右即可

*/
#include <climits>
#include <cstddef>

struct TreeNode {
  int val;
  TreeNode *left;
  TreeNode *right;
  TreeNode(int data) : val(data), left(NULL), right(NULL) {}
};

class Solution {
public:
  bool isValidBST(TreeNode *root) {
    // 巧妙的维护一个全局的范围
    return dfs(root, LONG_MIN, LONG_MAX);
  }

private:
  bool dfs(TreeNode *node, long min, long max) {
    // 前序,先判断当前节点,然后再递归去判断左右节点
    if (node == NULL)
      return true;

    // 如果节点不在范围内,就out
    if (node->val <= min || node->val >= max) {
      return false;
    }

    return dfs(node->left, min, node->val) && dfs(node->right, node->val, max);
  }
};
