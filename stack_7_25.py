"""
给定一个非空的整数数组，返回其中出现频率前 k 高的元素。

示例 1:

输入: nums = [1,1,1,2,2,3], k = 2
输出: [1,2]
"""
from typing import List
from collections import  defaultdict
class Solution():
    def function(self,nums:List[int],k:int)->List:
        time_dict={}
        #通过字典统计每个元素出现的次数
        for num in nums:
            time_dict[num]+=1
        #更改字典，key为出现次数，value为相应的数字的集合
        index_dict=defaultdict(list)    #---创建一个字典，每个键的默认值都是一个空列表
        for key in time_dict:
            index_dict[time_dict[key]].append(key)  #--将频率设置为键，将所有达到这个次数的元素以列表方式设置为频率的值
        #排序
        key=list(index_dict.keys())  #--首先获取所有的键，然后以列表方式取出
        key.sort()
        #取出前k项
        result=[]
        cnt=0
        while key and cnt !=k:         
            result+=index_dict[key[-1]]        #--result会得到所有该频率下的元素值
            cnt+=len(index_dict[key[-1]])      #--有cnt来记录result中有了几个元素值
            key.pop()                          #--将最高频率弹出，然后重复
        return result[0:k]

            
            

