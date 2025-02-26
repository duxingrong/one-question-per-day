"""
基本计算器

给你一个字符串表达式s,请你实现一个基本计算器来计算并返回它的值

注意：不允许使用任何将字符串作为数学表达式计算的内置函数，比如eval()


提示：
- 1 <= s.length <= 3 * 105
- s 由数字、'+'、'-'、'('、')'、和 ' ' 组成
- s 表示一个有效的表达式
- '+' 不能用作一元运算(例如， "+1" 和 "+(2 + 3)" 无效)
- '-' 可以用作一元运算(即 "-1" 和 "-(2 + 3)" 是有效的)
- 输入中不存在两个连续的操作符
- 每个数字和运行的计算将适合于一个有符号的 32位 整数

"""

class Solution:
    def calculate(self,s:str)->int:
        ## 变量
        stack = [] # 用于保存遇到'('时的结果和符号
        result = 0 # 当前的累加结果
        sign = 1   # 当前数字前的符号，1表示正，-1表示负
        i = 0      # 索引
        n = len(s) # 总长度

        ## 循环遍历字符串
        while i<n :
            # 如果遇到数字，就累积出完整的数字，然后和他前面的符号一起汇入result
            char = s[i]
            if char.isdigit(): # isdigit()判断是否是数字
                num = 0
                while i<n and s[i].isdigit():
                    num = num*10 + int(s[i])
                    i+=1
                result+= sign*num
                continue # 因为这里有i+=1，所以要跳过后面的i+=1

            # 遇到符号，就改变sign
            if char == "+":
                sign = 1
            if char == "-":
                sign = -1

            # 遇到括号，就保留状态，然后从新开始
            if char == "(":
                stack.append(result)
                stack.append(sign)

                # 重置
                result = 0
                sign = 1

            # 遇到')',就是计算结果并且和之前保存的一起汇总
            if char == ")":
                prev_sign = stack.pop()
                prev_result = stack.pop()
                result = prev_sign*result +prev_result

            i+=1

        return result


