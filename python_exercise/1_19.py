"""
126. 单词接龙||
按字典wordList完成从单词beginWord到单词endWord转化,一个表示此过程的转换序列是形式上像beginWord->s1->s2->...->sk这样的单词序列，并满足:
- 每对相邻的单词之间仅有单个字母不同
- 转换过程中的每个单词si(1<=i<=k)必须是字典中wordList中的单词。注意,beginWord不必是字典wordList中的单词。
sk==endWord
给你两个单词beginWord和endWord,以及一个字典wordList。请你找出并返回从beginWord到endWord的最短转换序列，如果不存在这样的转换序列，返回一个空列表。每个序列都应该以单词列表[beginWord,s1,s2,...,sk]的形式返回
"""

from typing import List
from collections import deque,defaultdict
class Solution:
    def findLadders(self,beginWord:str,endWord:str,wordList:List[str])->List[str]:
        # 去重
        wordSet = set(wordList)

        # 特殊情况
        if endWord not in wordList:
            return []


        # 用于存储BFS过程中每个单词的前驱节点
        pre_dict = defaultdict(list)
        # 用来记录单词是否已经访问
        visited = set()
        visited.add(beginWord)
        # 利用队列来实现
        que = deque()
        que.append(beginWord)
        found = False

        # BFS查找最短路径
        while que and not found:
            # 本层新访问的单词
            current_level_visited = set()
            for _ in range(len(que)):
                word = que.popleft()
                # 尝试替换单词的每个字符
                for i in range(len(word)):
                    for c in 'abcdefghijklmnopqrstuvwxyz':
                        if word[i]==c:
                            continue
                        new_word = word[:i]+c+word[i+1:]
                        if new_word in wordSet and new_word not in visited:
                            if new_word == endWord:
                                found = True
                            if new_word not in current_level_visited:
                                que.append(new_word)
                                current_level_visited.add(new_word)
                            # 记录前驱节点
                            pre_dict[new_word].append(word)
            visited.update(current_level_visited)

        # 如果没有找到路径，返回空
        if not found:
            return []

        # 回溯构建所有最短路径
        res = []

        def backtrack(path,word):
            if word==beginWord:
                res.append(path[::-1])
                return 
            for prev_word in pre_dict[word]:
                backtrack(path+[prev_word],prev_word)

        backtrack([endWord],endWord)
        return res # **BFS只会寻找最短的路径**
        


