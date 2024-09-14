"""
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。

有效字符串需满足：

左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
注意空字符串可被认为是有效字符串。

输入: "()"
输出: true


要往这个栈与队列的方向去思考，怎么用呢？
"""

class Solution():
    def isValid(self,s:str)->bool:
        
        stack=[]
        for i in s:
            #当为左括号时，就将右括号输入栈中 
            if i=='(':
                stack.append(')')
            elif i=='{':
                stack.append('}')
            elif i=='[':
                stack.append(']')
            #当为右括号时，如果此时栈为空，或者栈的栈顶不等于此时的i
            elif not stack or stack[-1]!=i:
                return False
            #当栈顶等于此时的时，就将栈顶推出用来抵消
            else:
                stack.pop()
        #遍历完成后如果栈为空则说明括号正确，否则False
        return True if not stack else False

            
s="([])()"
solution=Solution()
result=solution.isValid(s)
print(result)

