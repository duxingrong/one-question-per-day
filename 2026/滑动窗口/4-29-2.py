"""
最多替换K个字符后的最长重复字符子串

给你一个只包含大写英文字母的字符串s，以及一个整数k

你最多可以替换k个字符，把它们改成任意大写字母

请你返回：经过最多k次替换后，能够得到的最长连续相同字符子串的长度

"""

def character_replacement(s: str, k: int) -> int:
    """维护一个窗口，使得 窗口长度 - max_count <= k"""

    ans = 0 # 维护结果
    count = {} # 记录窗口中的各个字符数量
    left = 0 # 左指针
    max_count = 0 # 记录窗口中最多重复字符的数量

    for right in range(len(s)):

        count[s[right]] = count.get(s[right],0) +1 
        
        max_count = max(max_count, count[s[right]])

        # 不满足条件时，就要缩小窗口
        while right-left +1 - max_count > k: # max_count 不下降可能会让当前窗口“看起来合法”，但这个窗口长度不会超过之前已经能真实达到的长度，所以 ans 不会错
            count[s[left]]-=1
            left+=1  

        
        ans = max(ans, right-left +1 )

    return ans 

if __name__ == "__main__":
    s= "AABABBA"
    k = 1 
    print(character_replacement(s,k))