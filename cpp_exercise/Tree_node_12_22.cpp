/*
二叉树的层平均值

给定一个非空二叉树,返回一个由每层节点平均值组成的数组
*/

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
  vector<double> averageOfLevels(TreeNode *root) {
    // 特殊情况
    vector<double> result;
    if (root == NULL)
      return result;
    deque<TreeNode *> que;
    que.push_back(root);
    while (!que.empty()) {
      int length = que.size();
      double sum = 0;
      for (int i = 0; i < length; i++) {
        TreeNode *node = que.front();
        que.pop_front();
        sum += node->val;
        if (node->left)
          que.push_back(node->left);
        if (node->right)
          que.push_back(node->right);
      }
      result.push_back(sum / length);
    }
    return result;
  }
};

int main() {
  TreeNode *root = new TreeNode(3);
  root->left = new TreeNode(9);
  root->right = new TreeNode(20);
  root->right->left = new TreeNode(15);
  root->right->right = new TreeNode(7);
  Solution obj;
  vector<double> result = obj.averageOfLevels(root);
  for (const double val : result) {
    cout << val << " ";
  }
}
