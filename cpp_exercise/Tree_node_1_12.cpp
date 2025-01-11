/*

二叉树的最近公共祖先

给定一个二叉树，找到该树中两个指定节点的最近公共祖先。

百度百科中最近公共祖先的定义为:"对于有根树T的两个结点p,q,最近公共祖先表示为一个结点x,满足x是p,q的祖先且x的深度尽可能大(一个节点也可以是自己的祖先)"

两种情况:
1. 一个节点的左右两边刚好有pq,那它就是最近的,因为我们是后序遍历
2. 一个节点本身自己为pq,然后左右孩子中有一边有pq,

对于这两种情况，我们都可以用遇到pq，就返回
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
  TreeNode *lowestCommonAncestor(TreeNode *root, TreeNode *p, TreeNode *q) {
    // 如果遇到空节点或者pq,直接返回
    if (root == NULL || root == p || root == q) {
      return root;
    }
    // 左右
    TreeNode *left = lowestCommonAncestor(root->left, p, q);
    TreeNode *right = lowestCommonAncestor(root->right, p, q);

    if (left != NULL && right != NULL)
      return root;
    else if (left != NULL && right == NULL)
      return left;
    else if (left == NULL && right != NULL)
      return right;
    else {
      return NULL;
    }
  }
};
