"""
最多包含k个不同字符的最长子串

给你一个字符串s和一个整数k

请你返回：s中最多包含k个不同字符的最长连续子串长度

"""

"""
窗口是什么 -> 是最长、包含k个不同字符 的连续子串
窗口状态时什么 -> 是这个窗口中的每个字符的个数 -> 字典
什么时候合法  ->  窗口中 不同字符个数< = k 时
什么时候移动left -> 窗口中 不同字符个数 > k 时
"""

def length_of_longest_substring_k_distinct(s: str, k: int) -> int:
    "维护窗口中不同字符的个数"

    ans= 0 # 维护结果
    count = {} # 字典维护窗口中的不同字符的个数
    left = 0 # 左指针

    for right in range(len(s)):
        # 加入新元素
        count[s[right]] = count.get(s[right],0) +1 

        # 不合法就移动
        while len(count) > k : 
            count[s[left]]-=1
            # 必须把values=0的key给删除掉
            if count[s[left]] == 0:
                del count[s[left]]
            left+=1 

        ans = max(ans,right-left+1)

    return ans 

if __name__ == "__main__":
    s = "eceba"
    k = 2 
    print(length_of_longest_substring_k_distinct(s,k))

