"""
有一个队列,他的people[i]=[hi,ki],表示他的身高(hi),表示他前面有几个比他高或者等于(ki)
现在是一个乱序的,你要把他排序让他们的位置和他们的hi以及ki一一对应
例如:
people=[[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]
排序后 [[5,0],[7,0],[6,1],[7,1],[5,2],[4,4]]
"""


"""
怎么贪心呢?
像这种两个纬度的题目,我们都一般方法都是先确定其中一个维度,然后在确定另外一个纬度
这里我们如果先确定k的话,我们就会按从小到大去排列,但是会发现排好后还是很乱
先确定h的话,我们就按照从大到小排列,然后我们会发现,有希望了,我们只需要再根据k去调整位置就好!
"""
from typing import List

class Solution():
    def function(self,people:List[List[int]])->List[List[int]]:
        # 首先对数组按照第一个元素降序排序,然后第二优先级是第二个元素升序排序
        people=sorted(people,key=lambda x:(-x[0],x[1]))
        print(people) # 调试

        # python中插入不会让后面的值消失,所以要重新定义一个二维数组
        result=[]

        for i in range(len(people)):
            result.insert(people[i][1],people[i])
        return result

people=[[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]
solution=Solution()
people=solution.function(people)
print(f"排序后的队列是{people}")
