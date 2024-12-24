/*
填充每个节点的下一个右侧节点指针

给定一个完美二叉树,其所有叶子节点都在同一层,每个父节点都有两个子节点


填充它的每个next指针,让这个指针指向其下一个右侧节点.如果找不到下一个右侧节点
则将next指针设置为NULL
*/

//迭代法还是简单的

#include <cstddef>
#include <vector>
#include <deque>
using namespace std;

class Node {
public:
    int val;
    Node* left;
    Node* right;
    Node* next;

    Node() : val(0), left(NULL), right(NULL), next(NULL) {}

    Node(int _val) : val(_val), left(NULL), right(NULL), next(NULL) {}

    Node(int _val, Node* _left, Node* _right, Node* _next)
        : val(_val), left(_left), right(_right), next(_next) {}
};


class Solution{
public: 
    Node* connect(Node*root){
        //特殊情况
        if (root==NULL) return NULL;
        deque<Node*> que;
        que.push_back(root);
        while (!que.empty()){
            int length = que.size();
            for (int i = 0;i<length;i++){
                Node*node = que.front();
                que.pop_front();
                if (i!=length-1){                
                node->next = que.front();
                }
                if (node->left) que.push_back(node->left);
                if (node->right)que.push_back(node->right);
            } 
        }
        return root;
    }
};


//主要看递归
class Solution{
public:
    void dfs(Node*root){
        //终止条件
        if (root==NULL) return ;
        
        //当前节点来处理下一层的next 
        if (root->left){ //完全二叉树,有左必有右
            root->left->next = root->right;
        }
        if (root->right){
            if (root->next)
                root->right->next = root->next->left;
            else 
                root->right->next = NULL; 
        }

        dfs(root->left);
        dfs(root->right);
    }

    Node* connect(Node*root){
        dfs(root);
        return root;
    }
};