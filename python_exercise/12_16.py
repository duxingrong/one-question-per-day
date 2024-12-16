"""
Dota2参议院

Dota2的世界里有两个阵营: Radiant(天辉)和Dire(夜魔)

Dota2 参议院由来自两派的参议员组成。现在参议院希望对一个 Dota2 游戏里的改变作出决定。他们以一个基于轮为过程的投票进行。
在每一轮中，每一位参议员都可以行使两项权利中的一项：

1. 禁止一名参议员的权利：参议员可以让另一位参议员在这一轮和随后的几轮中丧失所有的权利。

2. 宣布胜利：如果参议员发现有权利投票的参议员都是同一个阵营的，他可以宣布胜利并决定在游戏中的有关变化。

给定一个字符串代表每个参议员的阵营。字母 “R” 和 “D” 分别代表了 Radiant（天辉）和 Dire（夜魇）。
然后，如果有 n 个参议员，给定字符串的大小将是 n。

以轮为基础的过程从给定顺序的第一个参议员开始到最后一个参议员结束。
这一过程将持续到投票结束。所有失去权利的参议员将在过程中被跳过。

假设每一位参议员都足够聪明，会为自己的政党做出最好的策略，
你需要预测哪一方最终会宣布胜利并在 Dota2 游戏中决定改变。输出应该是 Radiant 或 Dire。

例如输入"RRDDD"，执行过程应该是什么样呢？

第一轮: senate[0]的R消灭senate[2]的D,senate[1]的R消灭senate[3]的D,senate[4]的D消灭senate[0]的R,此时剩下"RD"，第一轮结束！
第二轮:senate[0]的R消灭senate[1]的D,第二轮结束
第三轮:只有R了,R胜利
"""


"""
这个题目诀窍就在这点上,每一个议员怎样使用权力才是最优解?
例如RDDRD 
s[0]的R解决了s[1]的D,那么s[2]的D是解决s[3]还是s[0]的R,当然是解决他后面的R,因为这一轮中s[0]已经使用权力了，
但是s[3]的R却还可以消灭D,所以:
每一个议员都应该消灭他后面的敌人,因为他前面的敌人已经用过权力了，但是他后面的敌人却还可以消灭自己的同伴

局部最优:有一次权力机会，就解决后面的敌人->全局最优:为自己阵营赢得最大利益

"""

class Solution():
    def predictPartyVictory(self,senate:str)->bool:
        #首先变成列表，方便操作
        senate = list(senate)
        #R为true，说明这轮结束后还会有R，D同理
        R = True 
        D = True 

        #利用flag 他的正负代表了当前议员前面的数量是敌人多还是队友多，从而来判断自己是否被消灭了(这个就是这道题目的技巧)
        #flag>0 表示R在D前面，R可以消灭D , flag< 0 表示D在R前面，D可以消灭R 
        flag = 0 

        while R and D:
            R =False 
            D =False
            for i in range(len(senate)):
                if senate[i] == 'R':
                    if flag <0: senate[i]='0' #D消灭了R
                    else: R=True #表示这轮结束这个R没有被消灭，还存在R 
                    flag +=1
                if senate[i] == 'D':
                    if flag>0: senate[i] ='0' 
                    else: D=True 
                    flag -=1 

        return 'Radiant' if R else 'Dire'




if __name__=="__main__":
    solution = Solution()
    print(solution.predictPartyVictory("RRDDD")) 
    print(solution.predictPartyVictory("RDDRD"))  

