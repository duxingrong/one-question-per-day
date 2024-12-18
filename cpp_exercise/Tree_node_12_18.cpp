/*
二叉树的统一迭代法

难点就是无法同时解决访问节点(遍历节点)和处理节点(将元素放入结果集)不一致的情况

那我们就将访问的节点放入栈中，把要处理的节点也放入栈中但是要做标记
就是在要处理的节点放入栈之后，紧接着放入一个空指针作为标记，标记法

*/

#include <vector>
#include <stack>
#include <cstddef>
#include <iostream>
using namespace std;

struct TreeNode{
    int val;
    TreeNode*left;
    TreeNode*right;
    TreeNode(int data): val(data),left(NULL),right(NULL){}
};


class Solution{
public :
    //前序遍历
    vector<int> preorderTraversal(TreeNode*root){
        stack<TreeNode*> st;
        vector<int> result ;
        if (root==NULL) return result;
        st.push(root);
        while (!st.empty()){
            TreeNode*cur = st.top();
            if (cur!=NULL){
                st.pop();
                if (cur->right) st.push(cur->right);
                if (cur->left) st.push(cur->left);
                st.push(cur);
                st.push(NULL);
            }else {
                st.pop();
                cur = st.top();
                st.pop();
                result.push_back(cur->val);
            }
        }
        return result;
    }
    //中序遍历
    vector<int> InorderTraversal(TreeNode*root){
        vector<int> result;
        stack<TreeNode*> st;
        if (root==NULL) return result;
        st.push(root);
        while (!st.empty()){
            TreeNode*cur = st.top();
            if (cur!= NULL){
                st.pop();
                if (cur->right) st.push(cur->right);
                st.push(cur);
                st.push(NULL);
                if (cur->left ) st.push(cur->left);
            }else {
                st.pop();
                cur = st.top();
                st.pop();
                result.push_back(cur->val);
            }
        }
        return result;

    }
    //后序遍历
    vector<int> postorderTraversal(TreeNode*root){
        vector<int> result;
        stack<TreeNode*> st;
        if (root==NULL) return result;
        st.push(root);
        while (!st.empty()){
            TreeNode*cur = st.top();
            if (cur!= NULL){
                st.push(NULL);
                if (cur->right) st.push(cur->right);
                if (cur->left ) st.push(cur->left);
            }else {
                st.pop();
                cur = st.top();
                st.pop();
                result.push_back(cur->val);
            }
        }
        return result;
    }


};





int main(){
    TreeNode* root = new TreeNode(1);
    root->left = new TreeNode(2);
    root->right = new TreeNode(3);
    root->left->left = new TreeNode(4);
    root->left->right = new TreeNode(5);
    root->right->left = new TreeNode(6);
    root->right->right = new TreeNode(7);
    Solution obj;
    vector<int> result = obj.preorderTraversal(root);
    for (const int val:result ){
        cout<<val<<" ";
    }
}