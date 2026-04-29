"""
最长不含重复字符的字串

给你一个字符串s，请你返回其中不含重复字符的最长连续子串的长度，是连续子串，不是子序列


s = "abcabcbb" 输出 3 "abc"

时间复杂度：O(n)
空间复杂度：O(n)

"""


def length_of_longest_substring(s: str) -> int:
    """维护的就是一个子串"""

    ans = 0 # 维护答案
    count = {} # 字典维护是否存在重复的字符
    left = 0 # 窗口左指针

    for right in range(len(s)):

        # 当存在重复时
        while count.get(s[right],0) != 0:
            count[s[left]]-=1  
            left +=1 

        count[s[right]] = count.get(s[right], 0) + 1
        ans  = max(ans , right-left+1 ) 
    
    return ans

if __name__ == "__main__":
    s = "abcabcbb"
    print(length_of_longest_substring(s))