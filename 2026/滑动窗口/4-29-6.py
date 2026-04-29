"""
最短覆盖子串

给你两个字符串：
s
t 

请你在s中找到一个最短连续子串，使得这个子串包含t中所有字符，包括重复字符。

如果不存在这样的子串，返回空字符串"".
"""

"""
窗口是什么？ 当前尝试覆盖 t 的连续子串
窗口维护的是什么？-> window 字典维护当前窗口中各字符出现次数；need 字典维护 t 中各字符需要次数；valid 维护已经满足要求的字符种类数。
窗口什么时候合法？ -> valid == len(need)。
什么时候移动left？ -> 当窗口已经满足时，移动 left，尝试缩短窗口
"""

from collections import Counter,defaultdict

def min_window(s: str, t: str) -> str:
    
    if not t or not s :
        return ""
    
    need = Counter(t) # 维护t中各个字符需要的次数
    window = defaultdict(int)
    left = 0 # 左指针
    valid = 0

    min_len = float("inf") #维护最短
    start =0 # 这里返回的不是长度，而是具体的子串，所以需要记录子串的起始位置

    for right in range(len(s)):
        c = s[right]
        # 加入
        window[c]+=1 

        # 满足字符是需要的且数量也对齐了
        if  c in need and window[c]==need[c]:
            valid +=1 

        # 满足条件
        while valid ==len(need):
            # 先更新答案
            if right-left+1<min_len:
                min_len = right-left+1
                start =left 

            # 缩小窗口
            d = s[left]
            window[d]-=1
            left+=1 

            # 如果移走的是需要的字符，那条件就要变化
            if d in need and window[d]<need[d]:
                valid -=1 

        
    if min_len == float("inf"):
        return ""
    
    return s[start:start+min_len]
    

if __name__=="__main__":
    s = "ADOBECODEBANC"
    t = "ABC"

    print(min_window(s,t))
    print(min_window("a", "a"))                # a
    print(min_window("a", "aa"))               # ""
    print(min_window("aaabcbc", "abc"))        # abc