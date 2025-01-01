/*

左叶子之和

计算给定二叉树的所有左叶子之和

首先明白左叶子是什么?是cur->left并且cur->left的左右孩子为空,那么cur->left就是左孩子

*/

#include <cstddef>
#include <stack>
using namespace std;

struct TreeNode {
  int val;
  TreeNode *left;
  TreeNode *right;
  TreeNode(int data) : val(data), left(NULL), right(NULL) {}
};

// 一般有值的返回都是后序,这样才能累加
class Solution {
public:
  int sumOfLeftLeaves(TreeNode *root) {
    // 终止条件
    if (root == NULL)
      return 0;
    // 收获结果的程式
    int Val = 0;
    if (root->left && !root->left->left && !root->left->right)
      Val = root->left->val;

    int leftVal = sumOfLeftLeaves(root->left);
    int rightVal = sumOfLeftLeaves(root->right);
    return leftVal + rightVal + Val;
  }
};

// 迭代法更不用说了,直接前序解决
class Solution {
public:
  int sumOfLeftLeaves(TreeNode *root) {
    // 特殊情况
    if (root == NULL)
      return 0;
    stack<TreeNode *> st;
    st.push(root);
    int result = 0;
    while (!st.empty()) {
      TreeNode *node = st.top();
      st.pop();
      if (node->left && !node->left->left && !node->left->right)
        result += node->left->val;
      if (node->right)
        st.push(node->right);
      if (node->left)
        st.push(node->left);
    }
    return result;
  }
};
