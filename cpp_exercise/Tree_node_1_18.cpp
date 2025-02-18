/*

把二叉搜索树转换成累加树

给出二叉搜索树的根节点，该树的节点值各不相同，请你根据其转换为累加树(Greater Sum
Tree),使每个节点node的新值等于原树中大于或等于node.val的值之和

提醒一下，二叉搜索树满足下列约束条件:
节点的左子树仅包含健小于节点健的节点。节点的右子树仅包含大于节点健的节点。左右子树也必须是二叉搜索树.

*/
#include <cstddef>
struct TreeNode {
  int val;
  TreeNode *left;
  TreeNode *right;
  TreeNode(int data) : val(data), left(NULL), right(NULL) {}
};

class Solution {
private:
  int pre = 0;
  void dfs(TreeNode *cur) {
    if (cur == NULL)
      return;
    dfs(cur->right); //首先去到最右边
    cur->val += pre;
    pre = cur->val;
    dfs(cur->left);
  }

public:
  TreeNode *convertBST(TreeNode *root) {
    pre = 0; //保证不受前面一次的影响
    dfs(root);
    return root;
  }
};
