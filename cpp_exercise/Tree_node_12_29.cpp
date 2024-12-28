/*
对称二叉树

给定一个二叉树, 检查它是否是镜像对称的

二叉树是否对称，其实是比较左右子树

*/

#include <cstddef>
using namespace std;

struct TreeNode {
  int val;
  TreeNode *left;
  TreeNode *right;
  TreeNode(int data) : val(data), left(NULL), right(NULL) {}
};

// 递归法
class Solution {
public:
  bool isSymmetric(TreeNode *root) {
    if (root == NULL)
      return true;
    bool result = dfs(root->left, root->right);
    return result;
  }

  bool dfs(TreeNode *left, TreeNode *right) {

    if (left == NULL && right == NULL)
      return true;
    if (left == NULL || right == NULL)
      return false;
    if (left->val != right->val)
      return false;

    bool left_val = dfs(left->left, right->right);
    bool right_val = dfs(left->right, right->left);
    return left_val && right_val;
  }
};

// 迭代法
#include <stack>
class Solution {
public:
  bool isSymmetric(TreeNode *root) {
    if (root == NULL)
      return true;

    stack<pair<TreeNode *, TreeNode *>> st;
    st.push({root->left, root->right});

    while (!st.empty()) {
      auto [left, right] = st.top();
      st.pop();

      // 如果左节点和右节点都为空，则跳过这对节点
      if (left == NULL && right == NULL) {
        continue;
      }

      // 如果只有一个为空，或者值不相等，返回 false
      if (left == NULL || right == NULL || left->val != right->val) {
        return false;
      }

      // 将对称的子节点入栈
      st.push({left->left, right->right});
      st.push({left->right, right->left});
    }

    return true;
  }
};
