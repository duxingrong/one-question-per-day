"""

请根据每日气温列表，重新生成一个列表，对应位置的输出为:要想观测到更高的气温，至少需要等待的天数，如果气温在这之后都不会升高，请在该位置用0来代替


输入: [73,74,75,71,69,72,76,73]
输出: [ 1, 1, 4, 2, 1, 1, 0, 0]

单调栈就适合求比当前元素大或者小的第一个元素

这个真的很巧妙,我们这个单调栈记录的是每个元素的下标，这里我们要找的是比当前元素大的第一个元素，所以我们的栈要保持递增(就是栈顶到栈底是递增的),这样有意思的是，当我们发现遍历的元素要破坏这个递增的时候，就是我们收获结果的时候

首先stack.append(0)
for i in range(1,len(nums))
    while nums[i]>nums[stack[-1]]: 破坏了递增，所以收获结果
        result[stack[-1]]=i-stack[-1]
        stack.pop()
    stack.append(i) 如果比栈顶的小，加入还是递增，没有破坏,等待别人认领

这里的巧妙就在于，我们用单调栈记录了我们遍历过的元素，然后再遍历后面时候，可以拿来比较

"""

from typing import List

class Solution():
    def dailyTemperatures(self,nums:List[int])->List[int]:
        #初始化result
        result=[0]*len(nums)
        #初始化stack
        stack=[]
        stack.append(0)

        #遍历
        for i in range(1,len(nums)):
            while len(stack)>0 and nums[i]>nums[stack[-1]]:
                result[stack[-1]]=i-stack[-1]
                stack.pop()
            stack.append(i)
        return result

        
