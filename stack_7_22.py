"""
给出由小写字母组成的字符串 S，重复项删除操作会选择两个相邻且相同的字母，并删除它们。

在 S 上反复执行重复项删除操作，直到无法继续删除。

在完成所有重复项删除操作后返回最终的字符串。答案保证唯一。

示例：

输入："abbaca"
输出："ca"
"""
class Solution():
    def removeSame(self,s:str)->str:
         
        stack=[]   
        for i  in s:
            if stack and  i==stack[-1] :  #当栈不为空且栈顶等于i时，抵消
                stack.pop()
            else:
                stack.append(i)           #否则将i推入栈里
        return ''.join(stack)     #将列表转换成字符串
s='abbaca'
solution=Solution()
result=solution.removeSame(s)
print(result)


    
                