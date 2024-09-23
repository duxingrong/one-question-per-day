"""
给定一个只包含数字的字符串,复原他并返回所有可能的ip地址的格式
有效的ip地址:正好有4个整数(每个整数位于0-255之间组成,且不能含有前导0--就是除非就是0,不然数字不能用0来开头),整数之间用"."来分离.
"""


"""
回溯的三步骤:
1.参数: s:一个字符串 
2.result: 所有ip地址 List[str]
3. 终止条件:
首先,我们只需要分成4段,所以就是三个".",我们可以用一个参数point_sum来判断终止条件 if point_sum==3: 这里加判断第4段是不是有效的,如果是,result.append(current+s[startindex:]) 不管满不满足,都需要返回
4. 单层逻辑 :
for i  in range(startindex,len(s)): if s[startindex,i] 是有效的,就递归继续 否则直接break
为什么直接break?
这是因为不合法有两种情况:
1: ip只能三位数且小于255,如果当前不合法,那在往后4位更不可能,直接break
2: 前导是0,那也是一样的,这个0一直在这里,你后面加什么都不会合法,直接break
"""
from typing import List
class Solution():
    # 主函数
    def restoreIpAddresses(self,s:str)->List[str]:
        result=[]
        if len(s)==0:
            return result
        self.backtracking(s,0,0,"",result)
        return result
    # 判断是否有效的函数
    def is_valid(self,s,start,end):
        if start>end:
            return False  # 代码健壮性(系统只会单独看这个函数有没有缺陷,所以要满足函数的健壮性)
        if s[start]=="0" and start!=end:
            return False
        if int(s[start:end+1])>255:
            return False
        return True
    # 回溯函数
    def backtracking(self,s,startindex,point_sum,current,result):
        # 终止条件
        if point_sum==3:
            if self.is_valid(s,startindex,len(s)-1): # 因为这里是闭区间:
                result.append(current+s[startindex:len(s)]) # 这里是开区间
            return
        # 单层逻辑
        for i in range(startindex,len(s)):
            # 判断分割的是不是有效
            if self.is_valid(s,startindex,i):
                self.backtracking(s,i+1,point_sum+1,current+s[startindex:i+1]+".",result)
            else:
                break

s="25525511135"
solution=Solution()
result = solution.restoreIpAddresses(s)
print(result)

