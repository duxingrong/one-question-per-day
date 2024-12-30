/*
平衡二叉树

给定一个二叉树,判断它是否是高度平衡的二叉树

本题中,一个高度平衡的二叉树定义为:一个二叉树每个节点的左右两个子树的高度不超过1

 */

#include <cstddef>
#include <iostream>
#include <stack>
using namespace std;

struct TreeNode {
  int val;
  TreeNode *left;
  TreeNode *right;
  TreeNode(int data) : val(data), left(NULL), right(NULL) {}
};

// 递归
class Solution {
public:
  bool isBalanced(TreeNode *root) {
    if (root == NULL)
      return true;
    int result = dfs(root);
    if (result == -1)
      return false;
    else
      return true;
  }

private:
  // 这里可以用-1代表已经不满足了,其余的情况就是求高度
  int dfs(TreeNode *root) {
    // 空节点返回0
    if (root == NULL)
      return 0;

    int left = dfs(root->left);
    int right = dfs(root->right);
    // 代表从底层返回的值已经发现了不满足,那就继续返回-1
    if (left == -1 || right == -1 || abs(left - right) > 1)
      return -1;

    return 1 + max(left, right); // 满足就继续返回高度
  }
};

// 迭代法
// 先定义一个函数,专门用来求高度
// 这个函数通过栈模拟的后续遍历找每一个节点的高度(其实是通过求传入节点为根节点的最大深度来求的高度)

class Solution {
private:
  int getDepth(TreeNode *cur) {
    if (cur == NULL)
      return 0;
    stack<TreeNode *> st;
    st.push(cur);
    int result = 0; // 记录最大深度
    int depth = 0;  // 记录深度
    while (!st.empty()) {
      TreeNode *cur = st.top();
      if (cur != NULL) {
        st.push(NULL);
        depth++;
        if (cur->right)
          st.push(cur->right);
        if (cur->left)
          st.push(cur->left);
      } else {
        st.pop();
        st.pop();
        depth--;
      }
      result = result > depth ? result : depth;
    }
    return result;
  }

public:
  bool isBalanced(TreeNode *root) {
    stack<TreeNode *> st;
    if (root == NULL)
      return true;
    st.push(root);
    while (!st.empty()) {
      TreeNode *node = st.top();
      st.pop();
      if (abs(getDepth(node->left) - getDepth(node->right)) > 1)
        return false;
      if (node->left)
        st.push(node->left);
      if (node->right)
        st.push(node->right);
    }
    return true;
  }
};
