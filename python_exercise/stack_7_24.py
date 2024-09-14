from collections import deque
from typing import List

#制造一个单调递减的数列，这样当我们求最大值时，只用看队列的首位就可以了
class MyQueue():
    def __init__(self):
        self.queue=deque()

    #当队列不为空，并且当value等于queue的最大值时，才需要进行pop操作，因为我们本来队列里只维护最大值
    def pop(self,value):
        if self.queue and value==self.queue[0]:
            self.queue.pop()
    
    def push(self,value):
        while self.queue and value>self.queue[-1]:  #也就是说，我们维护递减队列，只用保留有可能成为最大值的元素
            self.queue.pop()
        self.queue.append(value)
    
    def front(self):
        return self.queue[0]
    
#现在开始移动滑动窗口
class Solution():
    def getMac(self,nums:List[int],k:int):
        que=MyQueue()
        result=[]
        for i in range(k):
            que.push(nums[i])
        result.append(que.front())   #记录前k个中的最大值
        for i in range(k,len(nums)):
            que.pop(nums[i-k])  #窗口移除最前面元素
            que.push(nums[i])   #窗口加入一个新元素
            result.append(que.front())
        return result

nums=[1,3,-1,-3,5,3,6,7]
solution=Solution()
result=solution.getMac(nums,3)
print(result)