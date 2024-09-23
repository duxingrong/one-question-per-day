"""
给定一个字符串s,将s分割成一些子串,使每个子串都是回文串,返回s所有可能的分割方案
什么是回文串?
答:从前往后读和从后往前读是一样的
*确实很难想,但是既然现在懂了,那肯定下次就会*
"""


"""
回溯的三步骤
参数:str  
返回: List[str]
终止条件: 通过画图可以知道,所有的结果不管是不是都是在叶子节点处得到,也就当startindex=len(digits)的时候
单层逻辑:
我们是一步一步去判断能不能分割成回文串的集合的,当startindex=0的时候,我们会先取区间[0,1),如果他是,则再看[1,2),然后[2,3),其中每当遇到不是的时候,就没必要让他做任何处理,直接跳过就好,如果是,他会在[3,4),这个循环中满足终止条件直接添加值后返回,startindex=0对应的是我们开局只分一个字符,当0的处理完后,我们会开局就取2位,然后继续,然后依次下去
"""

from typing import List
class Solution():
    def partition(self,digits:str)->List[str]:
        result = []
        if len(digits)==0:
            return result
        self.traversal(digits,0,[],result)
        return result


    def traversal(self,digits,startindex,path,result):
        # 终止条件
        if startindex==len(digits):  # 能到这一步的都是子集是回文串,不然直接被剪枝了
            result.append(path[:])
            return 
        
        # 单层逻辑
        for i in range(startindex,len(digits)):
            if digits[startindex:i+1]==digits[startindex:i+1][::-1]:      #  因为是左闭右开,所以要写的是i+1,我们取的是[startindex,i]
                path.append(digits[startindex:i+1])
                self.traversal(digits,i+1,path,result)
                path.pop()



digits="aab"
solution=Solution()
print(f"这个字符串分割子集回文串的方式有{solution.partition(digits)}")











