"""
用栈实现队列：

push(x) -- 将一个元素放入队列的尾部。
pop() -- 从队列首部移除元素。
peek() -- 返回队列首部的元素。
empty() -- 返回队列是否为空。

栈操作的是栈顶，队列操作的是队列首尾。
"""
class MyQueue():
    def __init__(self):
        """
        定义两个栈，一个负责操作队列尾部，一个负责操作队列首部。
        """
        self.stack_in=[]
        self.stack_out=[]

    def push(self,x:int)->None:
        """
        作用是放在队列的尾部，那直接往self.stack_in操作就好
        """ 
        self.stack_in.append(x)

    def pop(self)->int:
        #判断是否为空队列
        if self.empty():
            return None 
        else:
            if self.stack_out:
                return self.stack_out.pop()
            else:
                for _ in range(len(self.stack_in)):
                    self.stack_out.append(self.stack_in.pop()) 
                return self.stack_out.pop()
    
    def peek(self)->int:
        ans=self.pop()
        self.stack_out.append(ans)
        return ans
    
    def empty(self)->bool:
        return  not  (self.stack_in or self.stack_out)

    def __str__(self) -> str:
        """
        返回队列的字符串表示
        """
        if self.stack_out:
            return str(self.stack_out[::-1] + self.stack_in)
        else:
            return str(self.stack_in)
queue=MyQueue()
print(queue.empty())
queue.push(1)
queue.push(2)
queue.push(3)
print(queue)
print(queue.pop())
print(queue.peek())
print(queue)  
                 

            
