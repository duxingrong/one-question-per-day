/*
二叉搜索树中的众数

给定一个有相同值的二叉搜索树(BST)，找出BST中的所有众数(出现频率最高的元素)

假定BST有如下定义:
- 结点左子树中所含节点的值小于等于当前结点的值
- 结点右子树中所含结点的值大于等于当前结点的值
- 左子树和右子树都是二叉搜索树

*/
#include <climits>
#include <cstddef>
#include <vector>
using namespace std;

struct TreeNode {
  int val;
  TreeNode *left;
  TreeNode *right;
  TreeNode(int data) : val(data), left(NULL), right(NULL) {}
};

// 二叉搜索树的特性就是想等的肯定就是连续的，所以也可以用pre 和cur来看

class Solution {
  vector<int> result;
  int count = 0;
  int maxcount = INT_MIN;
  TreeNode *pre = NULL;

public:
  vector<int> findMode(TreeNode *root) {
    // 更新值，保证每次从头开始
    pre = NULL;
    count = 0;
    maxcount = INT_MIN;
    result.clear();
    dfs(root);
    return result;
  }

private:
  void dfs(TreeNode *root) {
    // 空结点返回
    if (root == NULL)
      return;

    // 先到最左边
    dfs(root->left);

    if (pre == NULL) {
      count = 1; // 说明这是第一个值
    } else if (pre->val == root->val) {
      count++;
    } else {
      count = 1;
    }
    pre = root;
    if (count == maxcount) {
      result.push_back(root->val);
    } else if (count > maxcount) {
      maxcount = count;
      result.clear();
      result.push_back(root->val);
    }
    dfs(root->right);
  }
};
