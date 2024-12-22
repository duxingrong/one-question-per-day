/*
N叉树的层序遍历

给定一个N叉树,返回其节点值的层序遍历.(即从左到右,逐层遍历)

 */

#include <cstddef>
#include <deque>
#include <iostream>
#include <vector>
using namespace std;

// N叉树类
class Node {
public:
  int val;
  vector<Node *> children;

  Node() {}

  Node(int _val) { val = _val; }

  Node(int _val, vector<Node *> _children) {
    val = _val;
    children = _children;
  }
};

class Solution {
public:
  vector<vector<int>> levelOrder(Node *root) {
    // 特殊情况
    vector<vector<int>> result;
    if (root == NULL)
      return result;
    // 队列
    deque<Node *> que;
    que.push_back(root);
    while (!que.empty()) {
      int length = que.size();
      vector<int> level;
      for (int i = 0; i < length; i++) {
        Node *node = que.front();
        que.pop_front();
        // 加入数组
        level.push_back(node->val);
        for (int i = 0; i < node->children.size(); i++) {
          if (node->children[i] != NULL)
            que.push_back(node->children[i]);
        }
      }
      result.push_back(level);
    }
    return result;
  }
};

class Solution {
public:
  vector<vector<int>> levelOrder(Node *root) {
    // 特殊情况
    vector<vector<int>> result;
    if (root == NULL)
      return result;
    dfs(root, 0, result);
    return result;
  }
  void dfs(Node *node, int depth, vector<vector<int>> &result) {
    // 首先判断有没有当前层
    if (depth == result.size())
      result.push_back(vector<int>());
    result[depth].push_back(node->val);

    for (int i = 0; i < node->children.size(); i++) {
      if (node->children[i])
        dfs(node->children[i], depth + 1, result);
    }
  }
};

int main() {
  // 创建根节点
  Node *root = new Node(1);

  // 创建子节点
  Node *child1 = new Node(2);
  Node *child2 = new Node(3);
  Node *child3 = new Node(4);

  // 添加子节点到根节点
  root->children.push_back(child1);
  root->children.push_back(child2);
  root->children.push_back(child3);

  // 实例化
  Solution obj;
  vector<vector<int>> result = obj.levelOrder(root);
  for (const vector<int> nums : result) {
    for (const int val : nums) {
      cout << val << " ";
    }
    cout << endl;
  }

  // 清理内存
  delete root;
  delete child1;
  delete child2;
  delete child3;

  return 0;
}
