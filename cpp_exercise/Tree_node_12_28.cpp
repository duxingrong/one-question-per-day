/*
翻转二叉树
*/

//首先重点关注递归法,反而是因为太简单了，所以每次记不住

//前序遍历和后序遍历都可以,也就是先处理还是先遍历的关系


#include <cstddef>
#include <deque>
#include <vector>
using namespace std;

struct TreeNode{
    int val;
    TreeNode*left;
    TreeNode*right;
    TreeNode(int data) : val(data),left(NULL),right(NULL) {}
};