/*
二叉树的最大深度

给定一个二叉树,找出其最大的深度

二叉树的深度为根节点到最远的叶子节点的最长路径上的节点数

说明:叶子节点是指没有子节点的节点
*/

//迭代法
#include <deque>
#include <cstddef>
using namespace std;

struct TreeNode{
    int val;
    TreeNode*left;
    TreeNode*right;
    TreeNode(int data):val(data),left(NULL),right(NULL){}
};

class Solution{
public:
    int maxDepth(TreeNode*root){
        int result=0;
        if (root==NULL) return result;
        deque<TreeNode*> que;
        que.push_back(root);
        while (!que.empty()){
            int length = que.size();
            result +=1;
            for (int i=0;i<length;i++){
                TreeNode*node = que.front();
                que.pop_front();
                if (node->left) que.push_back(node->left);
                if (node->right)que.push_back(node->right);
            } 
        }
        return result;
    }
};

//递归法
//每个节点的高度,等于左右孩子高度的最大值+1
//空节点的高度为0
class Solution{
public:
    int maxDepth(TreeNode*root){
        //空节点的高度为0
        if(root==NULL) return 0;

        //单层逻辑
        int left = maxDepth(root->left);
        int right = maxDepth(root->right);
        return max(left,right)+1 ;
    }

};