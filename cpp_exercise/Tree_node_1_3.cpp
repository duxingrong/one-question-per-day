/*

找树左下角的值
给定一个二叉树,在树的最后一行找到最左边的值

如何判断你找到了树最后一行左下角的值

 */

#include <cstddef>
#include <deque>
using namespace std;

struct TreeNode {
  int val;
  TreeNode *left;
  TreeNode *right;
  TreeNode(int data) : val(data), left(NULL), right(NULL) {}
};

// 迭代法,我们一直更新第一个值就好了
class Solution {
public:
  int findBottomLeftValue(TreeNode *root) {
    deque<TreeNode *> que;
    que.push_back(root);
    int result = 0;
    while (!que.empty()) {
      int size = que.size();
      for (int i = 0; i < size; i++) {
        TreeNode *node = que.front();
        que.pop_front();
        if (i == 0)
          result = node->val;
        if (node->left)
          que.push_back(node->left);
        if (node->right)
          que.push_back(node->right);
      }
    }
    return result;
  }
};

// 递归就是深搜,要找到最后一行的最左边的节点,也就是不断深搜,始终保持左边优先,更新深度和最左边的值
class Solution {
public:
  int result;              // 全局变量,记录最左边的值
  int max_depth = INT_MIN; // 记录最大深度,全局变量

  void dfs(TreeNode *node, int depth) {
    // 终止条件
    if (node->left == NULL && node->right == NULL) {
      if (depth > max_depth) {
        max_depth = depth;
        result = node->val;
      }
    }
    // 始终左边优先
    if (node->left) {
      depth++;
      dfs(node->left, depth);
      depth--;
    }
    if (node->right) {
      depth++;
      dfs(node->right, depth);
      depth--;
    }
  }
  int findBottomLeftValue(TreeNode *root) {
    dfs(root, 0);
    return result;
  }
};
