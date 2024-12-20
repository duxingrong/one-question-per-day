/*
二叉树的右视图
给定一棵二叉树,想象自己站在它的右侧,按照从顶部到底部的顺序,
返回从右侧所能看到的节点值
*/

//用层序遍历就很简单,每次当i == size-1的时候,加入数组即可

#include <cstddef>
#include <vector>
#include <deque>
#include <iostream>
using namespace std;
struct TreeNode{
    int val;
    TreeNode*left;
    TreeNode*right;
    TreeNode(int data): val(data),left(NULL),right(NULL){}
};

class Solution{
public:
    vector<int> rightSideView(TreeNode*root){
        vector<int> result;
        if (root==NULL) return result;
        deque<TreeNode*> que;
        que.push_back(root);
        while (!que.empty()){
            int size = que.size();
            for (int i=0 ; i<size;i++){
                TreeNode*node = que.front();
                que.pop_front();
                if (node->left) que.push_back(node->left);
                if (node->right) que.push_back(node->right);
                if (i==size-1) result.push_back(node->val);
            }
        }
        return result;
    }
};


int main(){
    TreeNode*root = new TreeNode(1);
    root->left = new TreeNode(2);
    root->right = new TreeNode(3);
    root->left->right= new TreeNode(5);
    root->right->right = new TreeNode(4);

    Solution obj;
    vector<int> result = obj.rightSideView(root);
    for (const int val: result){
        cout<<val<<" ";
    }
}