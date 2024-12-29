/*
完全二叉树的节点个数

 */

#include <cstddef>
#include <iostream>
using namespace std;

struct TreeNode {
  int val;
  TreeNode *left;
  TreeNode *right;
  TreeNode(int data) : val(data), left(NULL), right(NULL) {}
};

// 如果是一个普通的二叉树
class Solution {
public:
  // 递归
  // 现在由于是一个完全二叉树,我们可以利用它存在满二叉树来节约遍历
  // 如果一个节点向左深搜和向右深搜的深度一样,那就可以保证是满二叉树,因为整体是完全二叉树

  int countNodes(TreeNode *root) {

    if (root == NULL)
      return 0;
    TreeNode *left = root->left;
    TreeNode *right = root->right;
    int leftdepth, rightdepth = 0;
    // 通过深度是否一致来进行减枝
    while (left) {
      left = left->left;
      leftdepth += 1;
    }

    while (right) {
      right = right->right;
      rightdepth += 1;
    }

    if (leftdepth == rightdepth)
      return (2 << leftdepth) - 1; // 2<<1相当于2^2

    int leftnum = countNodes(root->left);
    int rightnum = countNodes(root->right);

    return leftnum + rightnum + 1;
  }
};

int main() {
  TreeNode *root = new TreeNode(1);
  root->left = new TreeNode(1);
  root->right = new TreeNode(2);
  root->left->left = new TreeNode(3);
  root->left->right = new TreeNode(4);
  Solution obj;
  int result = obj.countNodes(root);
  cout << result << endl;
}
