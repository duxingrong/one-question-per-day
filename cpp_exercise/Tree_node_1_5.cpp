/*

从中序与后序遍历序列构造二叉树

根据一棵树的中序遍历和后序遍历构造二叉树

注意:你可以假设树中没有重复的元素

*/
#include <cstddef>
#include <vector>

using namespace std;

struct TreeNode {
  int val;
  TreeNode *left;
  TreeNode *right;
  TreeNode(int data) : val(data), left(NULL), right(NULL) {}
};

// 采用递归,通过后续遍历得到头节点,然后分成两个子数组,递归去构建二叉树

class Solution {
public:
  TreeNode *buildTree(vector<int> &inorder, vector<int> &postorder) {
    // 特殊情况
    if (postorder.size() == 0 || inorder.size() == 0)
      return NULL;

    // 只要后续数组有值,那么后序数组的最后一个元素就是当前层的节点
    int rootVal = postorder[postorder.size() - 1];
    TreeNode *root = new TreeNode(rootVal);

    // 深搜到叶子节点,也就是数组长度万为1的时候,不用继续构造了
    if (postorder.size() == 1)
      return root;

    // 如果后序数组还有,那就根据这个节点来分割中序数组和后序数组
    int index;
    for (int i = 0; i < inorder.size(); i++) {
      if (inorder[i] == rootVal) {
        index = i;
        break;
      }
    }
    // 切割 inorder 和 postorder 数组
    vector<int> left_inorder(inorder.begin(), inorder.begin() + index);
    vector<int> right_inorder(inorder.begin() + index + 1, inorder.end());

    // post丢掉末尾
    postorder.resize(postorder.size() - 1);

    vector<int> left_postorder(postorder.begin(),
                               postorder.begin() + left_inorder.size());

    vector<int> right_postorder(postorder.begin() + left_inorder.size(),
                                postorder.end());
    // 递归构建左右子树
    root->left = buildTree(left_inorder, left_postorder);
    root->right = buildTree(right_inorder, right_postorder);

    return root;
  }
};
