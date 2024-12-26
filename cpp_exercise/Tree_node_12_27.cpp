/*
二叉树的最小深度
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

// 迭代法
class Solution {
public:
  int minDepth(TreeNode *root) {
    int result = 0;
    if (root == NULL)
      return result;
    deque<TreeNode *> que;
    que.push_back(root);
    while (!que.empty()) {
      int length = que.size();
      for (int i = 0; i < length; i++) {
        TreeNode *node = que.front();
        que.pop_front();
        if (node->left == NULL && node->right == NULL)
          return result + 1;
        if (node->left)
          que.push_back(node->left);
        if (node->right)
          que.push_back(node->right);
      }
      result += 1;
    }
    return result;
  }
};

// 递归法
class Solution {
public:
  int minDepth(TreeNode *root) {
    // 终止条件
    if (root == NULL)
      return 0;

    // 这里还需要考虑只有一边有孩子
    if (root->left && root->right == NULL)
      return minDepth(root->left) + 1;

    if (root->left == NULL && root->right)
      return minDepth(root->right) + 1;

    int left = minDepth(root->left);
    int right = minDepth(root->right);
    return min(left, right) + 1;
  }
};
