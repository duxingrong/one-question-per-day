/*

二叉搜索树的最小绝对差

给你一棵所有节点为非负值的二叉搜索树,请你计算树中任意两个节点的差的绝对值的最小值

 */

// 注意这里是二叉搜索树,所以你用相邻的比较就行了

#include <algorithm>
#include <climits>
#include <cstddef>
using namespace std;

struct TreeNode {
  int val;
  TreeNode *left;
  TreeNode *right;
  TreeNode(int data) : val(data), left(NULL), right(NULL) {}
};

class Solution {
  int result = INT_MAX;
  TreeNode *pre = NULL;

public:
  int getMinimumDifference(TreeNode *root) {
    dfs(root);
    return result;
  }

private:
  void dfs(TreeNode *root) {
    // 终止条件
    if (root == NULL)
      return;
    dfs(root->left);
    if (pre != NULL) {
      result = min(result, root->val - pre->val);
    }

    pre = root;
    dfs(root->right);
  }
};
