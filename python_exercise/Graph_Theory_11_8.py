"""
字典strList中从字符串beginStr和endStr的转换序列是一个按下述规格形成的序列:
1. 序列中第一个字符串是beginStr.
2. 序列中最后一个字符串endStr.
3. 每次转换只能改变一个字符
4. 转换过程中的中间字符串必须是字典strList中的字符串
给你两个字符串beginStr和endStr 和一个strList，找到从beginStr 到endStr 的最短转换序列中的字符串数目，如果不存在这样的转换序列，返回0

输入描述:
第一行包含一个整数N，表示字典strList中的字符串数量.第二行包含两个字符串用空格隔开，分别代表beginStr 和endStr . 后序N行，每行一个字符串，代表strList中的字符串

输出描述:
找出一个整数.代表从beginStr转换到endStr需要的最短转换序列中的字符串数量，如果不存在样的转换序列，则输出0.

6 
abc def 
efc 
dbc
ebc
dec
dfc
yhn

4


这个题目，其实就是无向图寻找最短路径,我们需要使用广搜，因为广搜找到了就是最短路径，不用判断了
"""

from collections import deque



class Solution():
    def __init__(self):
        self.strList = []

    #判断是否是只有一个字母不同
    def judge(self,x,y):
        count = 0
        for i in range(len(x)):
            if x[i]!=y[i]:
                count+=1
        return count==1
        
    def main(self):
        n = int(input())
        beginStr,endStr = map(str,input().split())
        #判断特殊情况
        if beginStr==endStr:
            print(0)
            return 
        for _ in range(n):
            self.strList.append(input())
        self.visited = [False]*n

        #使用bfs,还需要作标记防止重复
        q = deque()
        q.append([beginStr,1])
        while  q:
            Str,step = q.popleft()
            #判断是否等于了endStr
            if self.judge(Str,endStr):
                print(step+1)
                return 
            for i in range(len(self.strList)):
                if self.judge(Str,self.strList[i]) and self.visited[i]==False:
                    self.visited[i]=True
                    q.append([self.strList[i],step+1])


solution =Solution()
solution.main()




