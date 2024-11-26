"""

独一无二的出现次数


给你一个整数数组arr，请你帮忙统计数组中的每个数的出现次数,如果每个数组的出现次数是独一无二的，就返回true,否则返回false

arr.length = (1,1001)
arr[i] = (-1000,1001)

"""

#很明显的记录次数的就用哈希表，然后看是否一样，就用一个标记数组


from typing import List


class Solution():
    def uniqueOccurrences(self,nums:List[int])->bool:
        #初始化哈希表
        hash = [0]*2001

        #哈希表来记录每个数字出现的次数,+1000防止负索引
        for i in range(len(nums)):
            hash[nums[i]+1000]+=1

        #标记数组
        freq = [False]*1001

        #判断是否重复
        for i  in range(len(hash)):
            if hash[i]>0:
                if freq[hash[i]] ==False: #记录这个次数用过了
                    freq[hash[i]] = True
                else:#再用就False
                    return False

        return True

    def uniqueOccurrences(self,nums:List[int])->bool:
        #用哈希表记录
        table = {}
        for num in nums:
            table[num] = table.get(num,0)+1

        #使用set
        len_set = len(set(table.values()))
        len_values = len(table)

        return len_set == len_values


            



        


