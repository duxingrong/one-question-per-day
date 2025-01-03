/*
最大二叉树

给定一个不含有重复元素的整数树组,一个以此数组构建的最大二叉树定义如下:

- 二叉树的根是数组中的最大元素
- 左子树是通过数组中最大值左边部分构造出的最大二叉树
- 右子树是通过数组中最大值右边部分构造出的最大儿叉树

通过给定的数组构建最大二叉树,并且输出这个树的根节点
*/
#include <algorithm>
#include <cstddef>
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
  TreeNode *constructMaximumBinaryTree(vector<int> &nums) {
    // 空了直接返回
    if (nums.size() == 0)
      return NULL;

    // 找到最大值
    int maxVal = *max_element(nums.begin(), nums.end());
    TreeNode *root = new TreeNode(maxVal);

    // 如果长度为1,那直接返回就好了
    if (nums.size() == 1)
      return root;

    // 分开数组
    int index;
    for (index = 0; index < nums.size(); index++) {
      if (nums[index] == maxVal)
        break;
    }

    vector<int> left_nums(nums.begin(), nums.begin() + index);
    vector<int> right_nums(nums.begin() + index + 1, nums.end());

    root->left = constructMaximumBinaryTree(left_nums);
    root->right = constructMaximumBinaryTree(right_nums);

    return root;
  }
};
