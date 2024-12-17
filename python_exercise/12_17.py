"""
分割平衡字符串

在一个平衡字符串中，'L'和'R'字符的数量是相同的

给你一个平衡字符串s，请你将它分割成尽可能多的平衡字符串

注意:分割得道的每个字符串都必须是平衡字符串

返回可以通过分割得到的平衡字符串的最大数量


s="RLRRLLRLRL" 输出: 4

"""

"""
感觉就直接看flag为0的次数?(还真是)
"""

class Solution():
    def balancedStringSplit(self,s:str)->int:
        flag = 0 #判断当前元素前面的R和L的数量
        result = 0
        for i in range(len(s)):
            if s[i] == 'R':
                flag+=1 
            else :
                flag-=1
            if flag == 0:
                result+=1
        return result

if __name__=="__main__":
    solution = Solution()
    s = "RLRRLLRLRL" 
    print(solution.balancedStringSplit(s))
