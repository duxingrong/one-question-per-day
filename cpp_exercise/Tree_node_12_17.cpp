/*
二叉树的迭代遍历

迭代遍历无非就是利用stack来模仿递归罢了

前序好模仿，因为处理的就是中节点，后序是左右中，就是前序中左右变成中右左，然后反转即可。最难的是中序遍历，左中右，如何利用层序遍历
*/

#include <stack>
#include<vector>
#include <cstddef>
#include <algorithm>
using namespace std;

struct TreeNode{
    int val;
    TreeNode*left;
    TreeNode*right;
    TreeNode(int data ): val(data),left(NULL),right(NULL){}
};

//迭代遍历 前序遍历
class Solution{
public:
    vector<int> preordertraversal(TreeNode*root){
        vector<int> nums ;
        if (root==NULL) return nums; // 如果树为空，直接返回空数组
        stack<TreeNode*> st;
        st.push(root); 
        while (!st.empty()){
            TreeNode*cur = st.top();
            st.pop();
            nums.push_back(cur->val);
            //stack是先进后出，所以先将右孩子加入栈
            if (cur->right) st.push(cur->right);
            if (cur->left) st.push(cur->left);
        }
        return nums;
    }
};

//迭代遍历 后序遍历
class Solution{
public:
    vector<int>  postorderTraversal(TreeNode*root){
        vector<int> nums;
        if (root==NULL) return nums; //特殊情况
        stack<TreeNode*> st;
        st.push(root);
        while(!st.empty()){
            TreeNode*cur  = st.top();
            st.pop();
            nums.push_back(cur->val);
            if (cur->left) st.push(cur->left);
            if (cur->right) st.push(cur->right);
        }
        reverse(nums.begin() , nums.end()); // 反转之后就是左右中
        return nums;
    }
};


/*迭代遍历 中序遍历 只知道怎么做，却不知道为什么这么做
处理顺序和访问顺序不一致，所以需要借用指针的遍历来帮助访问节点，栈则用来处理
节点上的元素
两个步骤：
- 先走到最左子节点：在栈的帮助下，我们将一直深入到树的最左边，直到没有左子节点为止。
- 回溯处理节点：一旦没有左子节点，我们就弹出栈顶的节点，访问它
（即相当于访问根节点），然后转向它的右子树。
*/
class Solution{
public :
    vector<int> inorderTraversal(TreeNode*root){
        vector<int> nums;
        if (root==NULL) return nums; //特殊情况
        stack<TreeNode*> st;
        TreeNode*cur  = root; //利用指针来进入最底层
        while(cur!=NULL || !st.empty()){
            if(cur!= NULL){
                st.push(cur);
                cur = cur->left;
            }else {
                cur = st.top();
                st.pop();
                nums.push_back(cur->val);
                cur = cur->right;
            }
        }
        return nums;
    }
};



