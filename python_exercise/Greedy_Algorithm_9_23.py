"""
给定一个非负整数N,找出小于或者等于N的最大的整数,同时这个整数需要满足其各个位数上的数字是单调递增(平坡也算增)
例如N=10
输出:9
N=332
输出:299
"""

"""
确定位数
每一位怎么取？从左到右还是从右到左
方法:
1. 我们两位两位比较,如果两位不是递增,那就需要将前一位减减,那此时后一位肯定取9才及时止损
2. 所有我们是从右到左,才能让改正位置的后面全部取9
"""
class Solution():
    def monotoneIncreasingDigits(self,N:int)->int:
        strNum=list(str(N))
        print(strNum)
        # 从右到左遍历
        for i in range(len(strNum)-1,0,-1):
            # 如果当前位置<前一位
            if strNum[i]<strNum[i-1]:
                strNum[i-1]=str(int(strNum[i-1])-1)
                # 将后面的所有数字都变成9
                strNum[i:]='9'*(len(strNum)-i) # 直接考虑如果最后一个就是这里,那就是不改,所以是(len(strNum)-i)
                print(strNum)
        return int("".join(strNum))# 把转成列表的str合并然后转成数字
            

Number=4352
solution=Solution()
result=solution.monotoneIncreasingDigits(Number)

print(result)










