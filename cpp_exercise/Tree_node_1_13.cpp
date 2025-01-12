/*
二叉搜索树的最近公共祖先

给定一个二叉搜索树，找到该树中两个指定的最近公共祖先

最近公共祖先的定义为:"对于有根树T的两个节点p,q,最近公共祖先表示为一个结点x,满足x是p,q的祖先且x的深度尽可能大(一个结点也可以是自己的祖先)"


这里要理解我们从上往下遍历，遇到第一个cur在[p,q]内的话，那它就是最近的公共祖先，因为我们再往左范围就是[q,cur]，向右就是[cur,q]，都一定会错过另一个，所以第一次遇见的就是最近公共祖先

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

    if (root->val > p->val && root->val > q->val) {
      return lowestCommonAncestor(root->left, p, q);
    } else if (root->val < p->val && root->val < q->val) {
      return lowestCommonAncestor(root->right, p, q);
    } else {
      return root;
    }
  }
};
