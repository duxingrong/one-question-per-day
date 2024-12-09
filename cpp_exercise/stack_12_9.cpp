/*
用栈实现队列

使用栈实现队列的下列操作

push(x)- 将一个元素放入队列的尾部
pop()- 从队列首部移除元素
peek()- 返回队列首部的元素
empty()- 返回队列是否为空

你只能使用标准的栈操作 - push to top ; -peek/pop from top ; size ; is empty
;是合法的


队列两边都可以出 , 栈只能栈顶出
所以用两个栈来模拟队列
 */
#include <stack>
#include <stdexcept> // 引入 std::runtime_error
using namespace std;

class MyQueue {
public:
  stack<int> stIn;
  stack<int> stOut;

  /* Initialize your data structure here. */
  MyQueue() {}

  /* Push element x to the back of queue.*/
  void push(int x) { stIn.push(x); }

  /* Removes the element from in the front of queue and returns that element */
  int pop() {
    // 如果stOut没值了，添加值，然后pop()
    if (stOut.empty()) {
      // 保证stIn不为空
      if (stIn.empty()) {
        throw runtime_error("Queue is empty!");
      }

      while (!stIn.empty()) {
        stOut.push(stIn.top());
        stIn.pop();
      }
    }
    int result = stOut.top();
    stOut.pop();
    return result;
  }

  /* Get the front element */
  int peek() {
    int res = this->pop();
    stOut.push(res);
    return res;
  }

  /* Returns whether the queue is empty */
  bool empty() { return stIn.empty() && stOut.empty(); }
};
