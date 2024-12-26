"""

根据数字二进制下1的数目排序

给你一个整数数组arr.请你将数组中的元素按照其二进制表示中数字1的数目升序排序

如果存在多个数字的二进制中1的数目相同,则必须将他们按照树值大小升序排列

请你返回排序后的数组

arr= [0,1,2,3,4,5,6,7,8]
输出:[0,1,2,4,8,3,5,6,7]

0有0个1
1,2,4,8二进制中有1个1
3,5,6,7二进制中有2个1

"""

from typing import List

class Solution():
    def sortByBits(self,arr:List[int])->List[int]:
        table = {}
        for val in arr:
            tmp = self.muchOne(val)
            if tmp not in table:
                table[tmp] = []

            table[tmp].append(val)

        result = []
        #从字典中按顺序取出添加到result中
        for key in sorted(table.keys()):
            result.extend(sorted(table[key])) #extend会展开传入的可迭代对象，逐个加入

        return result


    def muchOne(self,val):
        result = 0
        while val:
            val &= val-1 #就这里，没进行一次这个运算，就会把二进制中的最后一个1变成0
            result+=1
        return result


if __name__=="__main__":
    solution = Solution()
    arr= [0,1,2,3,4,5,6,7,8]
    print(solution.sortByBits(arr))
