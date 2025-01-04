/*

合并二叉树

给定两个二叉树,想象当你将它们中的一个覆盖到另一个上时,两个二叉树的一些点便会重叠

你需要将他们合并为一个新的二叉树,合并的规则是如果两个节点重合,那么将他们的值相加作为节点合并后的新值,否则不为NULL的节点将直接作为新二叉树的节点


一共有几种情况,
1. 两边节点都为空,return NULL
2. 两边节点有一个为空, return 不为空的那个
3. 两边节点都不为空, 那就返回1+2

这里能进入递归的前提就是他两都不为空,不论是何种遍历方式,都是如此

*/

#include <cstddef>
using namespace std;

// 前序遍历更清除一些
struct TreeNode {
  int val;
  TreeNode *left;
  TreeNode *right;
  TreeNode(int data) : val(data), left(NULL), right(NULL) {}
};

class Solution {
public:
  TreeNode *mergeTrees(TreeNode *t1, TreeNode *t2) {
    // 终止条件
    if (t1 == NULL)
      return t2;
    if (t2 == NULL)
      return t1;
    // 只有当两个都有值,才进入递归,其他顺序就是改变这三行代码
    t1->val += t2->val;                           // 中
    t1->left = mergeTrees(t1->left, t2->left);    // 左
    t1->right = mergeTrees(t1->right, t2->right); // 右

    return t1;
  }
};
