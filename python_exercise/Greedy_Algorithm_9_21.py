"""
字符串S由小写字母组成,我们要把这个字符串划分为尽可能多的片段,同一字母最多出现在一个片段中,返回一个表示每个字符串片段的长度的列表
S='ababcbacadefegdehijhklij'
输出[9,7,8] ['ababcbaca','defegde','hijhklij']
"""
"""
怎么知道到什么时候要将val加入result中,并且重置为0呢?
找到同一个字母的最大区间范围?(很接近了,但是本题目我们只需要记录每个字母的最远位置下标就好了)-->利用哈希表来记录
然后,我们再一次遍历字符串,我们不断更新最远的位置,然后如果i==最远处的位置,记录长度,然后重置继续遍历
"""
from typing import List

class Solution():
    def partitionLabels(self,S:str)->List[int]:
        # 用哈希表来记录每个字母的最远处位置
        hash=[0]*26
        for i in range(len(S)):
            hash[ord(S[i])-ord('a')]=i
        # 现在第二步遍历
        # 初始化
        left=0  # 区间初始左边界
        right=0
        result=[]
        for i in range(len(S)):
            right=max(right,hash[ord(S[i])-ord('a')])
            if i==right:
                result.append(right-left+1)
                left=i+1
        return result
"""
字典时间更快
"""
class Solution1():
    def partitionLabels(self,S:str)->List[int]:
        # 用python独特的字典
        dict={}
        for i ,val in enumerate(S):
            dict[val]=i
        start=end=0
        result=[]
        for i in range(len(S)):
            end=max(end,dict[S[i]])
            if i==end:
                result.append(end-start+1)
                start=end+1
        return result

S='ababcbacadefegdehijhklij'
solution=Solution1()
print(f"分成区间的长度分别是{solution.partitionLabels(S)}")
