"""
单词接龙

字典wordList中从单词beginWord和endWord的转换序列是一个按下述规格形成的序列:
- 序列中第一个单词是beginWord
- 序列中最后一个单词是endWord
- 每次转换只能改变一个字母
- 转换过程中的中间单词必须是字典wordList中的单词
- 给你两个单词beginWord和endWord和一个字典wordList,找到从beginWord到endWord的最短转换序列中的单词数目.如果不存在这样的转换序列,返回0

beginWord='hit' 
endWord='cog'
wordList=['hot','dot','dog','lot','log','cog']
hit->hot->dot->dog->cog
长度为5，输出5

无向图求最短路径,广搜最为合适,广搜只要搜到了终点,就是最短路径
"""

from typing import List
from collections import deque


class Solution():
    def ladderLength(self,beginWord:str,endWord:str,wordList:List[str])->int:
        #特殊情况
        if endWord not in wordList:
            return 0
        
        #去重
        wordset =set(wordList)

        # 变量
        mapping = {beginWord:1}
        que = deque()
        que.append(beginWord)
        
        #广搜
        while que:
            word = que.popleft()
            path = mapping[word]

            #终止条件
            if word == endWord:
                return path

            #这种方式不用遍历所有的wordset,对于List很大的时候非常节约时间
            for i in range(len(word)):
                word_list = list(word)
                for j in range(26):
                    word_list[i]=chr(ord('a')+j)
                    newword = "".join(word_list)
                    if newword not in mapping and newword in wordset:
                        mapping[newword] = path+1
                        que.append(newword)

        #如果没有返回,说明没有路径
        return 0

if __name__=="__main__":
    beginWord='hit' 
    endWord='cog'
    wordList=['hot','dot','dog','lot','log','cog']
    solution = Solution()
    print(solution.ladderLength(beginWord,endWord,wordList))



                


