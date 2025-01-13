"""
最小覆盖子串

给你一个字符串s,一个字符串t.返回s中t所有字符的最小子串.如果s中不存在覆盖t所有字符的子串,则返回空字符串"".

双指针?滑动窗口?
"""

class Solution:
    def minWindow(self,s:str,t:str)->str:
        ## 特殊情况
        if len(s)<len(t):
            return ""

        table = {}

        for char in t:
            table[char] = table.get(char, 0)+1
            

        ## 滑动窗口
        window = {}
        left = 0
        valid = 0 # 记录的是窗口中满足条件的字符数量
        min_len = float('inf')
        start = 0 # 记录起始位置

        for right in range(len(s)):
            char = s[right]

            ## 添加到window中
            if char in table:
                window[char]= window.get(char,0)+1
                ## 如果满足相等了，说明窗中这个字符满了
                if window[char] == table[char]:
                    valid +=1 

                ## 如果valid 和table 想等，说明满足了条件，移动左边和更新值了
                while valid == len(table):
                    ## 更新
                    if right - left +1 <min_len:
                        min_len  =  right-left +1
                        start = left ## 方便后面取值

                    ## 移动左边
                    char_remove = s[left]
                    left +=1
                    if  char_remove in table:
                        if window[char_remove]== table[char_remove]: ## 这里只用关心等号就好，因为只有==的时候，我们移除了才是动本
                            valid -=1 
                        window[char_remove]-=1 

        return  "" if min_len== float('inf') else s[start : start+min_len]



            





