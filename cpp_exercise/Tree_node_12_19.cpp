/*
二叉树的层序遍历

返回结果[
[3],
[9,20],
[15,7]
]
*/

#include <cstddef>
#include <deque>
#include <vector>
using namespace std;

struct TreeNode {
  int val;
  TreeNode *left;
  TreeNode *right;
  TreeNode(int data) : val(data), left(NULL), right(NULL) {}
};

// 迭代法 :python中for 循环开始了次数就不会变，但是c++是会变化的
class Solution {
public:
  vector<vector<int>> levelOrder(TreeNode *root) {
    vector<vector<int>> result;
    if (root == NULL)
      return result;
    deque<TreeNode *> que;
    que.push_back(root);

    while (!que.empty()) {
      vector<int> level;
      int size = que.size();
      for (int i = 0; i < size; i++) {
        TreeNode *node = que.front();
        level.push_back(node->val);
        que.pop_front();
        if (node->left)
          que.push_back(node->left);
        if (node->right)
          que.push_back(node->right);
      }
      result.push_back(level);
    }
    return result;
  }
};

// 递归法:中左右
class Solution {
public:
  vector<vector<int>> levelOrder(TreeNode *root) {
    vector<vector<int>> result;
    if (root == NULL)
      return result;
    dfs(root, 0, result);

    return result;
  }

private:
  void dfs(TreeNode *node, int depth,
           vector<vector<int>> &result) { // 一定要记得是引用传递
    if (node == NULL)
      return;

    // 中
    if (result.size() == depth) {
      result.push_back(vector<int>());
    }
    result[depth].push_back(node->val);

    // 左右
    if (node->left)
      dfs(node->left, depth + 1, result);
    if (node->right)
      dfs(node->right, depth + 1, result);
  }
};
