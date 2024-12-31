/*
二叉树的所有路径

给定一个二叉树，返回所有从根节点到叶子节点的路径

说明: 叶子节点是指没有子节点的节点

*/

#include <cstddef>
#include <string>
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
  vector<string> binaryTreePaths(TreeNode *root) {
    vector<string> result;
    vector<int> path;
    // 特殊情况
    if (root == NULL)
      return result;
    dfs(root, path, result);
    return result;
  }

private:
  void dfs(TreeNode *root, vector<int> &path, vector<string> &result) {

    path.push_back(root->val);
    // 终止条件也是收获结果
    if (root->left == NULL && root->right == NULL) {
      string sPath;
      for (int i = 0; i < path.size(); i++) {
        sPath += to_string(path[i]);
        if (i != path.size() - 1)
          sPath += "->";
      }
      result.push_back(sPath);
    }

    // 单层逻辑
    if (root->left) {
      dfs(root->left, path, result);
      path.pop_back(); // 回溯
    }
    if (root->right) {
      dfs(root->right, path, result);
      path.pop_back(); // 回溯
    }
  }
};
