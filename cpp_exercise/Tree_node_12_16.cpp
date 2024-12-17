/*
二叉树的递归遍历
前序遍历 -  中序遍历 -  后序遍历 

递归三部曲:
1. 确定递归函数的参数和返回值
2. 确定终止条件
3. 确定单层递归的逻辑
*/


#include <vector>
#include <cstddef> //引入NULL
using namespace std;

//二叉树
struct  TreeNode{
    int val; 
    TreeNode*left;
    TreeNode*right;
    TreeNode(int data):val(data),left(NULL),right(NULL){}
};


//前序遍历- 中左右
class Solution{
public:
    void dfs(TreeNode*cur , vector<int>& res){
        if (cur == NULL) return ;
        res.push_back(cur->val);
        dfs(cur->left , res);
        dfs(cur->right,res);
    }

    vector<int> preorderTraversal(TreeNode*root){
        vector<int> res ;
        dfs(root,res);
        return res;
    }
};


//中序遍历-左中右
class Solution{
public:
    void dfs(TreeNode*cur , vector<int>& res){
        if (cur == NULL) return ;
        dfs(cur->left , res);
        res.push_back(cur->val);
        dfs(cur->right,res);
    }

    vector<int> inorderTraversal(TreeNode*root){
        vector<int> res ;
        dfs(root,res);
        return res;
    }
};

//后序遍历-左右中
class Solution{
public:
    void dfs(TreeNode*cur , vector<int>& res){
        if (cur == NULL) return ;
        dfs(cur->left , res);
        dfs(cur->right,res);
        res.push_back(cur->val);
    }

    vector<int> postorderTraversal(TreeNode*root){
        vector<int> res;
        dfs(root,res);
        return res;
    }
};