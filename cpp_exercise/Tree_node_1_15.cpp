/*
删除二叉搜索树中的节点

给定一个二叉搜索树的根节点root和一个值key,删除二叉搜索树中的key对应的节点，并保证二叉搜索树的性质不变。返回二叉搜索树(有可能被更新)的根节点的引用

一般来说:删除节点可分成两个步骤:

首先找到需要删除的节点；如果找到了，删除它

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
  TreeNode *deleteNode(TreeNode *root, int key) {
    dfs(root, key);
    return root;
  }

private:
  void dfs(TreeNode *&root, int key) {
    // 如果为空，返回
    if (root == NULL)
      return;
    // 首先从上往下去找到key
    if (root->val > key) {
      dfs(root->left, key);
    } else if (root->val < key) {
      dfs(root->right, key);
    } else {
      // 找到了
      if (root->left != NULL && root->right != NULL) {
        TreeNode *cur = root->left;
        while (cur->right != NULL) {
          cur = cur->right;
        }
        cur->right = root->right;
        root = root->left;
      } else if (root->left == NULL && root->right != NULL) {
        root = root->right;
      } else if (root->left != NULL && root->right == NULL) {
        root = root->left;
      } else {
        root = NULL;
      }
    }
  }
};
