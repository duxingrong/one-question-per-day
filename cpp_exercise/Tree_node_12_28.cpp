/*
翻转二叉树
*/

// 首先重点关注递归法,反而是因为太简单了，所以每次记不住

// 前序遍历和后序遍历都可以,也就是先处理还是先遍历的关系

#include <cstddef>
#include <deque>
#include <stack>
#include <vector>
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
  TreeNode *invertTree(TreeNode *root) {
    // 终止条件
    if (root == NULL)
      return root;
    // 前序遍历
    swap(root->left, root->right);
    invertTree(root->left);
    invertTree(root->right);
    return root;
  }
};

class Solution {
public:
  TreeNode *invertTree(TreeNode *root) {
    // 终止条件
    if (root == NULL)
      return root;
    // 后序遍历
    invertTree(root->left);
    invertTree(root->right);
    swap(root->left, root->right);
    return root;
  }
};

class Solution {
public:
  TreeNode *invertTree(TreeNode *root) {
    // 终止条件
    if (root == NULL)
      return root;
    // 中序遍历
    invertTree(root->left);
    swap(root->left, root->right);
    invertTree(root->left); // 因为交换了，所以之前的右边又来到了左边
    return root;
  }
};

// 统一的迭代法,这样不同的遍历顺序只需要修改几行代码
class Solution {
public:
  TreeNode *invertTree(TreeNode *root) {
    if (root == NULL)
      return root;
    stack<TreeNode *> st;
    st.push(root);
    while (!st.empty()) {
      TreeNode *cur = st.top();
      if (cur != NULL) {
        st.pop();
        if (cur->right)
          st.push(cur->right);
        st.push(cur);
        st.push(NULL);
        if (cur->left)
          st.push(cur->left);
      } else {
        st.pop();
        TreeNode *cur = st.top();
        st.pop();
        swap(cur->left, cur->right);
      }
    }
    return root;
  }
};
