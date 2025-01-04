/*
二叉搜索树中的搜索

给定二叉搜索树(BST)的根节点和一个值,你需要在BST中找到节点值等于给定值的节点,返回以该节点为根的子树.如果节点不存在,则返回NULL

*/

#include <cstddef>
using namespace std;

struct TreeNode {
  int val;
  TreeNode *left;
  TreeNode *right;
  TreeNode(int data) : val(data), left(NULL), right(NULL) {}
};

class Solution {
public:
  TreeNode *searchBST(TreeNode *root, int val) {

    if (root == NULL)
      return NULL;

    if (root->val > val) {
      return searchBST(root->left, val);
    } else if (root->val < val) {
      return searchBST(root->right, val);
    } else {
      return root;
    }
  }
};
