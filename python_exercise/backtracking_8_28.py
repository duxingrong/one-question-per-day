"""
给定一个数组candidates和一个目标target,找出candidates中所有可以使数字和为target的组合(每个位置只能使用一次)
这里最大的难题就在于给出的数组是有重复数字的,我们需要进行去重,这里的去重复的意思是: 比如[1,1,2] 我们第一个1在穷举时就会有[1,1],[1,2],[1,1,2] 然后这时候如果我们在遍历第二个1的时候,就会取得[1,2] 如果[1,2]是答案的话,这就是重复了,所以其实第一个1他的情况会包含后面所有的1的情况,所以我们去重就是同一层中不再遍历相同的数字(树层去重),而我们的一层遍历是由for循环来决定的,所以就是在for 这里添加判断条件(i>startindexand candidates[i]=candidates[i-1]),具体的情况想一想就知道了,因为你今天懂了
"""




"""
参数 candidates , target 
返回 result
终止条件: if sum(path)==target result.append(path[:]) return    or  sum(path)>target return 
单层逻辑:  for i in range(startindex,len(candidates)) 由于不能重复取,所以下一层的时候startindex = i+1
树枝去重和树层去重:
对一一个数组[1,1,2]来说,我们允许他结果集里面有两个1,但是到树层for循环遍历的时候,我们不能在取1,因为后面的1的所有情况都已经被第一个1给取完了,再取就是重复的
"""
from typing import List
class Solution():
    def combinationSum2(self,candidates:List[int],target:int)->List[List[int]]:
        result = []
        if len(candidates)==0:
            return result 
        candidates = sorted(candidates) # 首先对数组进行排序,所以必须去重
        self.traversal(candidates,target,0,[],result)
        return result
    def traversal(self,candidates,target,startindex,path,result):
        # 终止条件
        if sum(path)>target:
            return 
        if sum(path)==target:
            result.append(path[:])

        # 单层逻辑
        for i in range(startindex,len(candidates)):
            if i>startindex and candidates[i]==candidates[i-1] :  # 神之一手,我们只允许所有遍历时候,重复的数字只有第一次才会继续,后面预见的都需要舍去
                continue
            val = candidates[i]
            path.append(val)
            self.traversal(candidates,target,i+1,path,result)
            path.pop()



num =[10,1,2,7,6,1,5]
target = 8

solution = Solution()
result =solution.combinationSum2(num,target)
print(result)
