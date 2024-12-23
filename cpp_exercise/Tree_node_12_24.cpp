/*

在每个树行中找最大值

你需要在二叉树的没一行中找到最大的值

 */

#include <climits>
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
  vector<int> largestValues(TreeNode *root) {
    vector<int> result;
    if (root == NULL)
      return result;
    deque<TreeNode *> que;
    que.push_back(root);
    while (!que.empty()) {
      int length = que.size();
      int max = INT_MIN;
      for (int i = 0; i < length; i++) {
        TreeNode *node = que.front();
        que.pop_front();
        if (max < node->val)
          max = node->val;
        if (node->left)
          que.push_back(node->left);
        if (node->right)
          que.push_back(node->right);
      }
      result.push_back(max);
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
  vector<int> result = obj.largestValues(root);
  for (const int val : result) {
    cout << val << " ";
  }
}
