"""
单词搜索||

给定一个mXn二维字符网络board和一个单词(字符串)列表words,返回所有二维网络上的单词

单词必须按照字母排序，通过相邻的单元格内的字母构成，其中"相邻"单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母在一个单词中不允许被重复使用

"""

"""
前缀树，用来实现单词存储，快速查找
self.children是一个字典，键是当前的子字母,值是指向子节点的TrieNode
self.word用于存储完整单词，只有当这个节点是一个单词的结尾时，才会存储单词，否则None
"""

class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self,word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.word=word # 最后一个节点才有word

from typing import List


class Solution:
    def findWords(self,board:List[List[str]],words:List[str])->List[str]:
        # 用前缀树来存储单词
        trie = Trie()
        for word in words:
            trie.insert(word)

        self.result = set()
        self.board = board
        self.rows , self.cols = len(board),len(board[0])
        root = trie.root

        # 遍历整个board，每个点都可能是单词的起点
        for r in range(self.rows):
            for c in range(self.cols):
                if board[r][c] in root.children: # 说明找到了单词的第一个字母
                    ## DFS
                    self.dfs(r,c,root)

        return list(self.result) # 转换成列表

    
    def dfs(self,r,c,node):
        char = self.board[r][c]



        next_node = node.children[char]
        if next_node.word: # 如果发现下一个字母它有word,说明下一个字母是结尾
            self.result.add(next_node.word)
            next_node.word = None # 避免重复加入

        # 标记已访问
        self.board[r][c]='#'

        # 开始四个方向继续深搜
        directions = [(-1,0),(1,0),(0,-1),(0,1)]
        for dr,dc  in directions:
            nr ,nc= r+dr,c+dc
            ## 防止越界
            if 0<=nr<self.rows and 0<=nc<self.cols and self.board[nr][nc] in next_node.children:
                # 继续DFS
                self.dfs(nr,nc,next_node)

        # 还原现场
        self.board[r][c]=char # 回溯










            
