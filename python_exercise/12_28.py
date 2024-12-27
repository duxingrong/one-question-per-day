"""
查询数组中元素的出现位置

给你一个整数数组nums,一个整数数组queries和一个整数X

对于每个查询queries[i],你需要找到nums中第queries[i]个的x的位置,并返回它的下标.如果数组中x的出现次数少于queries[i],该查询的答案为-1

"""

from typing import List

class Solution():
    def occurrencesOfElement(self,nums:List[int],queries:List[int],x:int)->List[int]:
        x_pos = []
        #首先得到一个哈希表
        for i in range(len(nums)):
            if nums[i]==x: 
                x_pos.append(i)

        result = [] 
        for index in queries:
            if index-1>=len(x_pos):
                result.append(-1)
            else:
                result.append(x_pos[index-1])
        return result


if __name__=="__main__":
    nums = [1,3,1,7]
    queries = [1,3,2,4]
    x = 1
    solution = Solution()
    print(solution.occurrencesOfElement(nums,queries,x))

