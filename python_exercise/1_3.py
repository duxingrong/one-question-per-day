"""
串联所有单词的子串

给定一个字符串s和一个字符串数组words,words中所有字符串长度相同

s中的串联子串是指一个包含words中所有字符串以任意顺序排列起来的子串

返回所有串联子串在s中的开始索引,你可以任意顺序返回答案

s= 'barfoothefoobarman',words = ['foo','bar'] 输出[0,9]

如果没有返回[]


"""

from collections import Counter  #字典子类,专门用来统计哈希对象的频率
from typing import List

class Solution():
    def findSubstring(self,s:str,words:List[str])->List[int]:
        """
        我们利用滑动窗口,也就是我们比较滑动窗口中的单词频率和words中的频率,要确认正确,就要满足,频率不超过且长度刚刚好
        """

        ## 变量
        word_len = len(words[0])
        n = len(words)
        total_len = word_len*n #每个单词的长度*个数
        words_count = Counter(words) #是一个字典
        result = [] #记录结果

        ## 遍历所有能充当滑动窗口开始的位置
        for i in range(word_len):
            left = i
            right = i
            window_count = Counter()
            ## 开始往窗口中填充
            while right+word_len <=len(s):
                word = s[right:right+word_len]
                right += word_len #指向了下一个单词的首字母

                ## 判断这个单词在不在words中
                if word in words:
                    window_count[word]+=1
                    ## 如果发现多余,那就需要剔除到不超过为止
                    while window_count[word]>words_count[word]:
                        left_word = s[left:left+word_len]
                        window_count[left_word]-=1
                        left+=word_len

                    ## 如果发现长度达标且度过了上面的频率检查
                    if right-left ==total_len:
                        result.append(left)

                ## 如果单词都不是的,那说明要直接清空,因为是滑动窗口
                else:
                    window_count.clear()
                    left = right
        
        return result
                    

        
