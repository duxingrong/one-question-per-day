/*
修剪二叉搜索树

给定一个二叉搜索树，同时给定最小边界L和最大边界R。通过修建二叉搜索树，使得所有节点的值在[L,R]中(R>=L)。你可能需要改变树的根节点，所以结果应当返回修剪好的二叉树的新的根节点

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
  TreeNode *trimBST(TreeNode *root, int low, int high) {
    //空节点，直接返回
    if (root == NULL)
      return NULL;
    //如果root->val<R,就是将右边的满足的节点返回充当root
    if (root->val < low)
      return trimBST(root->right, low, high);
    //如果root->val>L,就是将左边的满足的节点返回充当root
    if (root->val > high)
      return trimBST(root->left, low, high);
    //接收返回的值
    root->left = trimBST(root->left, low, high);
    root->right = trimBST(root->right, low, high);

    return root;
  }
};
