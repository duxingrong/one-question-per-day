/*
二叉树的层序遍历||

返回其节点值自底向上的层次遍历(从叶子节点到根节点)

就是反转一下
 */
#include <algorithm>
#include <cstddef>
#include <deque>
#include <iostream>
#include <vector>
using namespace std;

struct TreeNode {
  int val;
  TreeNode *left;
  TreeNode *right;
  TreeNode(int data) : val(data), left(NULL), right(NULL) {}
};

class Solution {
public:
  vector<vector<int>> levelOrderBottom(TreeNode *root) {
    // 迭代法
    vector<vector<int>> result;
    if (root == NULL)
      return result;
    deque<TreeNode *> que;
    que.push_back(root);
    while (!que.empty()) {
      vector<int> level;
      int len = que.size();
      for (int i = 0; i < len; i++) {
        TreeNode *node = que.front();
        que.pop_front();
        level.push_back(node->val);
        if (node->left)
          que.push_back(node->left);
        if (node->right)
          que.push_back(node->right);
      }
      result.push_back(level);
    }
    reverse(result.begin(), result.end());
    return result;
  }

  // 递归法
  vector<vector<int>> levelOrderBottom1(TreeNode *root) {
    vector<vector<int>> result;
    if (root == NULL)
      return result;
    dfs(root, 0, result);
    reverse(result.begin(), result.end());
    return result;
  }

  void dfs(TreeNode *node, int depth,
           vector<vector<int>> &result) { // 不要忘记引用
    if (depth == result.size()) {
      result.push_back(vector<int>());
    }
    result[depth].push_back(node->val);
    if (node->left)
      dfs(node->left, depth + 1, result);
    if (node->right)
      dfs(node->right, depth + 1, result);
  }
};

int main() {
  TreeNode *root = new TreeNode(1);
  root->left = new TreeNode(2);
  root->right = new TreeNode(3);
  root->left->left = new TreeNode(4);
  root->left->right = new TreeNode(5);
  root->right->left = new TreeNode(6);
  root->right->right = new TreeNode(7);
  Solution obj;
  vector<vector<int>> result = obj.levelOrderBottom1(root);
  for (const vector<int> nums : result) {
    for (const int val : nums) {
      cout << val << " ";
    }
    cout << endl;
  }
}
