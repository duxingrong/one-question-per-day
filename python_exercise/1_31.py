"""
233.数字1的个数

给定一个整数n,计算所有小于等于n的非负整数中数字1出现的个数。


纯数学知识

"""
class Solution:
    def countDigitOne(self,n:int)->int:

        # 变量
        digit = 1 # 权重
        count = 0 # 记录1个数

        while digit<=n:
            left = n//(digit*10)# 高位
            current = (n//digit)%10# 当前位
            right = n%digit #低位

            if current==0:
                count+=left*digit
            elif current==1:
                count +=left*digit+right+1
            elif current>1:
                count+=(left+1)*digit

            digit*=10 # 处理下一个数位

        return count



