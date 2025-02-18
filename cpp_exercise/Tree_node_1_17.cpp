/*
 将有序数组转换成高度平衡的二叉搜索树
 本题目中，一个高度平衡的二叉树是指一个二叉树每个节点的左右两个子树的高度差的相对值不超过1

 这里唯一要注意的是，用下标来缩短数组，而不是重复的构造新的数组

*/

#include <cstddef>
#include <vector>
using namespace std;

struct TreeNode {
  int val;
  TreeNode *left;
  TreeNode *right;
  TreeNode(int data) : val(data), left(NULL), right(NULL){};
};

class Solution {
private:
  TreeNode *dfs(vector<int> &nums, int left, int right) {
    if (left > right)
      return NULL;
    int mid = left + ((right - left) / 2);
    TreeNode *root = new TreeNode(nums[mid]);
    root->left = dfs(nums, left, mid - 1);
    root->right = dfs(nums, mid + 1, right);
    return root;
  }

public:
  TreeNode *sortedArrayToBST(vector<int> &nums) {
    TreeNode *root = dfs(nums, 0, nums.size() - 1);
    return root;
  }
};
