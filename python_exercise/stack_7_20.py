"""
使用队列实现栈的下列操作：

push(x) -- 元素 x 入栈
pop() -- 移除栈顶元素
top() -- 获取栈顶元素
empty() -- 返回栈是否为空
"""
"""
队列是先进先出，栈是先进后出
"""
from collections import deque
class MyStack():
    def __init__(self):
        self.que=deque()
        
    
    def push(self,x:int):
        self.que.append(x)

    def pop(self)->int:
        if self.empty():
            return None
        else:
            for _  in  range(len(self.que)-1):
                self.que.append(self.que.popleft())
        return self.que.popleft()
    

    def top(self)->int:
        ans=self.pop()
        self.que.append(ans)
        return ans
    
    def empty(self)->bool:
        return not self.que
    
    """
    转换duque为列表，使得内容以列表的形式显示
    str()将列表转换成字符串
    """
    def __str__(self)->str:
            
        return str(list(self.que))
        
        

stack=MyStack()
stack.push(1)
stack.push(2)
stack.push(3)
print(stack)
print(stack.pop())
print(stack.top())
print(stack)
print(stack.empty())

