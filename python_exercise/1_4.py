"""
最长有效括号

给你一个只包含'(' 和')'的字符串,找出最长有效(格式正确且连续)括号子串的长度

肯定是用stack,如何记录呢?

我们先初始化stack,里面存了一个-1(为什么是-1,后面解释)

遇到左括号的时候,压入栈中,这里我们要压入索引,这就很巧妙,因为我们需要计算两个括号之间的长度

遇到右括号的时候,就pop出去一个,如果此时栈不为空,那就可以记录当前有效括号子串的长度

                               如果为空,那就是没有办法匹配这个右括号,所以就要把这个索引压入栈中,来当作新的起始位置

为什么-1?
初始情况下，栈为空
处理第一个有效括号子串

"""

class Solution():

    def longestValidParentheses(self,s:str):

        max_length = 0 #记录最长的有效字符串括号
        stack = [-1]

        for i,val in enumerate(s):
            if val == "(":
                stack.append(i)  ##可以压入任何值，我们不关心
            else:
                ## 右括号,进行匹配,为什么需要初始-1,就是这里防止边界条件,
                stack.pop()

                if not stack: ## 如果stack为空了,说明前面没有匹配,所以把他当作新的起点
                    stack.append(i)
                else: ## 不为空,更新最长长度
                    max_length = max(max_length, i - stack[-1])

        return max_length






