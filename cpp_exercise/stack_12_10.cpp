/*
用队列实现栈 

使用队列实现栈的下列操作:
push(x) -- 元素x入栈
pop()   -- 移除栈顶元素
top()   -- 获取栈顶元素
empty() -- 返回栈是否为空


只能使用队列的基本操作
push to back 
peek/pop from front 
size 
is empty()
可以假设所有的操作都是有效的，对一个空的栈不会调用pop或者top操作
*/


#include <queue>
using namespace std;


//一个队列在模拟栈弹出元素的时候只要将队列头部的元素（除了最后一个元素外)
//重新添加到队列尾部，此时再去弹出元素就是栈的顺序了
class MyStack{
public:
    queue<int> que;

    MyStack() {}

    void push(int x){
        que.push(x);
    }

    int  pop(){
        for (int i=0;i<que.size()-1;i++){
            int res =que.front();
            que.pop();
            que.push(res);
        }
        int result = que.front();
        que.pop();
        return result;
    }

    int top(){
        int result = this->pop();
        que.push(result);
        return result;
    }

    bool empty(){
        return que.empty();
    }
};