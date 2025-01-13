/*
二叉搜索树中的插入操作

给定二叉搜索树(BST)的根节点和要插入树中的值，
将值插入二叉搜索树。返回插入后二叉搜索树的根节点。输入数据保证，新值和原始二叉搜索树中的任意节点值都不同

注意，可能存在多种有效的插入方式，只要树在插入后仍保持为二叉搜索树即可。

不会和树上的值想等，所以一定可以放在叶子节点吗？
那就简单了，直接根据范围递归，遇到空节点就放入

 */

#include <cstddef>

struct TreeNode {
  int val;
  TreeNode *left;
  TreeNode *right;
  TreeNode(int data) : val(data), left(NULL), right(NULL) {}
};

class Solution {
public:
  TreeNode *insertIntoBST(TreeNode *root, int val) {
    dfs(root, val);
    return root;
  }

private:
  void dfs(TreeNode *&root, int val) {
    // 空节点就是放入的时候
    if (root == NULL) {
      root = new TreeNode(val);
      return;
    }
    // 如果值比节点大，就要右递归
    if (root->val < val) {
      dfs(root->right, val);
    } else if (root->val > val) {
      dfs(root->left, val);
    }
  }
};
